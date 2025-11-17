"""

Exercícios
1-Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
2-No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
3-Crie uma nova classe chamada Carro que herda da classe Veiculo.
4-No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
5-Em um arquivo chamado main.py, importe a classe Carro.
6-No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
"""
from abc import ABC, abstractmethod
#1
class Veiculo(ABC):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()
    
    @abstractmethod
    def ligar(self):
        pass


#2
class Veiculo(ABC):
    def __init__(self,marca,modelo):
        super().__init__()
        self.modelo = modelo
        self.marca = marca
    def __str__(self):
        return f"Marca:{self.marca}| Modelo:{self.modelo} | Cor: {self.cor}"
    
    @abstractmethod
    def ligar(self):
        pass

#2
class Carro(Veiculo):
    def __init__(self, marca, modelo,cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        print(f"O carro {self.modelo} está ligado.")