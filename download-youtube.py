#!/usr/bin/env python3
import os
import re
import argparse
import subprocess
from pytubefix import YouTube

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
FFMPEG_PATH = os.path.join(diretorio_atual, "ffmpeg", "bin", "ffmpeg.exe")

def sanitize_filename(name, max_length=200):
    """Remove caracteres proibidos e encurta o nome."""

    name = name.replace('/', '-').replace('\\', '-')
    name = re.sub(r'[^A-Za-z0-9À-ÖØ-öø-ÿ _\-.]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()

    if len(name) > max_length:
        name = name[:max_length].rstrip()

    return name.replace(' ', '_')

def check_ffmpeg_available():
    return os.path.isfile(FFMPEG_PATH)

def baixar_audio_ffmpeg(arquivo_input, arquivo_output, formato):
    """Converte qualquer arquivo de áudio para mp3 ou wav usando ffmpeg."""
    cmd = [
        FFMPEG_PATH, "-y", "-i", arquivo_input,
        "-vn"  # sem vídeo
    ]

    if formato.lower() == "mp3":
        cmd += ["-b:a", "320k"]

    cmd.append(arquivo_output)
    completed = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if completed.returncode != 0:
        raise RuntimeError(f"ffmpeg falhou:\n{completed.stderr.decode(errors='ignore')}")

def baixar_mp3_wav(yt, destino_dir, formato):
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    if not audio_stream:
        raise RuntimeError("Nenhum stream de áudio disponível para esse vídeo.")

    print("Baixando melhor stream de áudio disponível...")
    arquivo_temp = audio_stream.download(output_path=destino_dir, filename="temp_audio")

    titulo = sanitize_filename(yt.title)
    caminho_final = os.path.join(destino_dir, f"{titulo}.{formato}")

    print(f"Convertendo para {formato.upper()} usando FFmpeg...")
    baixar_audio_ffmpeg(arquivo_temp, caminho_final, formato)

    os.remove(arquivo_temp)
    return caminho_final

def baixar_mp4(yt, destino_dir):
    progressive = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    titulo = sanitize_filename(yt.title)
    caminho_final = os.path.join(destino_dir, f"{titulo}.mp4")

    if progressive:
        print(f"Baixando stream progressivo (vídeo+áudio) — {progressive.resolution} ...")
        caminho_temp = progressive.download(output_path=destino_dir, filename="temp_video")
        os.rename(caminho_temp, caminho_final)
        return caminho_final

    print("Nenhum stream progressivo disponível. Vou baixar vídeo e áudio separadamente e mesclar com FFmpeg...")

    video_stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    if not video_stream or not audio_stream:
        raise RuntimeError("Não foi possível encontrar streams de vídeo e áudio para mesclar.")

    if not check_ffmpeg_available():
        raise RuntimeError("FFmpeg não encontrado no caminho especificado.")

    arquivo_video = video_stream.download(output_path=destino_dir, filename="temp_video")
    arquivo_audio = audio_stream.download(output_path=destino_dir, filename="temp_audio")
    temp_merged = os.path.join(destino_dir, "merged.mp4")

    cmd = [
        FFMPEG_PATH, "-y",
        "-i", arquivo_video,
        "-i", arquivo_audio,
        "-c", "copy",
        temp_merged
    ]

    print("Mesclando vídeo e áudio com FFmpeg...")

    completed = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if completed.returncode != 0:
        raise RuntimeError(f"FFmpeg falhou ao mesclar arquivos:\n{completed.stderr.decode(errors='ignore')}")

    os.rename(temp_merged, caminho_final)
    os.remove(arquivo_video)
    os.remove(arquivo_audio)
    return caminho_final

def download(link, diretorio_destino, formato="mp3"):
    if formato not in ("mp3", "wav", "mp4"):
        raise ValueError("Formato inválido. Use 'mp3', 'wav' ou 'mp4'.")

    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino, exist_ok=True)

    print("\nObtendo informações do vídeo...")
    yt = YouTube(link)
    print(f"Vídeo encontrado: {yt.title}")

    try:
        if formato in ("mp3", "wav"):
            caminho = baixar_mp3_wav(yt, diretorio_destino, formato)
            print(f"Áudio salvo em: {caminho}")
        else:
            caminho = baixar_mp4(yt, diretorio_destino)
            print(f"Vídeo MP4 salvo em: {caminho}")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro durante o download/conversão: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Baixa áudio (MP3/WAV) ou vídeo (MP4) de um link do YouTube."
    )
    parser.add_argument("-u", "--url", required=True, help="URL do vídeo do YouTube")
    parser.add_argument("-f", "--format", default="mp3", choices=["mp3", "wav", "mp4"], help="Formato de saída")
    parser.add_argument("-o", "--output", required=True, help="Diretório onde o arquivo será salvo")
    args = parser.parse_args()

    try:
        download(args.url, args.output, args.format.lower())
    except Exception as err:
        print(f"Erro: {err}")
        exit(1)
