import subprocess
import yt_dlp
import os
import requests
import sys
from PIL import Image
from io import BytesIO

def _obter_caminho_ffmpeg():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    caminho_local = os.path.join(base_path, 'ffmpeg.exe')
    
    if os.path.exists(caminho_local):
        return caminho_local
    return 'ffmpeg'

FFMPEG_PATH = _obter_caminho_ffmpeg()

def converter_imagem(caminho_entrada, caminho_saida):
    img = Image.open(caminho_entrada)
    extensao_destino = caminho_saida.split('.')[-1].lower()
    
    if extensao_destino == 'ico':
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        img_hd = img.resize((256, 256), Image.Resampling.LANCZOS)
        icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img_hd.save(caminho_saida, format='ICO', sizes=icon_sizes)
    else:
        if extensao_destino in ['jpg', 'jpeg'] and img.mode in ('RGBA', 'LA', 'P'):
            fundo_branco = Image.new('RGB', img.size, (255, 255, 255))
            fundo_branco.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = fundo_branco
            
        img.save(caminho_saida)

def converter_midias(caminho_entrada, caminho_saida):
    comando = [FFMPEG_PATH, "-loglevel", "quiet", "-y", "-i", caminho_entrada, caminho_saida]
    subprocess.run(comando)

def baixar_midias(url, caminho_saida=".", so_audio=False):
    modelo_saida = os.path.join(caminho_saida, '%(title)s.%(ext)s')
    pasta_ffmpeg = os.path.dirname(FFMPEG_PATH) if os.path.isabs(FFMPEG_PATH) else None

    ydl_opts = {
        'outtmpl': modelo_saida,
        'quiet': True,
        'no_warnings': True,
        'socket_timeout': 30,
        'retries': 10,
        'fragment_retries': 10,
    }

    if pasta_ffmpeg:
        ydl_opts['ffmpeg_location'] = pasta_ffmpeg

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