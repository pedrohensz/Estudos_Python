"""No Python, a criação de classes é uma parte essencial da programação orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:

class Musica:
    nome = ''
    artista = ''
    duracao = int
Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python."""

class musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def tocar(self):
        return (f"A música {self.nome} de {self.artista} está tocando") 


musica1 = musica('The Way Things Go', 'beabadoobee',307 )

musica2 = musica("Dont Dream is Over", "Crowded House", 356)

musica3 = musica("Every Breath You Take","The Police",349)


print(musica1.tocar())