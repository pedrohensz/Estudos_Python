"""
Nas últimas aulas do curso, estavamos criando as classes, atributos
no mesmo arquivo, mas nesse módulo foi passado que em casos reais 
as classes são criadas e alteradas em um arquivo e os objetos instânciados
em outro, usando a função import, como feito abaixo.
"""

from restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_mexicano = Restaurante("Mexican Food", "Comida Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_japones.receber_avaliacao("Pedro", 4.5)
restaurante_japones.receber_avaliacao("Ana", 5)
restaurante_japones.receber_avaliacao("João", 3.8)


restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()