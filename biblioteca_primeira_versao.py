informacoes_cadastrais = {
    'titulo_do_livro': [],
    'categoria_do_livro': [],
    'autor_do_livro': []
}

administradores_biblioteca = {
    'admistradores_gerais': ["FELIPE NEGRI", "CINTIA NEGRI", "MARCELO NEGRI"],
    'supervisora_de_secao': ["ISADORA BARBIZAM"],
    'supervisora_de_recebidos': ["NATHALIA NEGRI"]
}

senhas_administradores_biblioteca = {
    'senhas_administradores_gerais': ["3101", "2012", "0404"],
    'senha_supervisora_de_secao': [1703],
    'senha_supervisora_de_recebidos': [1708]
}

livros_cadastrados = []

utilizar_sistema = str(input('\nDeseja utilizar o sistema? \n1. SIM \n2. NÃO \n'))
utilizar_sistema.upper()

try:

    if utilizar_sistema.upper() == "SIM":

        quest_login_usuario = str(input('\nInforme seu nome de usuario: '))
        quest_login_usuario.upper()

        quest_senha_usuario = str(input('\nInforme sua senha de usuario: '))
        quest_senha_usuario.upper()


        quest_cadastrar_livros = str(input('\nDeseja cadastrar algum livro? \n1. SIM \n2. NÃO \n'))
        quest_cadastrar_livros.upper()

        if quest_cadastrar_livros.upper() == 'SIM':
                
            cadastro_livros = str(input('Insira um novo livro: '))
            livros_cadastrados.append(cadastro_livros)

        elif quest_cadastrar_livros.upper() == 'NÃO' or quest_cadastrar_livros.upper() == 'NAO':
            print(f'\nCerto, até a próxima!')

        else:
            print('Opção inválida, tente entrar novamente.')

        utilizar_sistema = str(input('Deseja continuar no sistema? \n'))
        utilizar_sistema.upper

    elif utilizar_sistema.upper() == 'NÃO' or utilizar_sistema.upper() == 'NAO':
        
        print(f'Perfeito, esta biblioteca tem {len(livros_cadastrados)} livro(s) \nSua biblioteca: {livros_cadastrados} ')

    else:
        print('Resposta inválida, reinicie o sistema.')

finally:

    exit()