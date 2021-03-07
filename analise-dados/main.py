import requests
import pandas as pd
import numpy as np

import json

def buscar_dados():

    result = requests.get('http://localhost:21262/pesos/2', headers={'token':'token_de_acesso'})    
    
    #my_json é uma lista de jsons obtido pelo requests
    my_json = json.loads(result.content)

    # passando a minha lista de jsons para o formato str
    my_json = json.dumps(my_json)
    

    # passando o my_json para o formato de tabela para facilitar minhas analises
    dados = pd.read_json(my_json, orient='records')
    
    
    # Passo Parte2 - Passo 2
    #Verificar se não tem nenhum animal em mais de um lote

    dupli3 = dados[['idlote','idanimal']].query('idlote == 1')
    print(dupli3)
    print('ID_ANIMAL NO LOTE 1:',dupli3['idanimal'].unique())

    dupli4 = dados[['idlote','idanimal']].query('idlote == 2')
    print('ID_ANIMAL NO LOTE 2:',dupli4['idanimal'].unique())

    dupli5 = dados[['idlote','idanimal']].query('idlote == 3')
    print('ID_ANIMAL NO LOTE 3:',dupli5['idanimal'].unique())

    dupli6 = dados[['idlote','idanimal']].query('idlote == 4')
    print('ID_ANIMAL NO LOTE 4:',dupli6['idanimal'].unique())

buscar_dados()