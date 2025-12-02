"""Strings são sequências de caracteres usadas para representar textos.
Em Python, podem ser declaradas com aspas simples, duplas ou triplas (para textos longos ou multilinhas).
"""
#Exemplos:
mensagem = "Olá, Mundo."

texto = """Essa é uma string de múltiplas linhas,
e é assim que a declaramos."""

#Principais Métodos de Strings
teste = " Python"

print(teste.strip())      # remove espaços no início ou fim
print(teste.upper())      # transforma em MAIÚSCULAS
print(teste.lower())      # transforma em minúsculas
print(teste.replace("Python", "Mundo"))  # substitui partes do texto

# F-Strings

"Permitem inserir variáveis dentro do texto de forma simples e elegante."

estudante = "Pedro"
nota = 10

frase = f"O estudante {estudante} tirou a nota {nota}."
print(frase)

# Indexação

"Strings podem ser tratadas como listas de caracteres."

texto = "Python"

print(texto[5])   # n  (6ª letra)
print(texto[-1])  # n  (última letra)

# Slicing (Fatiamento)

"Sintaxe:"

"string[inicio:fim:passo]"


#início → índice onde começa

#fim → onde termina (não inclusivo)

#passo → de quantos em quantos caracteres

texto1 = "Python"

print(texto1[1:4])   # yth
print(texto1[:3])    # Pyt
print(texto1[::2])   # Pto

# Operador in

#Verifica se uma substring existe dentro de outra string.

texto = "Python"

print("Py" in texto)  # True
print("jo" in texto)  # False

# .startswith() e .endswith()

"Verificam se a string começa ou termina com determinada substring."
texto = "Joelho"

print(texto.startswith("Jo"))   # True
print(texto.endswith("Ilho"))   # False