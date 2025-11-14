"""
Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
"""

"""
Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
"""
from veiculo import Carro,Moto

def main():
    carro1 = Carro("Ferrari", "La Ferrari", 2)
    moto1 = Moto("Kawasaki","Ninja","Esportiva")
    carro2 = Carro("McLaren", "Senna", 2)
    print(carro1)
    print(carro2)
    print(moto1)

if __name__ == "__main__":
    main()


