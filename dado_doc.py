import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
import random
from estado_ddd import *
from datetime import datetime, timedelta


#gera uma data aleatória para a data de expedição
def data_aleatoria():
        # Defina o intervalo de anos para escolher aleatoriamente
        ano_inicial = 2000
        ano_final = 2023

        # Escolha um ano aleatório entre ano_inicial e ano_final
        ano = random.randint(ano_inicial, ano_final)

        # Escolha um mês e um dia aleatórios
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)  # Você pode ajustar o limite superior com base no mês se desejar

        # Crie a data de expedição
        data_expedicao = datetime(ano, mes, dia)

        # Converta a data para uma string formatada
        data_expedicao_str = data_expedicao.strftime('%d%m%Y')
        return data_expedicao_str


def documento(navegador,tipo_documento,numero_documento,tel,div):
    ## parte documento
    EC.presence_of_element_located((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[1]/div/label'))
    tpdoc_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[1]/div/div/select')
    if tipo_documento == 'RG':
        tpdoc_element.send_keys(Keys.ARROW_DOWN)
        tpdoc_element.send_keys(Keys.TAB)
    else:
        tpdoc_element.send_keys(Keys.ARROW_DOWN)
        tpdoc_element.send_keys(Keys.ARROW_DOWN)
        tpdoc_element.send_keys(Keys.TAB)
    time.sleep(2)
    numdoc_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[2]/div/input')                                                                      
    numdoc_element.send_keys(numero_documento)
    time.sleep(2)
    data = data_aleatoria()
    dtexpedicao_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[3]/div/input')                                                                      
    dtexpedicao_element.send_keys(data)
    time.sleep(2)
    # Valor da opção que deseja selecionar
    # Use 'clicks_needed' no seu loop para simular os cliques necessários
    cliques_necessarios = DDD.obter_ddds_por_ddds(tel[0:2])
    select_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[4]/div/div/select')
    for _ in range(int(cliques_necessarios)):
            time.sleep(1)
            select_element.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    select_element.send_keys(Keys.TAB)
    time.sleep(1)
    estadocivil_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[5]/div/div[1]/select')
    estadocivil_element.send_keys(Keys.ARROW_DOWN)
    estadocivil_element.send_keys(Keys.TAB)
    time.sleep(2)
    numdoc_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[6]/div/input')                                                                      
    numdoc_element.send_keys('não informado')
    time.sleep(2)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[2]/button[2]'))).click()
    time.sleep(5)