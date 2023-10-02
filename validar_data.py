from datetime import datetime
from mensagem_bot import Whatsapp

def data_valida(tel,nome_1,datanascimento):
    data_numerico = ''.join(filter(str.isdigit, datanascimento))
    try:
        data_1 = data_numerico
        if len(data_1) == 8:
            dia = int(data_numerico[0:2])
            mes = int(data_numerico[2:4])
            ano = int(data_numerico[4:])
            
            if 1900 <= ano <= datetime.now().year:
                datetime.strptime(data_1, '%d%m%Y')
                data_nascimento = f'{ano}-{mes:02d}-{dia:02d}'
                print('Data de nascimento correta')
                return data_nascimento
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print('Data de nascimento errada')
        aviso = 'erro_dn'
        Whatsapp.whats_erro_dados(tel, nome_1, datanascimento, aviso)
        return True