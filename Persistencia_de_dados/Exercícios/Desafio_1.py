"""A partir do dicionário que você criou, faça um loop no dicionário e imprima na tela suas chaves e os valores

Se quiser saber mais sobre como realizar essa atividade, clique na opinião da pessoa instrutora."""

lista = ['8 Mile - Rua das Ilusões', 'Matrix', 'Clube da Luta']
t = '10/10/2025','24/11/2025','01/06/2019'
dados = {lista[0]:t[0]}

for chave, valor in zip(lista, t):
  dados[chave] = valor

for k,v in dados.items():
    print(f"{k}: {v}")