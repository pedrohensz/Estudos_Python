"""
Apis (Application Programming Interface)
Apis são basicamente um conjunto de regras que permitem a comunicação entre diferentes aplicações. Elas funcionam como uma "guarita em uma ponte" que definem como um sistema pode requisitar informações de outro.
No módulo 4 somos introduzidos ao JSON(JavaScript Object Notation) um padrão muito utilizado em APIs por ser leve e fácil de ler tanto por humanos 
quanto por máquinas.
Abaixo estamos estudando a biblioteca requests que é permite realizar as solicitações em HTTP para apis.
e estamos requisitando as informações contidas no link armazenado na variavel URL. 

"""
import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json" 

response = requests.get(url)

# print(response)

if response.status_code == 200:
    dados_json = response.json()
    print(dados_json)
else:
    print(f"O erro foi {response.status_code}")


#Filtrando dados do arquivo JSON
import requests

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json" 

response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {} #criamos um dicionário que vazio que vai receber os dados do restaurante
    for item in dados_json: # iterando os items retornados pela API
        nome_do_restaurante = item['Company'] #aqui definimos que nome do restaurante é o item company
        if nome_do_restaurante not in dados_restaurante: #se o nome do restaurante não estiver em dados restaurante
            dados_restaurante[nome_do_restaurante] = [] #dicionário com o nome do restaurante será criado
        #dicionário com o nome do restaurante recebe todos os itens pertencentes ao mesmo criando um item "prato"
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
        
    print(f"O erro foi {response.status_code}")

# print(dados_restaurante["Pizza Hut"])

"""
Criando arquivos com Python
"""
for nome_do_restaurante, dados in dados_restaurante.items(): #percorrendo cada restautante e seus dados
    nome_do_arquivo = f'{nome_do_restaurante}.json' #definindo o nome do arquivo baseado no nome do restaurante
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        #open cria um arquivo, w significa que é no modo de escrita (write)
        json.dump(dados,arquivo_restaurante,indent=4)# dados é alista contendo os items de cada restaurante, arquivo restaurante é o nome do arquivo criado pelo dump e ident indentação pra estilizar o arquivo JSON