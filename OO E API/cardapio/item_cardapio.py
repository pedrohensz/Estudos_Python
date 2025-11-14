class ItemCardapio:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
         return f"Nome:{self.nome} Preço:{self.preco} "
#Aqui eu descobri que caso você atribua um métdo a classe pai, ambas as classe pegam ele também
#exemplo do método string