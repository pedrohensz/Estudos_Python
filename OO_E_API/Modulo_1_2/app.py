from cardapio.bebida import Bebida
from cardapio.prato import Prato
from OO_E_API.Modulo_1_2.restaurante import Restaurante

bebida_suco = Bebida("Suco de Melancia", 5.0, "Grande")
prato_paozinho = Prato("Pãozinho", 2.00, "O melhor pão da cidade")
restaurante_praca = Restaurante("Praça", "Gourmet")

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

#Aqui eu descobri que caso você atribua um métdo a classe pai, ambas as classe pegam ele também
#exemplo do método string
def main():
    print(bebida_suco)
    print(prato_paozinho)
if __name__ == '__main__':
    main()