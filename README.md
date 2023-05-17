# whatsapp-auto-message-sender 

Projeto de automação do WhatsApp usando Python e Selenium


Automação de envio de mensagens no WhatsApp Web
Esse é um projeto de automação de envio de mensagens no WhatsApp Web, desenvolvido em Python utilizando a biblioteca Selenium. Com ele, é possível enviar mensagens personalizadas para vários contatos em sequência, de forma automatizada.

## Pré-requisitos
Para rodar o projeto, é necessário ter os seguintes softwares instalados:

-> Python 3.x

-> Chrome Web Browser

-> ChromeDriver

### Para instalar as dependências do projeto, execute o seguinte comando:


pip install -r requirements.txt

### Como utilizar
1. Abra o arquivo Envios.xlsx e preencha as informações de acordo com o modelo fornecido.
2. Execute o script enviar_mensagens.py usando o seguinte comando:
python enviar_mensagens.py

3. Aguarde enquanto o script abre o WhatsApp Web e faz o login automaticamente.
4. O script percorrerá a tabela de envios e enviará as mensagens para os contatos correspondentes.
5. Opcionalmente, é possível anexar um arquivo de imagem ou vídeo a cada mensagem. Para isso, basta preencher o nome do arquivo na coluna correspondente da tabela e colocar o arquivo na pasta arquivos.

## Observações
Certifique-se de ter uma boa conexão com a internet enquanto o script estiver em execução.
O WhatsApp Web pode exibir uma mensagem de segurança pedindo para escanear um código QR. Caso isso aconteça, faça a leitura do código QR manualmente e aguarde até que a página seja carregada antes de executar o script.


É importante ter cuidado ao enviar mensagens automatizadas para muitos contatos em sequência, pois isso pode ser considerado spam e violar as políticas do WhatsApp. É recomendável usar o script com moderação e apenas para fins legítimos, como enviar mensagens de felicitações ou avisos importantes para um grupo restrito de contatos.
