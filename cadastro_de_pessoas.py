login_admin = ('isalinda')
senha_admin = ('0111')

usuarios_cadastrados = []
senhas_cadastradas = []

cadastrar_usuarios = str(input('Olá usuário, já tem cadastro? \n'))
cadastrar_usuarios.upper()


if cadastrar_usuarios.upper() == "SIM" or cadastrar_usuarios.upper() == "TENHO":
    nome_usuario_cadastrado = str(input('\nCerto, insira aqui seu nome de usuário: '))
    senha_usuario_cadastrado = str(input('\nAgora, insira aqui a senha da sua conta: '))
    
    if nome_usuario_cadastrado == login_admin and senha_usuario_cadastrado == senha_admin:
        print('Bem vindo(a), Admin!')

    else:

        if nome_usuario_cadastrado in usuarios_cadastrados and senha_usuario_cadastrado in senhas_cadastradas:
            print(f'Bem vindo(a), {nome_usuario_cadastrado}!')

        else:
            print(f'ERRO! O usuario ou a senha estão inválidas!')

elif cadastrar_usuarios.upper() == 'NÃO' or cadastrar_usuarios.upper() == 'NAO':
    req_cadastro_de_usuario = str(input('\nInforme um nome de usuário par seu cadastro: '))

    if req_cadastro_de_usuario in usuarios_cadastrados:
        
        print(f'\nEste nome de usuário é inválido, insira outro!')
        req_cadastro_de_usuario = str(input('\nInforme um nome de usuário para seu cadastro: '))
        usuarios_cadastrados.append(req_cadastro_de_usuario)

    else:
        usuarios_cadastrados.append(req_cadastro_de_usuario)
        req_cadastro_de_senhas = str(input('\nInforme uma senha para seu cadastro: '))
        senhas_cadastradas.append(req_cadastro_de_senhas)

    if req_cadastro_de_usuario in usuarios_cadastrados and req_cadastro_de_senhas in senhas_cadastradas:
        print(f'Bem vindo(a), {req_cadastro_de_usuario}!')

    else:
        print(f'ERRO! O usuario ou a senha estão inválidas!')

