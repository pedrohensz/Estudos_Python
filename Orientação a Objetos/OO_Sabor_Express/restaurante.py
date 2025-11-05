"""
O que é uma classe ?
Uma abstração do mundo real em um código onde será possível juntar
tipos diferentes
Nome = ' ' String
Categoria = ' ' String
Ativo ou não = Booleano
Como eu consigo que, qualquer restaurante que eu vá criar tenham esses 3 atributos?
Utilizando uma palavra reservada do python chamada Class
sempre que utilizamos essa palavra, estamos criando uma classe
e podemos nomear ela 

"""
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

"""
Como criamos uma classe a partir de um objeto ? 

"""
restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"
restaurante_praca.ativo = False
restaurante_pizza = Restaurante()
"Qualquer restaurante que vai ser criado, terá que ser armazenado em uma variável que é igual a classe restaurante"

restaurantes = [restaurante_praca, restaurante_pizza]

<<<<<<< HEAD
print(restaurante_praca)
=======
print(vars(restaurante_praca))
>>>>>>> 4ba570466ea667860cbe20387acfbf89c5b5a254
