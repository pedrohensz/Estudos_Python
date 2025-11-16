from cardapio.bebida import Bebida
from cardapio.prato import Prato

bebida_suco = Bebida("Suco de Melancia", 5.0, "Grande")
prato_paozinho = Prato("Pãozinho", 2.00, "O melhor pão da cidade")


#Aqui eu descobri que caso você atribua um métdo a classe pai, ambas as classe pegam ele também
#exemplo do método string
def main():
    print(bebida_sucoo)
    print(prato_paozinho)

if __name__ == '__main__':
    main()