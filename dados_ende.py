from endereco_cep import *
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



def ajustar_telefone(telefone):
    ddd = telefone[0:5]
    numero = telefone[5:]
    return f'{ddd}9{numero}'

def endereco(navegador,tel,div):
    telefone = '+55'+ tel
    ddd = telefone[3:5]
    if int(ddd) > 28:
        telefone = ajustar_telefone(telefone)
    local = EnderecoDDD.estado_ddd(telefone)
    # Obtenha a UF do estado
    uf, _ = EnderecoDDD.uf_estado(local)
    # Obtenha o CEP e o endereço com base na UF, cidade e local
    cep, endereco, localidade, uf_cep = EnderecoDDD.cep_endereco(uf, local)
    time.sleep(2)
    cep_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[1]/div/div/input')                                                                      
    cep_element.send_keys(cep)
    time.sleep(2)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[1]/div/button'))).click()
    time.sleep(7)
    numero_aleatorio = random.randint(1, 100)
    numero_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[3]/div/input')                                                                      
    numero_element.send_keys(numero_aleatorio)
    time.sleep(2)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[2]/button[2]'))).click()
    time.sleep(5)
    