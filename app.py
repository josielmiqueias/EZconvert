import customtkinter as ctk
import os
from conversores import converter_imagem, converter_midias, baixar_imagem, baixar_midias

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EZconvert - Conversor de arquivos")
        self.geometry("650x450")
        self.resizable(False, False)
        self.label_titulo = ctk.CTkLabel(self, text="EZconvert", font=("Arial", 24, "bold"))
        self.label_titulo.pack(pady=15)
        self.tabview = ctk.CTkTabview(self, width=600, height=350)
        self.tabview.pack(pady=10)
        self.tab_imagem = self.tabview.add("Imagens")
        self.tab_midia = self.tabview.add("Mídias")
        self.tab_url_midia = self.tabview.add("URL Mídias")
        self.tab_url_imagem = self.tabview.add("URL Imagens")
        self.caminho_img_selecionada = None

        self.setup_tab_imagem()
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
                ("Arquivos de Imagem", ("*.png", "*.jpg", "*.jpeg", "*.webp", "*.tiff", "*.pdf", "*.bmp", "*.ico", "*.gif")),
                ("Todos os arquivos", "*.*")
                ]
        )
        if caminho:
            self.caminho_img_selecionada = caminho
            self.lbl_arquivo_imagem.configure(text=caminho)
    def executar_conversao_img(self):
        if not self.caminho_img_selecionada:
            print("Erro! Nenhum arquivo/ficheiro selecionado. . .")
            return
        formato = self.opt_formato_img.get()
        imagem_selecionada = self.caminho_img_selecionada
        nome_imagem, extensao = os.path.splitext(imagem_selecionada)
        imagem_nova = nome_imagem + '.' + formato.lower()
        print("Convertendo imagem, aguarde..!")
        converter_imagem(imagem_selecionada, imagem_nova)
        print("Imagem convertida com sucesso!!")
        



if __name__ == "__main__":
    app = App()
    app.mainloop()