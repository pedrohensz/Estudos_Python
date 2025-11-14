from cardapio.item_cardapio import ItemCardapio
"""
Herança
Herança é quando uma classe Herda atributos e métodos de outra classe (classe pai), isso faz com que você possa usar atributos da classe pai sem precisar escrever os mesmos novamente. Poupando tempo e duplicação de código.
"""

class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao