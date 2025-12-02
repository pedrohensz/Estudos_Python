"""Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. Esses critérios são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize essa validação de forma automática.
Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?
Exemplo de Entrada:
Digite a URL para validação: https://monitorrenan.com
Saída esperada:
URL válida!"""

url = input("Digite a URL para validação: ")

if url.startswith("https://") and url.endswith(".com"):
    print("URL Válida! ")
else:
    print("URL Inválida. ")