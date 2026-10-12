import subprocess
import yt_dlp
import os
import requests
import sys
import mimetypes
import time as te
import threading
from datetime import datetime
from urllib.parse import urlparse
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
    subprocess.run(comando, check=True)

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

def baixar_imagem(url, pasta_destino="."):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    resposta = requests.get(url, headers=headers, timeout=15)
    resposta.raise_for_status()
    imagem = Image.open(BytesIO(resposta.content))
    formato = (imagem.format or 'jpeg').lower()
    
    extensoes = {
        'jpeg': '.jpg',
        'png': '.png',
        'webp': '.webp',
        'gif': '.gif',
        'bmp': '.bmp'
    }
    extensao = extensoes.get(formato, '.jpg')
    
    nome_arquivo = f"imagem_{datetime.now().strftime('%Y%m%d_%H%M%S')}{extensao}"
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    if extensao in ('.jpg', '.jpeg') and imagem.mode in ('RGBA', 'LA', 'P'):
        fundo_branco = Image.new('RGB', imagem.size, (255, 255, 255))
        fundo_branco.paste(imagem, mask=imagem.split()[-1] if imagem.mode == 'RGBA' else None)
        imagem = fundo_branco

    imagem.save(caminho_completo)
    return caminho_completo

# animacaozinha pra eu fazer lá no terminal
animacaoC = {"rodando": False, "thread": None}
def animacao():
    print("Convertendo", end="", flush=True)
    while animacaoC["rodando"]:
        te.sleep(0.67)
        print(".", end="", flush=True)
        sys.stdout.flush()
def iniciar_animacao():
    if animacaoC["thread"] and animacaoC["thread"].is_alive():
        return
    animacaoC["rodando"] = True
    t = threading.Thread(target=animacao)
    t.daemon = True
    t.start()
    animacaoC["thread"] = t
def parar_animacao():
    animacaoC["rodando"] = False
    if animacaoC["thread"]:
        animacaoC["thread"].join(timeout=1.0)
    print()