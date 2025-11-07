"""
O que é uma classe ?
Uma abstração do mundo real em um código onde será possível juntar
tipos diferentes
Nome = ' ' String
Categoria = ' ' String
Ativo ou não = Booleano
Como eu consigo que, qualquer restaurante que eu vá criar tenham esses 3 atributos?
Utilizando uma palavra reservada do python chamada Class
sempre que utilizamos essa palavra, estamos criando uma classe
e podemos nomear ela 

"""
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

"""
Como criamos uma classe a partir de um objeto ? 

"""
restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()
"Qualquer restaurante que vai ser criado, terá que ser armazenado em uma variável que é igual a classe restaurante"

restaurantes = [restaurante_praca, restaurante_pizza]



"""
Método construtor
O construtor é executado automaticamente sempre que um objeto de uma classe é instânciado
Serve para definir os valores iniciais de cada atributo
"""
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
"""
O self é utilizado para "dizer ao python" qie o valor do argumento deve ser armazenado no atributo que está dentro do objeto
O nome self é uma convenção, podendo ser chamado de "qualquer coisa" visto que é uma variável

"""


restaurante_praca = Restaurante("Praça","Gourmet")
restaurante_pizza = Restaurante("Pizza Express","Italiana")


"""
Métodos especiais
São métodos nativos do python, utilizando o comando dir() você consegue vizualizar todos os métodos, inclusio o __str__ que trás a visulização do método via string
"""
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
restaurante_praca = Restaurante("Praça","Gourmet")
restaurante_pizza = Restaurante("Pizza Express","Italiana")
    


"""
Criando métodos
O python tem métodos especiais chamados de Dunder options( Double Underscore) essa seleção engloba o método construtor (__init__) e diversos outros, esses métodos definem o comportamento especial dos objetos.
Abaixo criamos o método "listar restaurantes" que pode ser chamado com a classe Restaurante e listará todos restaurantes instânciados.


"""
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

restaurante_praca = Restaurante("Praça","Gourmet")
restaurante_pizza = Restaurante("Pizza Express","Italiana")
Restaurante.listar_restaurantes()

"""
Uma classe é o molde.

Um objeto é o produto feito com esse molde.

Um método é um comportamento que pertence a esse molde — e, portanto, também a todos os objetos criados a partir dele.
"""
#property
"""
@property é um decorador usado para transformar um método em um atributo "controlado".
Ele serve para mascarar uma função dentro da classe, permitindo acessar o seu valor
como se fosse um atributo (sem precisar usar parênteses), deixando o código mais limpo.

Além disso, o @property permite adicionar lógica (como validação ou formatação)
sem alterar a forma de acesso ao atributo.
"""
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "Ativo 👌" if self.ativo else "Desativado 📛"
restaurante_praca = Restaurante("Praça","Gourmet")
restaurante_pizza = Restaurante("Pizza Express","Italiana")
Restaurante.listar_restaurantes()
