"""
Classes Abstratas
São classes que não são instânciadas
diretamente, ela serve como um molde
para outras classes.
Dentro dela são definidos métodos
obrigatórios que todas as classes 
filhas (que herdam dela) devem implementar.
são comummente utilizadas para garantir
que as classes tenham méotodos obrigatórios,
definir uma estrutura comum.
"""
from abc import ABC,abstractmethod
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
         return f"Nome:{self.nome} Preço:{self.preco} "

    @abstractmethod
    def aplicar_desconto(self):
        pass
#Aqui eu descobri que caso você atribua um métdo a classe pai, ambas as classe pegam ele também
#exemplo do método string