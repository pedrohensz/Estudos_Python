""" Solicite ao usuário que insira um número e, em seguida,
 use uma estrutura if else para determinar se o número é par ou ímpar."""
numero = int(input("Insira um número inteiro: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

"""Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
"""
numero = int(input("Insira a sua idade: "))
if numero <= 12:
    print("Você é criança")
elif numero >= 13 or numero <= 18:
    print("Você é Adolescente")
elif numero >= 18:
    print("Você é Adulto")

"""
Solicite um nome de usuário e 
uma senha e use uma estrutura 
if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

"""

usuario_login = input("Insira seu nome ")
senha_login = input("Insira sua senha: ")
login = "Pedro"
senha = "batata_maneira"
if senha_login == senha and usuario_login == login:
    print("Logado com sucesso")
else:
    print("Senha errada, tente outra vez. ")


"""
4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.

"""
x = float(input("Insira o ponto X"))
y = float(input("Insira o ponto Y"))

if x > 0 and y > 0:
    print("O ponto está no Primeiro Quadrante")
elif x < 0 and y > 0:
    print("O ponto está no Segundo Quadrante")
elif x < 0 and y < 0:
    print("O ponto está localizado no Terceiro Quadrante")
elif x > 0 and y < 0:
    print("O ponto está localizado no Quarto Quadrante")
else:
    print("O ponto está localizado no eixo de origem")