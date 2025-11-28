"""
>Criar um arquivo que recebe dados do usuário
>Armazenar esses dados em um arquivo txt
>Ler os dados salvos nesse arquivo
"""
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

with open("Data_Entry.txt", "a",encoding="UTF-8") as f:
    f.write(f"Nome:{nome}\n")
    f.write(f"Idade: {idade}\n")

with open("Data_Entry.txt", "r") as f:
    leitura = f.read()
    print(leitura)