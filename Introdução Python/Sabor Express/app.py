import os 

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa','Ativo':False},
                {'nome':'Pizza Suprema','categoria':'Pizza','Ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana','Ativo':False}]

def exibir_subtitulo(texto):
    linha = '*' * (len(texto) + 4)
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)
    print()


def exibir_nome_do_programa():
    """Essa função exibe o nome do app"""
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opções():
    """Essa função exibe as opções do app"""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    """Essa função retorna ao meu principal solicitando que o usuário digite uma tecla
    Input = Qualquer decla inserida pelo usuário
    Output = Retorno ao menu principal
    """
    input("\nDigite uma tecla para retornar ao menu principal: ")
    main()

def finalizar_app():
    """Essa função é responsável por finalizar o app, exibindo uma mensagem de finalização"""
    exibir_subtitulo("Finalizando o app.\n")


def opcao_invalida():
    """Essa função apresenta uma mensagem quando uma opção inválida é inserida"""
    print("Opção Inválida\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    -Nome do restaurante
    -Categoria
    Outputs:
    Adiciona um novo restaurante a lista de restaurantes

    
    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f'Digite o nome da categoria do deseja restaurante {nome_do_restaurante}: ')
    print(f"O restaurante: {nome_do_restaurante} foi cadastrado com sucesso. ")
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'Ativo':False}
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Essa função lista os restaurantes cadastrados, sua categoria e status"""
    exibir_subtitulo("Listando todos restaurantes.")
    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """Essa função ativa e desativa os restaurantes"""
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrando = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrando = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrando:
        print('O restaurante nâo foi encontrado')


    voltar_ao_menu_principal()

def escolher_opcao():
    """Essa função apresenta todas as funções disponíveis para o usuário"""
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as e:
        print(f"Erro: {e}")


def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()



if __name__ == '__main__':
    main()