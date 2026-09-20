import os
import sys
import ctypes
import traceback
import webview

import conversores

try:
    myappid = 'ezconvert.app.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

PASTA_PADRAO = os.path.join(os.path.expanduser('~'), 'Downloads')

def _trocar_extensao(caminho_entrada, novo_formato):
    base = os.path.splitext(caminho_entrada)[0]
    return f'{base}_convertido.{novo_formato.lower()}'

class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def selecionar_arquivo(self, tipo):
        if tipo == 'imagem':
            file_types = ('Imagens (*.jpg;*.jpeg;*.png;*.webp;*.bmp;*.gif;*.tiff;*.ico)', 'Todos os arquivos (*.*)')
        else:
            file_types = ('Mídias (*.mp4;*.mkv;*.avi;*.mov;*.webm;*.mp3;*.wav;*.flac;*.aac;*.ogg)', 'Todos os arquivos (*.*)')

        result = self._window.create_file_dialog(
            webview.OPEN_DIALOG,
            allow_multiple=False,
            file_types=file_types
        )
        return result[0] if result else None

    def selecionar_pasta(self):
        result = self._window.create_file_dialog(webview.FOLDER_DIALOG)
        return result[0] if result else None

    def caminho_padrao(self):
        return PASTA_PADRAO

    def converter_imagem_ui(self, caminho_entrada, formato):
        try:
            if not caminho_entrada or not os.path.isfile(caminho_entrada):
                return {'ok': False, 'erro': 'Arquivo de origem não encontrado.'}
            caminho_saida = _trocar_extensao(caminho_entrada, formato)
            conversores.converter_imagem(caminho_entrada, caminho_saida)
            return {'ok': True, 'saida': caminho_saida}
        except Exception as e:
            traceback.print_exc()
            return {'ok': False, 'erro': str(e)}

    def converter_midia_ui(self, caminho_entrada, formato):
        try:
            if not caminho_entrada or not os.path.isfile(caminho_entrada):
                return {'ok': False, 'erro': 'Arquivo de origem não encontrado.'}
            caminho_saida = _trocar_extensao(caminho_entrada, formato)
            conversores.converter_midias(caminho_entrada, caminho_saida)
            if not os.path.isfile(caminho_saida):
                return {'ok': False, 'erro': 'A conversão falhou. Verifique se o ffmpeg está instalado.'}
            return {'ok': True, 'saida': caminho_saida}
        except Exception as e:
            traceback.print_exc()
            return {'ok': False, 'erro': str(e)}

    def baixar_midia_ui(self, url, pasta, so_audio):
        try:
            if not url:
                return {'ok': False, 'erro': 'Informe uma URL válida.'}
            pasta_destino = pasta or PASTA_PADRAO
            os.makedirs(pasta_destino, exist_ok=True)
            conversores.baixar_midias(url, pasta_destino, so_audio)
            return {'ok': True, 'pasta': pasta_destino}
        except Exception as e:
            traceback.print_exc()
            return {'ok': False, 'erro': str(e)}

def _obter_caminho_base():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    api = Api()
    base_path = _obter_caminho_base()
    html_file = os.path.join(base_path, 'web', 'index.html')
    icon_file = os.path.join(base_path, 'web', 'assets', 'icons', 'iconv3v.ico')

    if not os.path.exists(icon_file):
        icon_file = None

    window = webview.create_window(
        'EZconvert',
        html_file,
        js_api=api,
        width=1000,
        height=700,
        resizable=True
    )
    api.set_window(window)

    webview.start(icon=icon_file)