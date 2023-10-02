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
from mensagem_bot import *


def link(navegador,div,tel,nome):
    EC.presence_of_element_located((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/table/tbody/tr[1]/td[1]'))
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/table/tbody/tr[1]/td[2]/span/label/input'))).click()
    time.sleep(1)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/table/tbody/tr[2]/td[2]/span/label/input'))).click()
    time.sleep(1)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/table/tbody/tr[3]/td[2]/span/label/input'))).click()
    time.sleep(1)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/table/tfoot/tr/td/span/label/input'))).click()
    time.sleep(1)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/span[2]/button'))).click()
    time.sleep(1)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/div/a[2]'))).click()
    time.sleep(1)
    elemento_link = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div/div/a[2]/input')
    # Obtenha o URL do link
    url_do_link = elemento_link.get_attribute('value')
    Whatsapp.link_assinatura(tel,nome,url_do_link)
    # Imprima o URL
    #print(url_do_link)
    
