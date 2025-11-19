"""
API
É um conjunto de regras que permite que um software peça informações 
ou envie dados para outro software.

Exemplo:
Quando você vai a um restaurante, você não entra na cozinha e não sabe 
como o chef prepara os pratos. Você apenas olha o cardápio, faz o pedido 
(que é como uma *request*) e o garçom retorna com o prato, 
que representa os dados solicitados.

Framework (exemplo: FastAPI)
Um framework é um kit de ferramentas pronto que facilita o desenvolvimento.

Exemplo:
Criar um sistema sem framework é como construir uma casa fazendo tudo do zero: 
misturar cimento, cortar madeira, montar parede, puxar fiação.  
Com um framework, essas partes pesadas já estão prontas. 
Assim, você foca apenas em “arquitetar a obra”, ou seja, 
na lógica do código, enquanto o framework cuida da estrutura.

"""

#criando a primeira rota com fastAPI
from fastapi import FastAPI, Query
import requests

app = FastAPI()

"""
Aqui foi criado um servidor rodando localmente e, dentro dele, 
foi definida uma rota "/api/hello". 
Quando essa rota é acessada (pelo navegador ou por outro software),
a aplicação executa a função associada e retorna o JSON 
{"Hello": "World!"}.
"""
@app.get('/api/hello')
def hello_world():
    return{'Hello':'World!'}

"""
Criando diferentes rotas
Pegando o exemplo do último módulo vamos inserir o cardápio no nosso servidor criando uma rota para cada restaurante
"""
@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json" 
    response = requests.get(url)



    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'dados':dados_json}
        dados_restaurante = {}
        for item in dados_json:
            nome_do_restaurante = item['Company']
            if item['Company'] == restaurante:
                dados_restaurante[nome_do_restaurante].append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })
        return {'Restaurante':restaurante,'Cardapio':dados_restaurante}
    else:
        print(f"O erro foi {response.status_code}")