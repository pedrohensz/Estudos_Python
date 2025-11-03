"""1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade."""
pessoa = {'nome':'Pedro', 'Idade':23,'Cidade':'Valinhos'}

""" 2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário"""

pessoa['Idade'] = 25
print(pessoa)
pessoa['Profissao'] = 'Programador'
print(pessoa)
pessoa.pop('Profissao')
print(pessoa)

"""3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados."""
quadrados = {}
for numero in range(1,6):
    quadrados[numero] = numero ** 2

print(quadrados)

"""4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário."""
novo = {"1":"Pedro", "2":"Cristiano", "3":"Ronaldo"}

chave = input("Insira a chave desejada: ")
if chave in novo:
    print(f"Chave encontrada {novo[chave]}")
else:
    print('Chave não encontrada')


"""5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário."""
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)