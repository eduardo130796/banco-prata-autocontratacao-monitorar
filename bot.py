import requests
import json
import math
from validar_cpf import *
from banco_prata_monitorar import*
from validar_data import *
from banco_prata import*
import threading
import keyboard
import signal
import sys

def get_total_pages(headers):
    params = {'page': '1'}
    response = requests.get('https://backend.botconversa.com.br/api/v1/webhook/subscribers/', params=params, headers=headers)
    response.raise_for_status()
    data_dict = json.loads(response.text)
    total = math.ceil(data_dict["count"] / len(data_dict["results"]))
    return total

def get_subscribers(page, headers):
    params = {'page': page}
    response = requests.get('https://backend.botconversa.com.br/api/v1/webhook/subscribers/', params=params, headers=headers)
    response.raise_for_status()
    return json.loads(response.text)

def process_subscriber(subscriber, page, total_pages):
    tags = subscriber['tags']
    #if page > total_pages - 2:
    if 'simulacao' in tags:
        nome = subscriber['full_name']
        telefone = subscriber['phone'][3:]
        cpf = subscriber['variables']['CPF']
        print(f'Nome: {nome}')
        print(f'Telefone: {telefone}')
        print(f'CPF: {cpf}')
        try:
            if validar_cpf(telefone, nome, cpf):
                pass
                banco_prata(nome, cpf, telefone, data_de_nascimento=None, tipo_documento=None, numero_documento=None, banco=None, agencia=None, conta=None, tipo_conta=None, etiqueta=None)
        except CPFFormatError as e:
            print(f"Erro de CPF: {e}")

    elif 'autocontratacao_prata' in tags:
        nome = subscriber['full_name']
        telefone = subscriber['phone'][3:]
        cpf = subscriber['variables']['CPF']
        data_de_nascimento = subscriber['variables']['Data_de_Nascimento']
        tipo_documento = subscriber['variables']['tipo_documento']
        numero_documento = subscriber['variables']['numero_documento']
        banco = subscriber['variables']['nome_banco']
        agencia = subscriber['variables']['Agencia']
        conta = subscriber['variables']['Conta']
        tipo_conta = subscriber['variables']['tipo_conta']
        etiqueta = 'autocontratacao'
        print(f'Nome: {nome}')
        print(f'Telefone: {telefone}')
        print(f'CPF: {cpf}')
        print(f'Data de nascimento: {data_de_nascimento}')
        print(f'Tipo de documento: {tipo_documento}')
        print(f'número do documento: {numero_documento}')
        print(f'Banco: {banco}')
        print(f'Agência: {agencia}')
        print(f'Conta: {conta}')
        print(f'Tipo de Conta: {tipo_conta}')
        data_valida(telefone,nome,data_de_nascimento)
        banco_prata(nome, cpf, telefone, data_de_nascimento, tipo_documento, numero_documento, banco, agencia, conta, tipo_conta, etiqueta)

def process_subscriber_monitorar(subscriber, page, total_pages):
    tags = subscriber['tags']
    if ('simulacao_prata' in tags) or ('cadastrado_prata' in tags) or ('Simulacao' in tags):
        nome = subscriber['full_name']
        telefone = subscriber['phone'][3:]
        cpf = subscriber['variables']['CPF']
        print(f'Nome: {nome}')
        print(f'Telefone: {telefone}')
        print(f'CPF: {cpf}')
        try:
            if validar_cpf(telefone, nome, cpf):
                pass
                banco_prata_monitoramento(nome, cpf, telefone)
        except CPFFormatError as e:
            print(f"Erro de CPF: {e}")

def parar():
# Defina o evento para sinalizar a interrupção das threads
    parar_event.set()

    # Aguarde as threads terminarem (se necessário)
    thread1.join()
    thread2.join()

    # Encerre o programa
    sys.exit()


parar_event = threading.Event()
def main():
    headers = {'accept': 'application/json', 'API-KEY': '6f9d2125-3e30-49e0-b469-698f2b784231'}
    try:
        while not parar_event.is_set():
            total_pages = get_total_pages(headers)

            for page in range(total_pages, 0,-1):                
                subscribers = get_subscribers(page, headers)
                print(f"Processando página {page}")
                if not subscribers.get('results'):
                    break

                for subscriber in subscribers['results']:
                    process_subscriber(subscriber, page, total_pages)


            print('Esperando para a próxima verificação...')
            
    except Exception as e:
        print(f"Erro em main: {e}")
        parar()


def main_monitorar():
    headers = {'accept': 'application/json', 'API-KEY': '6f9d2125-3e30-49e0-b469-698f2b784231'}
    try:
        while not parar_event.is_set():
            total_pages = get_total_pages(headers)
            items_per_iteration = 2

            for start_page in range(1, total_pages + 1, items_per_iteration):
                end_page = min(start_page + items_per_iteration - 1, total_pages)
                for _ in range(2):
                    for page in range(start_page, end_page + 1):
                        subscribers = get_subscribers(page, headers)
                        print(f"Processando página {page}")
                        if not subscribers.get('results'):
                            break

                        for subscriber in subscribers['results']:
                            process_subscriber_monitorar(subscriber, page, total_pages)

            print('Esperando para a próxima verificação...')
            
    except Exception as e:
        print(f"Erro em main: {e}")
        parar()


#if __name__ == "__main__":
#    main()

thread1 = threading.Thread(target=main)
thread2 = threading.Thread(target=main_monitorar)

# Inicie as threads
thread1.start()
thread2.start()
# Aguarde até que a tecla 'q' seja pressionada para encerrar as threads
#input("Pressione 'q' e Enter para encerrar as threads...")




