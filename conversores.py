import subprocess
import yt_dlp
import os
import requests
from PIL import Image
from io import BytesIO

def converter_imagem(caminho_entrada, caminho_saida):
    foto = Image.open(caminho_entrada)
    foto_rgb = foto.convert('RGB')
    foto_rgb.save(caminho_saida)

def converter_midias(caminho_entrada, caminho_saida):
    comando = ["ffmpeg", "-loglevel", "quiet", "-y", "-i", caminho_entrada, caminho_saida]
    subprocess.run(comando)

def baixar_midias(url, caminho_saida = ".", so_audio=False):
    modelo_saida = os.path.join(caminho_saida, '%(title)s.%(ext)s')
    ydl_opts = {
        'outtmpl': modelo_saida,
        'quiet': True,
        'no_warnings' : True,
        'socket_timeout': 30,
        'retries': 10,
        'fragment_retries': 10,
    }
    if so_audio:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',

            }],
        })
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def baixar_imagem(url, caminho_saida):
    resposta = requests.get(url)
    resposta.raise_for_status()
    imagem = Image.open(BytesIO(resposta.content))
    if caminho_saida.lower().endswith(('.jpg', '.jpeg')) and imagem.mode in ('RGBA', 'LA'):
        imagem = imagem.convert('RGB')
    imagem.save(caminho_saida)