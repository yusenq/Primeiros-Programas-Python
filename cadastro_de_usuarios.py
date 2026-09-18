informacoes_cadastrais = {
    'nome_usuario': [],
    'idade_usuario': [],
    'senha_usuario': []
}

quest_entrada_sistema = str(input('Deseja se cadastrar? \n'))
quest_entrada_sistema.upper()

def login_usuario():
    cadastro_nome_usuario = str(input('\nInforme seu nome: '))
    informacoes_cadastrais['nome_usuario'].append(cadastro_nome_usuario)
           
    cadastro_idade_usuario = str(input('\nInforme sua idade em anos: '))
    informacoes_cadastrais['idade_usuario'].append(cadastro_idade_usuario)
           
    cadastro_senha_usuario = str(input('\nCrie uma senha de sua preferência: '))
    informacoes_cadastrais['senha_usuario'].append(cadastro_senha_usuario)
           
    print(f'\nBem vindo, {informacoes_cadastrais["nome_usuario"][0]} \nVocê tem {informacoes_cadastrais["idade_usuario"][0]} \nSua senha é: {informacoes_cadastrais["senha_usuario"][0]}')

if quest_entrada_sistema.upper() == 'SIM':
    quest_login = str(input('\nOlá, Usuário, já tem login? \n'))
    quest_login.upper()

    if quest_login.upper() == 'NÃO' or quest_login.upper() == 'NAO':

        login_usuario()

    elif quest_login.upper() == 'SIM' or quest_login.upper() == 'TENHO' or quest_login.upper() == 'JA' or quest_login.upper() == 'JÁ':
                
        if not informacoes_cadastrais['nome_usuario'] or not informacoes_cadastrais['idade_usuario'] or not informacoes_cadastrais['senha_usuario']:
            print('\nVocê ainda não tem cadastro registrado, se cadastre para continuar!')

            login_usuario()
                   
    elif quest_login.upper() != 'NÃO' or quest_login.upper() != 'NAO' or quest_login.upper() != 'SIM' or quest_login.upper() != 'TENHO' or quest_login.upper() != 'JA' or quest_login.upper() != 'JÁ':
        print('\nEstá resposta é inválida, tente novamente.')

        quest_login = str(input('\nOlá, Usuário, já tem login? \n'))
        quest_login.upper()

        if quest_login.upper() == 'NÃO' or quest_login.upper() == 'NAO':

            login_usuario()

        elif quest_login.upper() == 'SIM' or quest_login.upper() == 'TENHO' or quest_login.upper() == 'JA' or quest_login.upper() == 'JÁ':
                
            if not informacoes_cadastrais['nome_usuario'] or not informacoes_cadastrais['idade_usuario'] or not informacoes_cadastrais['senha_usuario']:
                print('\nVocê ainda não tem cadastro registrado, se cadastre para continuar!')

                login_usuario()

elif quest_entrada_sistema.upper() == 'NÃO' or quest_entrada_sistema.upper() == 'NAO':
    print(f'Obrigado, até mais!')


else:
    print('Algo de errado aconteceu! \nReinicie o programa.')
    exit()