"""
Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

nome
artista
duracao
Copiar código
Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..

"""
class musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = musica()
musica1.nome = 'The Way Things Go'
musica1.artista = 'beabadoobee'
musica1.duracao = 307

musica2 = musica()
musica2.nome = "Dont Dream is Over"
musica2.artista = "Crowded House"
musica2.duracao = 356

musica3 = musica()
musica3.nome = "Every Breath You Take"
musica3.artista = "The Police" 
musica3.duracao = 349