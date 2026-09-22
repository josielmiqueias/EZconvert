# EZconvert

O EZconvert foi uma ideia repentina de projeto que eu tive, ele é um conversor de imagens e mídias que pode converter entre as mais famosas das extensões, também é possível baixar mídias pela url diretamente da sua máquina, tudo roda localmente e não tem nenhuma telemetria nem mantém seus arquivos violando sua privacidade.

Tudo funciona a partir de um único executável (EZconvert.exe) que abre uma UI onde você pode fazer suas conversões/downloads.

## O que o programa faz

* Conversão de Imagens: Suporta os formatos mais comuns (PNG, JPG, WEBP). Também pode converter de .png para .ico, que preserva a transparência e gera .ico de alta resolução (até 256x256).
* Conversão de Áudio e Vídeo: Integração com o FFmpeg para converter formatos como MP4, MP3, AVI e MKV em segundo plano.
* Download de Mídias: Tem como baixar vídeos ou extrair áudios (MP3 a 192 kbps) diretamente de URLs através do yt-dlp.
* Fácil para usar: O FFmpeg e todas as dependências estão baixadas no .exe. É só baixar o .zip no releases e usar.

## Como usar (Para quem for usar)

Se você quer apenas utilizar o programa, não precisa mexer em código nem instalar dependências, é só seguir esses 3 passos:

1. Vá à seção "Releases" no lado direito da página desse repositório.
2. Baixe o arquivo EZconvert.zip e extrai.
3. Dê um duplo clique no arquivo EZconvert.exe para abrir.

Nota sobre alertas de segurança (Windows / Navegadores):
Por se tratar de um projeto de código aberto, independente e gratuito, o executável não possui uma assinatura digital paga (Certificado Code Signing). Devido a isto, navegadores como o Chrome ou Edge e o filtro Windows SmartScreen podem mostrar um aviso ao tentar baixar ou abrir o programa pela primeira vez. 

O arquivo é totalmente seguro e o código-fonte está disponível nesta página para qualquer pessoa auditar. Caso você se deparar com esse aviso, basta clicar nos três pontinhos e selecionar a opção "Manter mesmo assim" no teu navegador ou clicar em "Mais informações" e depois "Executar mesmo assim" no Windows.

## Como executar a partir do código-fonte (Para programadores)

Se quiser adaptar o projeto, contribuir ou simplesmente correr a aplicação localmente:

1. Clone o repositório:
   git clone https://github.com/josielmiqueias/EZconvert.git
   cd EZconvert

2. Crie e ative o seu ambiente virtual:
   python -m venv venv
   .\venv\Scripts\Activate.ps1

3. Instale as dependências necessárias:
   pip install -r requirements.txt

4. Adicione o FFmpeg:
   Baixe o binário do ffmpeg.exe para Windows e coloque na pasta principal do projeto, no mesmo local onde se encontra o main.py.

5. Para executar simplesmente use:
   python main.py

## Compilar o executável

Caso mude o código e queiras criar um novo arquivo .exe independente com o PyInstaller, use o comando abaixo na pasta principal do projeto:

pyinstaller --noconsole --onefile --icon="web/assets/icons/iconv3v.ico" --add-data "web;web" --add-binary "ffmpeg.exe;." main.py

O arquivo final compilado vai aparecer na pasta "dist".

## Stack e Tecnologias

* Python (Backend geral)
* pywebview (front-end (interface do usuario) usando HTML, CSS e JS)
* Pillow (Manipulação e redimensionamento de imagens)
* yt-dlp (Motor de extração e download de mídias online)
* FFmpeg (Processamento de áudio e vídeo)
* PyInstaller (Empacotamento do programa)


Se te ajudou de qualquer forma não se esqueça de deixar a estrelinha! :)
