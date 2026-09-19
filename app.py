import customtkinter as ctk
import os
import threading
from urllib.parse import urlparse
from conversores import converter_imagem, converter_midias, baixar_imagem, baixar_midias

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EZconvert - Conversor de arquivos")
        self.geometry("650x450")
        self.resizable(False, False)
        self.label_titulo = ctk.CTkLabel(self, text="EZconvert", font=("Brainstorm", 116, "bold"))
        self.label_titulo.pack(pady=15)
        self.tabview = ctk.CTkTabview(self, width=600, height=350)
        self.tabview.pack(pady=10)
        self.tab_imagem = self.tabview.add("Imagens")
        self.tab_midia = self.tabview.add("Mídias")
        self.tab_midiaURL = self.tabview.add("URL Mídias")
        self.tab_imagemURL = self.tabview.add("URL Imagens")
        self.caminho_img_selecionada = None
        self.caminho_midia_selecionada = None
        self.caminho_salvamento = None

        self.setup_tab_imagem()

        self.setup_tab_midia()

        self.setup_tab_midiaURL()

        self.setup_tab_imagemURL()

    def setup_tab_imagem(self):
        self.btn_selecionar_imagem = ctk.CTkButton(
            self.tab_imagem,
            text="Selecionar Imagem",
            command=self.selecionar_img
        )
        self.btn_selecionar_imagem.pack(pady=15)
        self.lbl_arquivo_imagem = ctk.CTkLabel(self.tab_imagem, text="Nenhum local selecionado")
        self.lbl_arquivo_imagem.pack(pady=5)
        self.opt_formato_img = ctk.CTkOptionMenu(
            self.tab_imagem,
            values=["PNG", "JPG", "WEBP", "TIFF", "PDF", "BMP", "ICO", "GIF"]
        )
        self.opt_formato_img.pack(pady=15)

        self.btn_converter_imagem = ctk.CTkButton(
            self.tab_imagem,
        text="Converter imagem",
        fg_color="green",
        hover_color="darkgreen",
        command=self.executar_conversao_img
        )
        self.btn_converter_imagem.pack(pady=15)

    def selecionar_img(self):
        caminho = ctk.filedialog.askopenfilename(
            title="Selecione a imagem",
            filetypes=[
                ("Arquivos de Imagem", ("*.png", "*.jpg", "*.jpeg", "*.webp", "*.tiff", "*.bmp", "*.ico", "*.gif")),
                ("Todos os arquivos", "*.*")
                ]
        )
        if caminho:
            self.caminho_img_selecionada = caminho
            self.lbl_arquivo_imagem.configure(text=caminho)

    def popup(self, mensagem, tempo_ms=3000, cor_fundo="darkgrey", cor_texto="white"):

        if hasattr(self, "popup_ativo") and self.popup_ativo is not None:
            try:
                self.popup_ativo.destroy()
            except Exception:
                pass

        self.popup_ativo = ctk.CTkFrame(self, fg_color=cor_fundo, corner_radius=10)
        self.popup_ativo.place(relx=0.98, rely=0.95, anchor="se")

        lbl = ctk.CTkLabel(self.popup_ativo, text=mensagem, font=("Arial", 13, "bold"), text_color=cor_texto)
        lbl.pack(expand=True, fill="both", padx=15, pady=(10,5))

        barra = ctk.CTkProgressBar(self.popup_ativo, height=3, progress_color="white", mode="determinate")
        barra.pack(fill="x", side="bottom", padx=10, pady=(0, 8))
        barra.set(0.0)

        intervalo = 16
        passos = tempo_ms / intervalo
        incremento = 1.0 / passos

        def atualizar_barra():
            if not hasattr(self, "popup_ativo") or self.popup_ativo is None or not barra.winfo_exists():
                return

            valor_atual = barra.get()
            if valor_atual < 1.0:
                barra.set(valor_atual + incremento)
                self.after(intervalo, atualizar_barra)
            else:
                self.popup_ativo.destroy()
                self.popup_ativo = None

        atualizar_barra()

    def executar_conversao_img(self):
        if not self.caminho_img_selecionada:
            self.popup(mensagem="Erro! Nenhum arquivo / ficheiro selecionado...", tempo_ms=2500, cor_fundo="darkred")
            return
        formato = self.opt_formato_img.get()
        imagem_selecionada = self.caminho_img_selecionada
        nome_imagem, extensao = os.path.splitext(imagem_selecionada)
        imagem_nova = nome_imagem + '.' + formato.lower()
        self.popup(mensagem="Convertendo imagem, aguarde..!", tempo_ms=3000)
        def tarefa():
            try:
                converter_midias(imagem_selecionada, imagem_nova)
                self.after(0, lambda: self.popup(mensagem="Imagem convertida com sucesso!!", tempo_ms=3000))
            except Exception as e:
                self.after(0, lambda: self.popup(mensagem=f"Erro na conversão: {e}", tempo_ms=3000, cor_fundo="darkred"))
        threading.Thread(target=tarefa, daemon=True).start()


    def setup_tab_midia(self):
        self.btn_selecionar_midia = ctk.CTkButton(
            self.tab_midia,
            text="Selecionar mídia",
            command=self.selecionar_midia
            )
        self.btn_selecionar_midia.pack(pady=15)
        self.lbl_arquivo_midia = ctk.CTkLabel(self.tab_midia, text="Nenhum local selecionado")
        self.lbl_arquivo_midia.pack(pady=5)
        self.opt_formato_midia = ctk.CTkOptionMenu(
            self.tab_midia,
            values=["MP4", "MOV", "WEBM", "AVI", "ASF", "MKV", "WMV", "FLV", "MP3", "OGG", "WAV", "M4A", "FLAC", "AIFF"]
            )
        self.opt_formato_midia.pack(pady=15)
    
        self.btn_converter_midia = ctk.CTkButton(
            self.tab_midia,
            text="Converter mídias",
            fg_color="green",
            hover_color="darkgreen",
            command=self.executar_conversao_midia
            )
        self.btn_converter_midia.pack(pady=15)
    
    def selecionar_midia(self):
        caminho = ctk.filedialog.askopenfilename(
            title="Selecione a mídia",
            filetypes=[
                ("Arquivos de mídia", ("*.mp4", "*.avi", "*.mp3", "*.webm", "*.flac", "*.wav", "*.ogg", "*.m4a", "*.mov", "*.aiff", "*.flac", "*.flv")),
                ("Todos os arquivos", "*.*")
            ]
        )
        if caminho:
            self.caminho_midia_selecionada = caminho
            self.lbl_arquivo_midia.configure(text=caminho)

    def executar_conversao_midia(self):
        if not self.caminho_midia_selecionada:
            self.popup(mensagem="Erro! Nenhum arquivo / ficheiro selecionado...", tempo_ms=2500, cor_fundo="darkred")
            return
        formato = self.opt_formato_midia.get()
        midia_selecionada = self.caminho_midia_selecionada
        nome_midia, extensao = os.path.splitext(midia_selecionada)
        midia_nova = nome_midia + '.' + formato.lower()
        self.popup(mensagem="Convertendo mídia, aguarde..!", tempo_ms=3000)
        def tarefa():
            try:
                converter_midias(midia_selecionada, midia_nova)
                self.after(0, lambda: self.popup(mensagem="Mídia convertida com sucesso!!", tempo_ms=3000))
            except Exception as e:
                self.after(0, lambda: self.popup(mensagem=f"Erro na conversão: {e}", tempo_ms=3000, cor_fundo="darkred"))
        threading.Thread(target=tarefa, daemon=True).start()    

    def setup_tab_midiaURL(self):
        self.entry_midiaURL = ctk.CTkEntry(
            self.tab_midiaURL, 
            placeholder_text="Insira o link da mídia",
            width=400
            )
        self.entry_midiaURL.pack(pady=15)

        self.btn_escolher_local = ctk.CTkButton(
            self.tab_midiaURL,
            text="Selecionar local de salvamento",
            command= self.escolher_local
        )


        self.switch_somente_audio = ctk.CTkSwitch(
            self.tab_midiaURL,
            text="Baixar apenas áudio (.mp3)"
        )
        self.switch_somente_audio.pack(pady=5)

        self.btn_escolher_local.pack(pady=10)
        self.lbl_escolher_local = ctk.CTkLabel(self.tab_midiaURL, text="Nenhum local selecionado")
        self.lbl_escolher_local.pack(pady=5)

        self.btn_baixar_midia = ctk.CTkButton(
        self.tab_midiaURL,
        text="Baixar mídia",
        command=self.baixar_midiaURL
        )
        
        self.btn_baixar_midia.pack(pady=5)

    def escolher_local(self):
        caminho = ctk.filedialog.askdirectory(
            title="Selecione o local de salvamento"
        )
        if caminho:
            self.caminho_salvamento = caminho
            self.lbl_escolher_local.configure(text=caminho)


    def baixar_midiaURL(self):
        if not self.caminho_salvamento:
            self.popup(mensagem="Erro! Nenhum local para salvamento selecionado...", tempo_ms=2500, cor_fundo="darkred")
            return
        caminho_saida = self.caminho_salvamento
        url = self.entry_midiaURL.get()
        somente_audio = True if self.switch_somente_audio.get() == 1 else False
        self.popup(mensagem="Baixando mídia, aguarde..!", tempo_ms=3000)
        def tarefa():
            try:
                baixar_midias(url, caminho_saida, so_audio=somente_audio)
                self.after(0, lambda: self.popup(mensagem="Mídia baixada com sucesso!!", tempo_ms=3000, cor_fundo="green"))
            except Exception as e:
                self.after(0, lambda: self.popup(mensagem=f"Erro ao baixar mídia: {e}", tempo_ms=3000, cor_fundo="darkred"))
        threading.Thread(target=tarefa, daemon=True).start()


    def setup_tab_imagemURL(self):
            self.entry_imagemURL = ctk.CTkEntry(
                self.tab_imagemURL, 
                placeholder_text="Insira o link da imagem",
                width=400
                )
            self.entry_imagemURL.pack(pady=10)
    
            self.btn_escolher_local = ctk.CTkButton(
                self.tab_imagemURL,
                text="Selecionar local de salvamento",
                command= self.escolher_local
            )
    
            self.btn_escolher_local.pack(pady=15)
            self.lbl_escolher_local = ctk.CTkLabel(self.tab_imagemURL, text="Nenhum local selecionado")
            self.lbl_escolher_local.pack(pady=5)

            self.opt_formato_imgURL = ctk.CTkOptionMenu(
                self.tab_imagemURL,
                values=["PNG", "JPG", "WEBP", "TIFF", "PDF", "BMP", "ICO", "GIF"]
            )
            self.opt_formato_imgURL.pack(pady=10)
    
            self.btn_baixar_imagem = ctk.CTkButton(
            self.tab_imagemURL,
            text="Baixar Imagem",
            command=self.baixar_imagemURL
            )
    
            self.btn_baixar_imagem.pack(pady=5)
    
    def escolher_local_img(self):
            caminho = ctk.filedialog.askdirectory(
                title="Selecione o local de salvamento"
            )
            if caminho:
                self.caminho_salvamento = caminho
                self.lbl_escolher_local.configure(text=caminho)
    
    
    def baixar_imagemURL(self):
            if not self.caminho_salvamento:
                self.popup(mensagem="Erro! Nenhum local para salvamento selecionado...", tempo_ms=2500, cor_fundo="darkred")
                return
            caminho_saida = self.caminho_salvamento
            url = self.entry_imagemURL.get()
            nome_arquivo_extensao = os.path.basename(urlparse(url).path)
            nome_arquivo, extensao_velha = os.path.splitext(nome_arquivo_extensao)
            if not nome_arquivo:
                nome_arquivo = "imagem_baixada"

            extensao = self.opt_formato_img.get()
    
            nome_arquivo = nome_arquivo+"."+extensao.lower()
            caminho_saida = caminho_saida+"/"+nome_arquivo
            
            self.popup(mensagem="Baixando imagem, aguarde..!", tempo_ms=3000)
            def tarefa():
                try:
                    baixar_imagem(url, caminho_saida)
                    self.after(0, lambda: self.popup(mensagem="Imagem baixada com sucesso!!", tempo_ms=3000, cor_fundo="green"))
                except Exception as e:
                    msg_erro = str(e)
                    self.after(0, lambda: self.popup(mensagem=f"Erro ao baixar imagem: {e}", tempo_ms=3000, cor_fundo="darkred"))
            threading.Thread(target=tarefa, daemon=True).start()
        


if __name__ == "__main__":
    app = App()
    app.mainloop()