"""Listas
São estruturas de dados ordenadas e mutáveis, são anunciadas
por colchetes, são indexadas (começando em zero [0]), aceitam
múltiplos tipos de dados(str, int, float,bool)
As listas possuem métodos como append, e insert 
Ex:
 """
lista = ['8 Mile - Rua das Ilusões', 'Matrix', 'Clube da Luta']
#print (lista[0])

"""
Tuplas
São estruturas de dados ordenadas e IMUTÁVEIS, são anunciadas por
parênteses.
As tuplas, por serem imutáveis não possuem nenhum método que 
possam alterá-las (append, insert), são mais utilizados em
datas e configurações (informações constantes)
Ex:
"""
t = '10/10/2025','24/11/2025','01/06/2019'
#print(type(t))
#print(t[1])

"""
Dicionário
São estruturas de dados ordenadas e mutáveis, são anunciadas por chaves.
A diferença das tuplas e listas é que os dicionários são compostos
por chaves e valores.
"""
dados = {lista[0]:t[0]}

for chave, valor in zip(lista, t):
  dados[chave] = valor

print(dados)