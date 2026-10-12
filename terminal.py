from conversores import baixar_imagem, baixar_midias, converter_imagem, converter_midias, iniciar_animacao, parar_animacao
import time
import os
import subprocess
import yt_dlp
import requests

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
                t = iniciar_animacao()
                erro = False
                try:
                    converter_imagem(caminho_entrada=caminhoentradaimg, caminho_saida=caminhosaidaimg)
                    time.sleep(2)
                    erro = False
                except(OSError):
                    parar_animacao()
                    print("\nErro! Tente digitar os caminhos sem aspas apenas o texto comum:")
                        
                    caminhoentradaimg = input("Digite o caminho da imagem.\n")
                    caminhosaidaimg = input("Digite o caminho onde a imagem imagem será salva.\n")
                        
                    t = iniciar_animacao()
                    try:
                        converter_imagem(caminho_entrada=caminhoentradaimg, caminho_saida=caminhosaidaimg)
                    except Exception as e:
                        parar_animacao()
                        print(f"Erro, o sistema deu erro novamente (Erro de {e}.)")
                        erro = True
                except Exception as e:
                    parar_animacao()
                    print(f"Erro! O programa deu erro por causa de(o) {e}")
                    time.sleep(1.67)
                    erro = True
                finally:
                    parar_animacao()
                if not erro:
                    print("\nImagem Convertida com sucesso!\n")
                else:
                    print("\nErro ao converter!")
                    
            
            elif escolhamenu ==2:
                caminhoentradamidia = input(r"Digite o caminho da mídia. Exemplo: 'C:\Users\Usuario\pasta\midia.extensão'." "\n")
                caminhosaidamidia = input("Digite o caminho onde a mídia será salva.\n"r"Exemplo: 'C:\Users\Usuario\pasta\midia.extensãodesejada'." "\n")
                t = iniciar_animacao()
                try:
                    converter_midias(caminho_entrada=caminhoentradamidia, caminho_saida=caminhosaidamidia)
                except subprocess.CalledProcessError:
                    parar_animacao()
                    print("Erro! Tente digitar os caminhos sem aspas apenas o texto comum:")
                    
                    caminhoentradamidia = input("Digite o caminho da mídia.\n")
                    caminhosaidamidia = input("Digite o caminho onde a mídia será salva.\n")
                    t = iniciar_animacao()
                    try:
                        converter_midias(caminho_entrada=caminhoentradamidia, caminho_saida=caminhosaidamidia)
                    except Exception as e:
                        parar_animacao()
                        print(f"O sistema falhou novamente por causa de um erro de {e}")
                        time.sleep(2.33)
                except Exception as e:
                    parar_animacao()
                    print(f"Erro! ({e}.)")
                finally:
                    parar_animacao()
                    print(
                          "A conversão foi concluída com sucesso"
                          f" no diretório ({caminhoentradamidia})."
                        )

            elif escolhamenu ==3:
                urlmidia = input("Digite a url da mídia para ser baixada:\n")
                caminhomidiabaixada = input("Digite o caminho onde a mídia será salva.\n"r"Exemplo: 'C:\Users\Usuario\pasta\nomedamidia'." "\n")
                print("Se você quiser a mídia só com áudio então digite 1, se quiser com o áudio e vídeo digite 0:\n")
                soaudio = None
                while soaudio not in (1, 0):
                    try:
                        soaudio = int(input("Digite apenas opções válidas (1 ou 0)\n"))
                    except(ValueError):
                        print("Apenas digite números, evite digitar outras coisas sem ser alguma das opções válidas.")
                if soaudio == 1:
                    soaudio=True
                else:
                    soaudio=False
                try:
                    baixar_midias(url=urlmidia, caminho_saida=caminhomidiabaixada, so_audio=soaudio)
                except yt_dlp.utils.DownloadError as e:
                    print(f"Erro, não foi possível baixar a mídia por causa de(o) {e}")
                    tt_nv=input("Deseja tentar novamente? (s/n):   ")
                    if tt_nv.lower() == "s":
                        print("Deseja colocar um novo caminho? (s/n):   ")
                        nv_caminho = input()
                        if nv_caminho.lower() == "s":
                            urlmidia = input("Digite a nova URL: ").strip()
                            print("Digite o caminho onde a mídia será salva: ")
                            caminhomidiabaixada = input().strip()
                            deu_erro=False
                            erro = None
                            try:
                                baixar_midias(url=urlmidia, caminho_saida=caminhomidiabaixada, so_audio=soaudio)
                                deu_erro = False
                            except Exception as e:
                                erro = e
                                deu_erro = True
                            finally:
                                if deu_erro:
                                    print(f"O programa falhou novamente! {erro}")
                                    time.sleep(5)
                                if not deu_erro:
                                    print("O sistema baixou a mídia com sucesso")
                        else:
                            erro = None
                            deu_erro = False
                            try:
                                baixar_midias(url=urlmidia, caminho_saida=caminhomidiabaixada, so_audio=soaudio)
                                deu_erro = False
                            except Exception as e:
                                erro = e
                                deu_erro = True
                            finally:
                                if deu_erro:
                                    print(f"O programa falhou novamente! {erro}")
                                    time.sleep(5)
                                if not deu_erro:
                                    print("O sistema baixou a mídia com sucesso")
                        
            else:
                urlimagem = input("Digite a url da imagem para ser baixada:\n")
                caminhoimagembaixada = input("Digite o caminho onde a imagem será salva.\n"r"Exemplo: 'C:\Users\Usuario\pasta\imagem.extensãodesejada'." "\n")
                try:
                    baixar_imagem(url=urlimagem, pasta_destino=caminhoimagembaixada)
                except requests.RequestException as e:
                    print(f"Erro ao baixar a imagem! ({e})")
                    print("Deseja tentar novamente? (s/n):   ")
                    tt_nv=input()
                    if tt_nv.lower() == "s":
                        print("Deseja colocar um novo caminho? (s/n):   ")
                        nv_caminho = input()
                        if nv_caminho.lower() == "s":
                            urlimagem = input("Digite a nova URL: ").strip()
                            print("Digite o caminho onde a imagem será salva: ")
                            caminhoimagembaixada = input().strip()
                            deu_erro=False
                            erro = None
                            try:
                                baixar_imagem(url=urlimagem, pasta_destino=caminhoimagembaixada)
                                deu_erro = False
                            except Exception as e:
                                erro = e
                                deu_erro = True
                            finally:
                                if deu_erro:
                                    print(f"O programa falhou novamente! {erro}")
                                    time.sleep(5)
                                if not deu_erro:
                                    print("O sistema baixou a imagem com sucesso")
                        else:
                            erro = None
                            deu_erro = False
                            try:
                                baixar_imagem(url=urlimagem, pasta_destino=caminhoimagembaixada)
                                deu_erro = False
                            except Exception as e:
                                erro = e
                                deu_erro = True
                            finally:
                                if deu_erro:
                                    print(f"O programa falhou novamente! {erro}")
                                    time.sleep(5)
                                if not deu_erro:
                                    print("O sistema baixou a imagem com sucesso")

            # pá ficar bunitin kkkkk
            time.sleep(2.67)
            os.system('cls' if os.name == 'nt' else 'clear')

            print("Obrigado por usar o programa! Se te ajudou não se esqueça de deixar uma estrelinha!\n")
            print("Deseja fazer uma nova conversão? Digite 1, caso queira sair, digite 0.")
            repetir = None
            while repetir not in (1, 0):
                try:
                    repetir = int(input())
                    while repetir not in (1, 0):
                        print("Digite apenas uma das opções válidas (0 para sair ou 1 para continuar)")
                        repetir = int(input())
                except(ValueError):
                    print("Erro, apenas digite números (1 ou 0)")
                except Exception as e:
                    print(f"O sistema falhou, (erro: {e}.)")
            if repetir ==0:
                print("Encerrando, até a próxima!")
                break
    except(KeyboardInterrupt):
        print("Fechando o programa! (Ação feita pelo usuário)...")
        break