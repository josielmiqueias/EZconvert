import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.iniciar_app()

    def iniciar_app(self):
        if self.process:
            self.process.kill()  # Fecha a janela antiga
        
        # sys.executable garante que o script use o MESMO python do venv que rodou o dev.py
        self.process = subprocess.Popen([sys.executable, "app.py"])

    def on_modified(self, event):
        # Se o arquivo alterado for o app.py, reinicia
        if event.src_path.endswith("app.py"):
            print("\n[LIVE RELOAD] Alteração detectada no app.py! Recarregando janela...")
            self.iniciar_app()

if __name__ == "__main__":
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    print("--- LIVE RELOAD ATIVO ---")
    print("Modifique o app.py e salve (Ctrl + S) para ver as mudanças ao vivo.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.kill()
    observer.join()