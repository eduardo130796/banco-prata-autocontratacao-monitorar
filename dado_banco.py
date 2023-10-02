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

def dados_banco(navegador,banco,agencia,conta,tipo_conta,div):
    time.sleep(2)
    EC.presence_of_element_located((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[1]/div/div/input'))
    banco_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[1]/div/div/input')
    time.sleep(2)
    banco_element.send_keys(banco)
    time.sleep(2)
    banco_element.send_keys(Keys.ENTER)
    time.sleep(2)
    tipoconta_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[2]/div/div/select')
    if tipo_conta == '1':
            tipoconta_element.send_keys(Keys.ARROW_DOWN)
            tipoconta_element.send_keys(Keys.TAB)
    elif tipo_conta == '2':
            tipoconta_element.send_keys(Keys.ARROW_DOWN)
            tipoconta_element.send_keys(Keys.ARROW_DOWN)
            tipoconta_element.send_keys(Keys.TAB) 
    time.sleep(2)
    agencia_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[3]/div/input')
    agencia_element.send_keys(agencia)
    time.sleep(2)
    agencia_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[4]/div/input')
    agencia_element.send_keys(conta)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[2]/button[2]'))).click()
    time.sleep(10)