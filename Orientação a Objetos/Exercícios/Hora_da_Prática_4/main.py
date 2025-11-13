"""8-Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str."""
from exercicios import Livro

livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("A Arte Da Guerra", "Sun Tzu", 500)
def main():
    print(livro1,livro2,livro3)

if __name__ == '__main__':
    main()

