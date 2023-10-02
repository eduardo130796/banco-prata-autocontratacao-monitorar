import phonenumbers
from phonenumbers import geocoder
import requests
from urllib.request import urlopen
import json

class EnderecoDDD:
    @staticmethod
    def estado_ddd(telefone):
        telefone_ajustado = phonenumbers.parse(telefone)
        local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
        
        local_ajustado = {
            'Federal District': 'Distrito Federal',
            'Espirito Santo': 'Espírito Santo',
            'Paraiba': 'Paraíba'
        }.get(local, local)
        return local_ajustado
    
    @staticmethod
    def uf_estado(local):
        url = "https://raw.githubusercontent.com/wgenial/br-cidades-estados-json/master/estados.json"
        response = requests.get(url)
        estados = {estado_data['estado']: (estado_data['id'], estado_data['estado']) for estado_data in response.json()['estados']}
        
        return estados.get(local)
    
    @staticmethod
    def cep_endereco(uf, local):
        while True:  # Loop infinito até encontrar um CEP com endereço válido
            url = f"https://raw.githubusercontent.com/wgenial/br-cidades-estados-json/master/cidades/{uf}.json"
            response = urlopen(url)
            data_json = json.loads(response.read()) 
            
            # Tentar cidades diferentes até encontrar um CEP válido com logradouro
            for cidade_data in data_json['cidades']:
                cidade = cidade_data['cidade']
                endereco = 'rua' if local == 'Pernambuco' else 'centro'
                link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'
                requisicao = requests.get(link)
                
                try:
                    dic_requisicao = requisicao.json()
                    if dic_requisicao and 'erro' not in dic_requisicao and dic_requisicao[0]['logradouro']:
                        ler_local = dic_requisicao[0]['localidade']
                        ler_uf = dic_requisicao[0]['uf']
                        cep = dic_requisicao[0]['cep']
                        endereco = dic_requisicao[0]['logradouro']
                        return cep, endereco, ler_local, ler_uf
                except json.JSONDecodeError:
                    pass  # Ignorar CEPs inválidos
    

#telefone = '+5562993526884'
# Obtenha o estado com base no DDD do telefone
#local = EnderecoDDD.estado_ddd(telefone)
# Obtenha a UF do estado
#uf, _ = EnderecoDDD.uf_estado(local)
# Obtenha o CEP e o endereço com base na UF, cidade e local
#cep, endereco, localidade, uf_cep = EnderecoDDD.cep_endereco(uf, local)