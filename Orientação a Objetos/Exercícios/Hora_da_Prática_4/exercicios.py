"""
1-Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
2-Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
3-Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
4-Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
5-Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
6-No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
7-No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
8-Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
"""
#1
class Livro():
    def  __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

#2
class Livro():
    def  __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# print(livro1)
# print(livro2)

#3
class Livro():
    def  __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = False
    
    def __str__(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"
    
    def emprestar(self):
        self.disponivel = not self.disponivel
    



livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)



#print(f"Antes de emprestar: Livro disponível? {livro2.disponivel}")
#livro2.emprestar()
#print(f"Depois de emprestar: Livro disponível? {livro2.disponivel}")

#4
class Livro():
    def  __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = False
    

    @property
    def ativo(self):
        return "Disponível 👍" if self.disponivel else "Indisponível 📛"

    def emprestar(self):
        self.disponivel = not self.disponivel
    
    def __str__(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

    def verificar_disponibilidade(ano):
        lista_livros = [livro1,livro2]
        livros_ano =[]
        for livro in lista_livros:
            if ano == livro.ano_publicacao:
                livros_ano.append(livro.titulo)
                return f"Os livros de {ano} são {livros_ano}"
            

                
                
            

livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

print(Livro.verificar_disponibilidade(1954))

#5



