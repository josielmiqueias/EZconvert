from conversores import baixar_imagem, baixar_midias, converter_imagem, converter_midias
import sleep

while True:
    try:
            print("""[0;97m ▄▀▀▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀█[0;37m [0;97;47m▓[0;97m▀▀▀▀▀▀▀[0;37m▀[0;97m▀▀█[0;37m [0;97m ▄▀▀▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀█[0;37m [0;97m ▄▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀▀▄ [0;37m [0;97m█▀▀[0;37m▀[0;97m▀▀▀▀▀▀▄ [0;37m [0;97m█▀▀[0;37m▀[0;97m▀█ ▓▀▀▀█[0;37m [0;97m ▄▀▀▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀█[0;37m [0;97m█▀▀[0;37m▀[0;97m▀▀▀▀▀▀▄ [0;37m [0;97m█▀▀▀▀▀▀[0;37m▀[0;97m▀[0;37m▀[0;97m▀█[0m
[0;97m█·   ▄▄▄▄▄[0;37m▄█ [0;97;47m▒[0;97m ∙ ▄▄▄    [0;97;47m▀[0;37m [0;97m█·   ▄▄▄▄▄[0;37m▄█ [0;97;47m▀[0;97m    ▄▄ .  █[0;37m [0;97;47m▀[0;97m    ▄▄    █[0;37m [0;97;47m▀[0;97m    ▓ ▒.  █[0;37m [0;97m█·   ▄▄▄▄▄[0;37m▄█ [0;97;47m▀[0;97m    ▄▄  ∙ █[0;37m [0;97m█▄▄▄·   ▄▄[0;37m▄█[0m
[0;97;47m▓[0;97m  . [0;97;47m▓[0;97m▄▄▄▄▄▄[0;37m ▀▀▀[0;90m▀[0;97m▀ [0;97;47m▓[0;97m    [0;97;47m▓[0;37m [0;97;47m▓[0;97m  . [0;97;47m▓[0;97m      [0;37m [0;97;47m▓[0;97m    [0;97;47m▓[0;97m ▌   [0;97;47m▓[0;37m [0;97;47m▓[0;97m    [0;97;47m▓[0;97m ▌   [0;97;47m▓[0;37m [0;97;47m▓[0;97m    [0;97;47m▓[0;97m ▒   [0;97;47m▓[0;37m [0;97;47m▓[0;97m  . [0;97;47m▓[0;97m▄▄▄▄▄▄[0;37m [0;97;47m▓[0;97m    [0;97;47m▓[0;97m▄▌   [0;97;47m▓[0;37m [0;97m   [0;97;47m▓[0;97m  . [0;97;47m▓[0;97m   [0m
[0;97;47m▒[0;97m ∙  [0;37m▄▄▄▄▄▄[0;97;47m▒[0;37m [0;97;47m▒[0;97m▀▀▀▀▀[0;90m▀[0;97m [0;37m▄▄▄[0;97;47m░[0;37m [0;97;47m▒[0;97m ∙  [0;97;47m▒[0;97m      [0;37m [0;97;47m▒[0;97m  · [0;97;47m▒[0;97m [0;97;47m▓[0;97m   [0;97;47m▒[0;37m [0;97;47m▒[0;97m    [0;97;47m▒[0;97m [0;97;47m▒[0;97m · [0;97;47m▒[0;37m [0;97;47m▒[0;97m  · [0;97;47m▒[0;97m [0;97;47m▓[0;97m   [0;97;47m▒[0;37m [0;97;47m▒[0;97m ∙  [0;37m▄▄▄▄▄▄[0;97;47m▒[0;37m [0;97;47m▒[0;97m   ·[0;37m▄▄▄[0;97m  [0;37m▀▄ [0;97m   [0;97;47m▒[0;97m ∙  [0;97;47m▒[0;97m   [0m
[0;97;47m░[0;97m    [0;97;47m░[0;37m▄▄▄▄▄▄ [0;97;47m░[0;97m.  ▒  ▄▄▄▄▄[0;37m [0;97;47m░[0;97m    [0;97;47m░[0;37m▄▄▄▄▄▄ [0;97;47m░[0;97m    [0;97;47m░[0;37m▄[0;97;47m░[0;90m·[0;97m. [0;97;47m░[0;37m [0;97;47m░[0;97m   ∙[0;97;47m░[0;97m [0;97;47m░[0;97m   [0;97;47m░[0;37m [0;97;47m░[0;97m    [0;97;47m░[0;37m▄[0;97;47m░[0;90m·[0;97m. [0;97;47m░[0;37m [0;97;47m░[0;97m    [0;97;47m░[0;37m▄▄▄▄▄▄ [0;97;47m░[0;97m .  [0;97;47m░[0;97m [0;97;47m░[0;97m  .[0;97;47m░[0;37m [0;97m   [0;97;47m░[0;97m    [0;97;47m░[0;97m   [0m
[0;37m█[0;97m    .    ·[0;37m█ █[0;97m  ∙▀▀▀▀   [0;97;47m▓[0;37m █[0;97m    .    ·[0;37m█ █[0;97m   .      [0;37m█ █[0;97m ∙  [0;37m█[0;97m [0;37m█[0;97m   [0;37m█ █[0;97m   .      [0;37m█ █[0;97m    .    ·[0;37m█ █[0;97m    [0;37m█[0;97m [0;37m█[0;97m∙  [0;37m█ [0;97m   [0;37m█[0;97m    [0;37m█[0;97m   [0m
[0;37m█▄▄▄▄▄▄▄▄▄▄█ █▄▄▄▄▄▄▄▄▄▄[0;97;47m░[0;37m █▄▄▄▄▄▄▄▄▄▄█ [0;97m [0;37m▀▄▄▄▄▄▄▄▄▀[0;97m [0;37m █▄▄▄▄█[0;97m [0;37m█▄▄▄█ [0;97m [0;37m▀▄▄▄▄▄▄▄▄▀[0;97m [0;37m █▄▄▄▄▄▄▄▄▄▄█ █▄▄▄▄█[0;97m [0;37m█▄▄▄█ [0;97m   [0;37m█▄▄▄▄█[0;97m   [0m
        """)
            print("Bem-vindo à versão de terminal do EZconvert!\n")
            print("""Selecione a opção que você deseja:
            (1) - 🖼️   Converter Imagens
            (2) - 🎞️   Converter Mídias
            (3) - 📥   Baixar Mídias
            (4) - 📥   Baixar Imagens""")
            escolhamenu = 0
            while escolhamenu not in (1, 2, 3, 4):
                try:
                    escolhamenu = int(input())
                except(ValueError):
                    print("Apenas digite números válidos, não digite letras ou caracteres.")
            if escolhamenu ==1:
                caminhoentradaimg = input(r"Digite o caminho da imagem. Exemplo: 'C:\Users\seu_usuario\pasta\foto.extensão'." "\n")
                caminhosaidaimg = input("Digite o caminho onde a imagem imagem será salva.\n"r"Exemplo: 'C:\Users\seu_usuario\pasta\fotoconvertida.extensãodesejada'." "\n")
                while True:
                    try:
                        converter_imagem(caminho_entrada=caminhoentradaimg, caminho_saida=caminhosaidaimg)
                    except(OSError):
                        print("Erro! Tente digitar os caminhos sem aspas apenas o texto comum:")
                        caminhoentradaimg = input("Digite o caminho da imagem.\n")
                        caminhosaidaimg = input("Digite o caminho onde a imagem imagem será salva.\n")
                        converter_imagem(caminho_entrada=caminhoentradaimg, caminho_saida=caminhosaidaimg)
            elif escolhamenu ==2:
                caminhoentradamidia = input(r"Digite o caminho da mídia. Exemplo: 'C:\Users\Usuario\pasta\midia.extensão'." "\n")
                caminhosaidamidia = input("Digite o caminho onde a mídia será salva.\n"r"Exemplo: 'C:\Users\Usuario\pasta\midia.extensãodesejada'." "\n")
                while True:
                    try:
                        converter_midias(caminho_entrada=caminhoentradamidia, caminho_saida=caminhosaidamidia)
                    except(OSError):
                        print("Erro! Tente digitar os caminhos sem aspas apenas o texto comum:")
                        caminhoentradamidia = input("Digite o caminho da mídia.\n")
                        caminhosaidamidia = input("Digite o caminho onde a mídia será salva.\n")
                        converter_midias(caminho_entrada=caminhoentradamidia, caminho_saida=caminhosaidamidia)

            elif escolhamenu ==3:
                urlmidia = input("Digite a url da mídia para ser baixada:\n")
                caminhomidiabaixada = input("Digite o caminho onde a mídia será salva.\n"r"Exemplo: 'C:\Users\Usuario\pasta\midia.extensãodesejada'." "\n")
                print("Se você quiser a mídia só com áudio então digite 1, se quiser com o áudio e vídeo digite 0:\n")
                soaudio = int(input())
                while soaudio not in (1, 0):
                    try:
                        soaudio = int(input("Digite apenas opções válidas (1 ou 0)\n"))
                    except(ValueError):
                        print("Apenas digite números, evite digitar outras coisas sem ser alguma das opções válidas.")
                        soaudio = int(input())
                if soaudio == 1:
                    self.so_audio=True
                else:
                    self.so_audio=False
                baixar_midias(url=urlmidia, caminhomidiabaixada=caminhomidiabaixada, so_audio=self.so_audio)
            else:
                urlimagem = input("Digite a url da imagem para ser baixada:\n")
                caminhoimagembaixada = input("Digite o caminho onde a imagem será salva.\n"r"Exemplo: 'C:\Users\Usuario\pasta\imagem.extensãodesejada'." "\n")
                baixar_imagem(url=urlimagem, pasta_destino=caminhoimagembaixada)

            print("\nObrigado por usar o programa! Se te ajudou não se esqueça de deixar uma estrelinha!\n")
            print("Deseja fazer uma nova conversão? Digite 1, caso queira sair, digite 0.")
            repetir = int(input())
            while repetir not in (1, 0):
                try:
                    print("Erro! Apenas digite opções válidas.")
                    repetir = int(input())
                except(ValueError):
                    print("Erro, apenas digite números (1 ou 0)")
                    repetir = int(input())
            if repetir ==0:
                print("Encerrando, até a próxima!")
                break
    except(KeyboardInterrupt):
        print("Fechando o programa! (Ação feita pelo usuário)...")
        break