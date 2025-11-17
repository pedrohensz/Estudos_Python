"""Crie uma classe chamada Sobremesa que herda de ItemCardapio, adicione atributos específicos como tipo, tamanho e descricao à classe Sobremesa. Ajuste a inicialização da classe para incluir esses novos atributos, possibilitando a criação de um novo item ao cardápio do restaurante.
Atualize o método __str__ conforme necessário para refletir essas mudanças.
Certifique-se de que a classe Sobremesa mantenha a herança do método aplicar_desconto de ItemCardapio."""

from cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco,descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho   
    def __str__(self):
         return f"{self.nome} - R$ {self.preco:.2f}"
    
    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.15)