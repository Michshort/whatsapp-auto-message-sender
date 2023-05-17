from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import urllib
import time
import pandas as pd
import os

# Configura o driver do Chrome
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Abre o WhatsApp Web e faz o login
navegador.get('https://web.whatsapp.com')
while len(navegador.find_elements(By.ID, 'pane-side')) < 1:
    time.sleep(1)

# Carrega a tabela de envios
tabela = pd.read_excel("Envios.xlsx")

# Percorre a tabela e envia as mensagens
for linha in tabela.index:
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]

    texto = mensagem.replace("fulano", nome)
    texto = urllib.parse.quote(texto)
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
    
    # Navega até o link da mensagem e envia
    navegador.get(link)
    while len(navegador.find_elements(By.ID, 'pane-side')) < 1:
        time.sleep(1)
    time.sleep(2)
    
    #anexar imagem
    if arquivo !='N':
        caminho_completo = os.path.abspath(f'arquivos/{arquivo}')
        #clica no clips
        clip = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
        clip.click()
        time.sleep(1)
        #clica no botão de imagem\video
        attach = navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')
        attach.send_keys(caminho_completo)
        time.sleep(1)
        #clica no botão enviar
        send = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')
        send.click()
        time.sleep(2)
        
    #envia a mensagem
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')\
        .click()
    time.sleep(2)
