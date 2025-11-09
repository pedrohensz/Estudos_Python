"""
A criação de classes em Python é uma maneira poderosa de estruturar código de forma orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Livro que representa informações sobre um livro, como título, autor e número de páginas:

class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade
Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.


"""
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f"{self.nome} | {self.idade} | {self.profissao}"
    
    def aniversario(self):
        self.idade += 1
    
    def saudacao(self):
        return f"Olá meu nome é {self.nome} e sou um {self.profissao} de {self.idade} anos de idade."


p1 = Pessoa("Pedro",23,"Programador")

print(p1.aniversario())
print(p1.saudacao())
