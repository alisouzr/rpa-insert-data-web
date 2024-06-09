from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import pyautogui
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho_arquivo = r'data\dados.xlsx'

dados = pd.read_excel(caminho_arquivo)

navegador.get("https://cadastroprodutos-devaprender.netlify.app/")
navegador.maximize_window()

# Percorrendo cada linha do DataFrame
for indice, linha in dados.iterrows():
    # Extraindo os valores de cada coluna
    produto = linha['Produto']
    fornecedor = linha['Fornecedor']
    categoria = linha['Categoria']
    valor_unitario = linha['Valor Unitário']
    notificar_venda = linha['Notificar A Cada Venda?']
 
    navegador.find_element('xpath', '//*[@id="campo1"]').send_keys(f'{produto}')
    navegador.find_element('xpath', '//*[@id="campo2"]').send_keys(f'{fornecedor}')
    navegador.find_element('xpath', '//*[@id="campo3"]').send_keys(f'{categoria}')
    navegador.find_element('xpath', '//*[@id="campo4"]').send_keys(f'{valor_unitario}')

    if str.upper(notificar_venda) == 'NÃO':
        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/form/div[2]/div[3]/div/div/label[2]').click()

    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/form/div[3]/button').click()

    time.sleep(2)
    pyautogui.press('enter')
