"""Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?"""

"""Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante."""
class Restaurante:
    nome = ''
    categoria = ''
    status = False

Restaurante1 = Restaurante()
Restaurante1.nome = "Praça"
Restaurante1.categoria = "Italiana"
Restaurante1.status = False 
"""Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante."""
print(f"O nome do restaurante é {Restaurante1.nome}")
"""Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo."""
print(f"O restaurante {Restaurante1.nome} está {"Ativo" if Restaurante1.status == True else "Desativado"}")
"""Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria."""
categoria = Restaurante1.categoria
print(f"A categoria é {categoria}")
"""Altere o valor do atributo nome para 'Bistrô'."""
Restaurante1.nome = "Bistrô"
print(f"O nome do restaurante agora é {Restaurante1.nome}")

"""Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'."""
Restaurante_pizza= Restaurante()
Restaurante_pizza.nome = "Pizza Place"
Restaurante_pizza.categoria = "Fast Food"
Restaurante_pizza.status = False

"""Verifique se a categoria da instância restaurante_pizza é 'Fast Food'."""
print(f"A categoria do Restaurante {Restaurante_pizza.nome} é {Restaurante_pizza.categoria}")
"""Mude o estado da instância restaurante_pizza para ativo."""
Restaurante_pizza.status = True

"""Imprima no console o nome e a categoria da instância restaurante_praca."""
Restaurante1 = Restaurante()
Restaurante1.nome = "Praça"
Restaurante1.categoria = "Italiana"
Restaurante1.status = False 
print(f"A categoria do Restaurante {Restaurante1.nome} é {Restaurante1.categoria} ")