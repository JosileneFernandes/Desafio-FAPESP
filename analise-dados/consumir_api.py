import requests
import pandas as pd
import json



def consumir_dados():

    result = requests.get('http://localhost:21262/pesos/', headers={'token':'token_de_acesso'})    
    
    #my_json é uma lista de jsons obtido pelo requests
    my_json = json.loads(result.content)

    # passando a minha lista de jsons para o formato str
    my_json = json.dumps(my_json)
    
    # passando o my_json para o formato de tabela para facilitar minhas analises
    dados = pd.read_json(my_json, orient='records')

    print(dados)

consumir_dados()