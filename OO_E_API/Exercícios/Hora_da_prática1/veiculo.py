"""Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão."""

class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

"""
Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
"""
class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
    
    @property
    def ligado(self):
        return "Ligado" if self._ligado else "Desligado"

    def __str__(self):
        return f"O Veículo: {self.marca} Modelo:{self.modelo} está {self.ligado}"
    
"""
Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
"""

class Carro(Veiculo):
    def __init__(self, marca, modelo,portas):
        super().__init__(marca, modelo)
        self.portas = portas
    
    def __str__(self):
        return f"{super().__str__()} - Portas: {self.portas}"
    
"""
Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
"""
class Moto(Veiculo):
    def __init__(self, marca, modelo,tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def __str__(self):
        return f"{super().__str__()} - Tipo: {self.tipo}"
    

teste = Veiculo("Toyota", "Corolla")
