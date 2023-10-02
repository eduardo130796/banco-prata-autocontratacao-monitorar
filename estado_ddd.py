class DDD:
    def obter_ddds_e_cliques_por_estado():
        # Dicionário que associa o estado à lista de DDDs e quantidade de cliques
        estados_e_ddds = {
            "Acre": (["68"], 1),
            "Alagoas": (["82"], 2),
            "Amapá": (["96"], 3),
            "Amazonas": (["92", "97"], 4),
            "Bahia": (["71", "73", "74", "75", "77"], 5),
            "Ceará": (["85", "88"], 6),
            "Distrito Federal": (["61"], 7),
            "Espírito Santo": (["27", "28"], 8),
            "Goiás": (["62", "64"], 9),
            "Maranhão": (["98", "99"], 10),
            "Mato Grosso": (["65", "66"], 11),
            "Mato Grosso do Sul": (["67"], 12),
            "Minas Gerais": (["31", "32", "33", "34", "35", "37", "38"], 13),
            "Pará": (["91", "93", "94"], 14),
            "Paraíba": (["83"], 15),
            "Paraná": (["41", "42", "43", "44", "45", "46"], 16),
            "Pernambuco": (["81", "87"], 17),
            "Piauí": (["86", "89"], 18),
            "Rio de Janeiro": (["21", "22", "24"], 19),
            "Rio Grande do Norte": (["84"], 20),
            "Rio Grande do Sul": (["51", "53", "54", "55"], 21),
            "Rondônia": (["69"], 22),
            "Roraima": (["95"], 23),
            "Santa Catarina": (["47", "48", "49"], 24),
            "São Paulo": (["11", "12", "13", "14", "15", "16", "17", "18", "19"], 25),
            "Sergipe": (["79"], 26),
            "Tocantins": (["63"], 27)
        }
        return estados_e_ddds

    def obter_ddds_por_ddds(ddd):
        estados_e_ddds = DDD.obter_ddds_e_cliques_por_estado()
        for estado, (ddds, cliques) in estados_e_ddds.items():
            if ddd in ddds:
                return cliques
        return [], 0  # Retorna uma lista vazia e 0 cliques se o DDD não for encontrado

    # Exemplo de uso:
#ddd_desejado = "31"  # Substitua pelo DDD desejado
#cliques_necessarios = DDD.obter_ddds_por_ddds(ddd_desejado)
#print(cliques_necessarios)

