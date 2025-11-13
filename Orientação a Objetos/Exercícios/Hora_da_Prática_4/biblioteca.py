
#5-Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from exercicios import Livro

#6-No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro1 = Livro("A Arte Da Guerra", "Sun Tzu", 500)
def main():
    livro1.emprestar()
    print(F"O livro {livro1.titulo} está {livro1.disponivel} ")

if __name__ == '__main__':
    main()

# 7-No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

print(Livro.verificar_disponibilidade(500))