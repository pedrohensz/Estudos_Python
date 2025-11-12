"""
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
"""
class carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = carro(modelo='Fusca', cor='Azul', ano=1970)

"""
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
"""
"""
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
"""
class restaurante:
    def __init__(self, nome, categoria, ativo, chefe, local):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.chefe = chefe
        self.local = local
    

    
restauranteDOM = restaurante("Dom","Culinária Brasileira",False,"Alex Atala", "São Paulo")
"""
# 4) Adicione um método especial `__str__` à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
"""
class restaurante:
    def __init__(self, nome, categoria, ativo, chefe, local):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.chefe = chefe
        self.local = local
    
    def __str__(self):
        return (f"{self.nome} | {self.categoria}")

restauranteDOM = restaurante("Dom","Culinária Brasileira",False,"Alex Atala", "São Paulo")
print(restauranteDOM)


"""
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
"""
class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')