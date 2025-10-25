🎬 YouTube Downloader (Áudio & Vídeo)


Script em Python para baixar áudio (MP3/WAV) ou vídeo (MP4) de vídeos do YouTube em alta qualidade.
Suporta streams progressivos e, caso não haja, faz mescla automática de vídeo e áudio usando FFmpeg.

📦 Requisitos

Python 3.7+

Bibliotecas Python:

pip install pytubefix


FFmpeg (necessário para conversão e mesclagem):

Ubuntu/Debian:

sudo apt install ffmpeg


Windows:
Baixe em https://ffmpeg.org/download.html
Coloque na mesma pasta do script com o nome ./ffmpeg


⚡ Funcionalidades

Baixa áudio em MP3 ou WAV em alta qualidade.

Baixa vídeo em MP4:

Stream progressivo: vídeo + áudio juntos.

Caso contrário: baixa vídeo-only + áudio-only e mescla automaticamente.

Sanitiza nomes de arquivos para evitar erros.

Cria diretório de destino se não existir.

Tratamento de erros com mensagens claras.

CLI amigável com -h para ajuda.

🛠️ Uso
Sintaxe
python download-youtube.py -u [URL] -f [FORMATO] -o [DIRETORIO]

Argumentos
Flag	Opção	Descrição
-u / --url	URL	Link do vídeo do YouTube (obrigatório)
-f / --format	mp3, wav, mp4	Formato de saída (padrão: mp3)
-o / --output	PATH	Diretório onde o arquivo será salvo (obrigatório)
-h / --help	—	Exibe ajuda detalhada com exemplos
Exemplos

Baixar áudio em MP3 (padrão):

python download-youtube.py -u "https://youtu.be/abc123" -o "/home/user/musicas"


Baixar áudio em WAV:

python download-youtube.py -u "https://youtu.be/abc123" -f wav -o "/home/user/musicas"


Baixar vídeo em MP4:

python download-youtube.py -u "https://youtu.be/abc123" -f mp4 -o "/home/user/videos"

⚠️ Observações

FFmpeg é necessário para:

Conversão de MP3/WAV

Mesclar vídeo-only + áudio-only para MP4

O script escolhe automaticamente a melhor qualidade disponível.

Nomes de arquivos longos ou com caracteres especiais serão sanitizados automaticamente.

🧰 Estrutura do projeto
download-youtube.py
README.md