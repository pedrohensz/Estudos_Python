"""
Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo". Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.
Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir o texto com as alterações aplicadas.
Exemplo de Entrada:
Digite o texto a ser revisado: O dia está bom, tudo está bom.`
Qual palavra deseja substituir? bom
Qual a nova palavra? ótimo
Copiar código
Saída esperada:
O dia está ótimo, tudo está ótimo.
"""
texto = input("Digite o texto a ser revisado: ")
p1 = input("Qual palavra deseja substituir? ")
p2 = input("Qual a nova palavra? ")
corrigido = texto.replace(p1, p2)
print(corrigido)