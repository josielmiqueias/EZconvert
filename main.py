from conversores import converter_imagem, converter_midias, baixar_midias, baixar_imagem

print("Seja bem vindo ao....")
print(r""" ________  ________                                                _    
|_   __  ||  __   _|                                              / |_  
  | |_ \_||_/  / /   .---.   .--.   _ .--.  _   __  .---.  _ .--.`| |-' 
  |  _| _    .'.' _ / /'`\]/ .'`\ \[ `.-. |[ \ [  ]/ /__\\[ `/'`\]| |   
 _| |__/ | _/ /__/ || \__. | \__. | | | | | \ \/ / | \__., | |    | |,  
|________||________|'.___.' '.__.' [___||__] \__/   '.__.'[___]   \__/  
                                                                        
                                                                        """)
print("""Escolha uma opção para selecionar o que você deseja converter:
    [1] 🖼️  Conversão de imagens    
    [2] 🎥 Conversão de mídias (Vídeos, áudios, etc.)
    [3] 📥  Baixar áudio da web (Link)
    [4] 📥  Baixar vídeo da web (Link)
    [5] 📥  Baixar imagem da web (Link)\n""")

while True:
    try:
        escolha_menu = int(input("Escolha a sua opção [1], [2], [3], [4] ou [5]...\n"))
        if escolha_menu in (1,2,3,4,5):
            break
        print("Digite apenas alguma das opções fornecidas")
    except ValueError:
        print("Digite apenas números inteiros!!!")
if escolha_menu == 1:
    print("Vamos converter imagens então..!")
    caminho_origem = input("Digite o caminho de origem da foto que irá ser usada para a conversão:\n")
    caminho_destino = input("Agora digite o caminho de onde a imagem convertida irá ficar:\n")
    converter_imagem(caminho_origem, caminho_destino)
    print("O arquivo foi convertido com êxito...")
elif escolha_menu == 2:
    print("Vamos converter mídias então..!")
    caminho_origem = input("Digite o caminho da mídia que irá ser convertida:\n")
    caminho_destino = input("Agora digite o caminho onde a mídia convertida irá ficar:\n")
    print("Convertendo a mídia desejada, aguarde um momento!")
    converter_midias(caminho_origem, caminho_destino)
    print("Conversão concluída com sucesso! Cheque o local onde você escolheu para ficar a conversão!")
elif escolha_menu == 3:
    print("Vamos baixar áudios da web utilizando a URL...!")
    url = input("Cole a URL do áudio:\n")
    pasta = input("Cole abaixo o caminho onde será salvo o áudio:\n")
    print("Baixando áudio...")
    baixar_midias(url, caminho_saida=pasta, so_audio=True)
    print("Áudio baixado com êxito..!")
elif escolha_menu == 4:
    print("Vamos baixar vídeos da web utilizando a URL..!")
    url = input("Cole a URL do vídeo:\n")
    pasta = input("Cole abaixo o caminho onde será salvo o vídeo:\n")
    print("Baixando vídeo. . .")
    baixar_midias(url, caminho_saida=pasta, so_audio=False)
    print("Vídeo baixado com sucesso!!")
elif escolha_menu == 5:
    print("Ótimo, vamos baixar imagens da web utilizando a URL..!")
    url = input("Cole a URL da imagem:\n")
    pasta = input("Cole abaixo o caminho onde será salvo a imagem:\n")
    print("Baixando imagem. . .")
    baixar_imagem(url, caminho_saida=pasta)
    print("Imagem baixada com sucesso!!")

