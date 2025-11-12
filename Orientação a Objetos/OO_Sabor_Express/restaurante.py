from avaliacao import Avaliacao

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

#restaurante_praca = Restaurante("Praça","Gourmet")
#restaurante_pizza = Restaurante("Pizza Express","Italiana")
#Restaurante.listar_restaurantes()

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
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do Restraurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        return "Ativo 👌" if self._ativo else "Desativado 📛"
#restaurante_praca = Restaurante("Praça","Gourmet")
#restaurante_pizza = Restaurante("Pizza Express","Italiana")
#Restaurante.listar_restaurantes()

"""
Aprofundando em propriedades:
Na aula em questão é passado que houve uma mudança na regra de negócio e todos restaurantes devem ter a primeira letra maiúscula
(o que pode ser alterado direto no atributo nome usando o .title()), também é passado a noção de atributos públicos, internos e privados. Sendo eles nomeados sem underscore(público, acesso livre), com 1 underscore (interno, ainda acessível mas por convenção não deve ser alterado) e 2 underscore (mangling dificulta o acesso mas não impede). Também foi passado sobre o @classmethod quando um método não vai variar conforme o objeto mas sempre que chamado trará a mesma resposta por que se refere a classe inteira. (geralmente não envolve o self)
"""

class Restaurante:
    restaurantes = []
    def __init__(self, _nome, _categoria):
        self.nome = _nome.title()
        self.categoria = _categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do Restraurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        return "Ativo 👌" if self._ativo else "Desativado 📛"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    
"""
Criando classe de avaliação
"""
class Restaurante:
    restaurantes = []
    def __init__(self, _nome, _categoria):
        self.nome = _nome.title()
        self.categoria = _categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do Restraurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        return "Ativo 👌" if self._ativo else "Desativado 📛"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)

"""
Após criarmos o método de avaliação, precisamos que ela seja exibida
de alguma maneira. E isso será feito abaixo com a criação de um 
método que irá fazer a soma e média das avaliações.
"""

class Restaurante:
    restaurantes = []
    def __init__(self, _nome, _categoria):
        self.nome = _nome.title()
        self.categoria = _categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    

    @property
    def ativo(self):
        return "Ativo 👌" if self._ativo else "Desativado 📛"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao: #caso não tenha nenhuma avalição retorna zero
            return 0
        soma_das_notas = sum(Avaliacao._nota for Avaliacao in self._avaliacao) #soma de todas as notas contidas na lista de avaliacoes
        quantidade_de_notas = len(self._avaliacao) #armazena o numero de avaliacoes
        media = round(soma_das_notas/ quantidade_de_notas, 1) #realiza o calculo da média
        return media #retorna a média
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restraurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliação'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}")