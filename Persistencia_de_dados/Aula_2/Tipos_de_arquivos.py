import csv
import json
"""
TXT
Arquivos TXT são arquivos de texto simples, sem formatação.
São usados para armazenar dados em formato cru, como notas, logs,
resultados ou qualquer conteúdo textual não estruturado.

O conteúdo é apenas texto contínuo, sem separadores definidos.
Ex:
"""
with open("exemplo.txt", "w", encoding='UTF-8') as f:
    f.write("Olá Mundo")

#Para leitura
with open("exemplo.txt", "r", encoding='UTF-8') as f:
    conteudo = f.read()
    print(conteudo)

#Para adicionar
with open("exemplo.txt", "a") as f:
    f.write("Last lines")

"""
CSV
CSV significa 'Comma-Separated Values'. São arquivos de dados
estruturados onde cada linha representa um registro e cada campo
é separado por vírgula (ou ponto e vírgula).

É muito utilizado em planilhas, bancos de dados e análise de dados.
Ex:
"""
with open ("dados.csv", "w", newline= "") as f:
    writer=csv.writer(f)
    writer.writerow(["Nome","Sobrenome"])
    writer.writerow(["Cristiano","Ronaldo"])
    writer.writerow(["Lionel","Messi"])

#Leitura
with open ("dados.csv","r",newline="") as f:
    reader = csv.reader(f)
    
    for linhas in reader:
        print(linhas)

"""
JSON
JSON significa 'JavaScript Object Notation'. É um formato baseado
em texto, estruturado em pares chave : valor.

É muito usado em APIs, integração entre sistemas e troca de dados,
por ser leve, estruturado e fácil de ler.

JSON trabalha com:
- objetos (dict no Python),
- listas,
- strings,
- números,
- booleanos.

Ex:
"""
dados = {"Nome":"Hometown Glory","Autor":"Adele","Duracao":"3:33"}
with open("Musicas.json","w",encoding="UTF-8") as f:
    json.dump(dados,f,indent=4)

with open("Musicas.json","r") as f:
    dados = json.load(f)
    print(dados)

"""
Ao final da Aula é pontuado que arquivos não são muito confiáves para armazenamento de dados:
-Falta de seguraça e integridade
-Não são relacionais (Fica difícil localizar informações)
-Se o sistema sobrescreve muito fica mais fácil do mesmo corromper
Por isso o ideal é fazer o uso de bancos de dados.

"""