# 🎬 **YouTube Downloader (Áudio & Vídeo)**  
![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-critical?logo=ffmpeg)

> 💡 Script em **Python** para baixar **áudio (MP3/WAV)** ou **vídeo (MP4)** do **YouTube** em alta qualidade.  
> Suporta streams progressivos e, caso não haja, faz mescla automática de vídeo e áudio usando **FFmpeg**.

---

## 📦 **Requisitos**

### 🐍 Python
- Versão **3.7+**

### 📚 Bibliotecas Python
Instale as dependências com:
```bash
pip install pytube pydub
```
### 🎞️ FFmpeg (necessário para conversão e mesclagem)
🐧 Ubuntu/Debian:
```bash
sudo apt install ffmpeg
```
### 🪟 Windows:

Baixe em https://ffmpeg.org/download.html  
Adicione dentro do projeto com o nome: **ffmpeg**

### ⚡ Funcionalidades

✅ Baixa áudio em MP3 ou WAV com alta qualidade  
✅ Baixa vídeo em MP4  
 └─ Stream progressivo (vídeo + áudio juntos)  
 └─ Caso contrário: baixa separadamente e mescla com FFmpeg  
✅ Sanitiza nomes de arquivos automaticamente  
✅ Cria diretório de destino se não existir  
✅ Tratamento de erros com mensagens claras  
✅ CLI amigável (-h para ajuda)  

### 🛠️ Uso
📘 Sintaxe
```bash
python downloader.py -u [URL] -f [FORMATO] -o [DIRETORIO]
```

#### ⚙️ Argumentos
| Flag            | Opção         | Descrição                                             |
| --------------- | ------------- | ----------------------------------------------------- |
| `-u / --url`    | URL           | Link do vídeo do YouTube (**obrigatório**)            |
| `-f / --format` | mp3, wav, mp4 | Formato de saída (**padrão:** mp3)                    |
| `-o / --output` | PATH          | Diretório onde o arquivo será salvo (**obrigatório**) |
| `-h / --help`   | —             | Exibe ajuda detalhada com exemplos                    |

### 💡 Exemplos
### 🎧 Baixar áudio em MP3 
```` bash
python downloader.py -u "https://youtu.be/abc123" -f mp3 -o "/home/user/musicas"
````

#### 🎵 Baixar áudio em WAV
```` bash
python downloader.py -u "https://youtu.be/abc123" -f wav -o "/home/user/musicas"
````
### 🎬 Baixar vídeo em MP4
```` bash
python downloader.py -u "https://youtu.be/abc123" -f mp4 -o "/home/user/videos"
````

### ⚠️ Observações Importantes
**FFmpeg é obrigatório para:**

- Conversão de MP3/WAV  
- Mesclar vídeo-only + áudio-only para MP4  
- O script escolhe automaticamente a melhor qualidade disponível.  
- Nomes de arquivos longos ou com caracteres especiais são sanitizados automaticamente.

  
