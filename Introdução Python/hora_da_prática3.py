"""
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
"""
Numeros_0_a_10 = [1,2,3,4,5,6,7,8,9,10]
Ano_nascimento = [2002,2025]
quatro_nomes = ["Pedro","Henrique","João", "Thiago"]

lista_final = [Numeros_0_a_10,quatro_nomes,Ano_nascimento]
print(lista_final)
"""2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

"""
for numero in Numeros_0_a_10:
    print(numero)

"3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10."
impares = []
for numero in Numeros_0_a_10:
    if numero % 2 != 0:
        impares.append(numero)
        print(numero)
        
total =(sum(impares))
print(total)

"""4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente."""
Numeros_0_a_10_dec = sorted(Numeros_0_a_10, reverse=True)
for numero in Numeros_0_a_10_dec:
    print(numero)

"""5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10."""
n1 = int(input("insira um número: "))

for numeros in  Numeros_0_a_10:
    print(numeros * n1)

"""
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
"""

try:
    numeros = (input("Insira os números da sua lista"))
    soma = sum(list(numeros))
    print(soma)
except ValueError:
    print("Valor inválido. ")