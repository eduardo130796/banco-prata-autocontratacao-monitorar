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
#verificar se o nome é masculino ou feminino
def get_gender_by_name(name):
    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    data = response.json()
    
    if data.get("gender"):
        return data["gender"]
    else:
        return "Desconhecido"

def dados_pessoais(navegador,nome,cpf,tel,data_de_nascimento,etiqueta): 
    time.sleep(2)
    if etiqueta == 'cadastro':
            div = 3
            print('cadastro')
            WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/button'))).click()
    else:
            div = 2
            print('lista')
            WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div/table/tbody/tr[{etiqueta+1}]/td/div/button/span'))).click()
                    
    time.sleep(5)       
    nome_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[1]/div/input')
    nome_element.send_keys(nome)
    time.sleep(2)
    telefone_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[3]/div/input')
    telefone_element.send_keys(tel)
    time.sleep(2)
    dnascimento_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/span[4]/div/input')                                                                      
    dnascimento_element.send_keys(data_de_nascimento)
    time.sleep(2)
    gender = get_gender_by_name(nome)
    genero_element = navegador.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[1]/div/span/div/div/select')
    if gender == 'female':
            genero_element.send_keys(Keys.ARROW_DOWN)
            genero_element.send_keys(Keys.TAB)
    elif gender == 'male':
            genero_element.send_keys(Keys.ARROW_DOWN)
            genero_element.send_keys(Keys.ARROW_DOWN)
            genero_element.send_keys(Keys.TAB)
    else: 
            genero_element.send_keys(Keys.ARROW_DOWN)
            genero_element.send_keys(Keys.TAB)
    time.sleep(5)
    WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="content"]/div[2]/div/div[{div}]/div[2]/div/span/form/div[2]/button[2]'))).click()
    time.sleep(5)
    return div
