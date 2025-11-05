#Imprima a frase: Python na Escola de Programação da Alura.
print("Python na Escola de Programação Alura")

#Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = "Pedro"
idade = 23
print(f"Meu nome é {nome} e tenho {idade} anos.")

n1 = "alura"
indice = 0
for letra in n1:
    while indice <len(n1):
        print(n1[indice])
        indice += 1
pi = 3.14159

print(f"O valor de pi arredondado é: {pi} ")

print('A','L','U','R','A',sep='\n')