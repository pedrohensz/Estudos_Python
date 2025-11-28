"""
Na Escola PythonVille, o professor quer registrar as notas dos alunos e depois consultar quem teve um bom desempenho.

Além disso, a coordenação precisa manter um registro organizado com essas informações para uso futuro.

O que você deve fazer:

Crie um programa que grave em um arquivo alunos.csv uma lista de alunos e suas notas.
Leia o arquivo alunos.csv e imprima apenas os alunos com nota maior ou igual a 7.0.

"""
import csv
nome_aluno = input('Insir o nome do aluno: ')
nota = input("Insira a nota do aluno: ")

with open("C:\\Users\\Usuario\\Desktop\\Pedro\\Estudos\\Estudos_Python\\Persistencia_de_dados\\Exercícios\\Alunos.csv","a",encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Nome','Nota'])
    writer.writerow([f'{nome_aluno}',f'{nota}'])

with open("C:\\Users\\Usuario\\Desktop\\Pedro\\Estudos\\Estudos_Python\\Persistencia_de_dados\\Exercícios\\Alunos.csv","r",encoding="UTF-8") as f:
    readers = csv.reader(f)
    for linha in readers:
        print(linha)