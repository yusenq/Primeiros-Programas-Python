marcas_em_estoque = ['FORD', 'CHEVROLET', 'FIAT', 'VOLKSWAGEN']
placas_em_estoque = []
carros_ford_em_estoque = []
carros_chevrolet_em_estoque = []
carros_fiat_em_estoque = []
carros_volkswagen_em_estoque = []

nome_proprietario = str(input('Cadastre o seu nome: '))
senha_proprietario = input('\nCadastre uma senha: ')

def login_usuario():
    nome_login_usuario = str(input('\nInsira o seu nome: '))
    senha_login_usuario = str(input('\nInsira sua senha: '))

    if nome_login_usuario == nome_proprietario and senha_login_usuario == senha_proprietario:
        print(f'Bem vindo, {nome_proprietario}!')

    while nome_login_usuario != nome_proprietario or senha_login_usuario != senha_proprietario:
        quest_tentativa_login = str(input(f'Sinto muito, mas este login é inválido. \nDeseja fazer login novamente? '))
        quest_tentativa_login.upper()

        if quest_tentativa_login.upper() == 'SIM':
            nome_login_usuario = str(input('\nInsira seu nome: '))
            senha_login_usuario = str(input('\nInsira sua senha: '))

        elif quest_tentativa_login.upper == 'NÃO' or quest_tentativa_login.upper() == 'NAO':
            print('Certo, até mais!')
            exit()
        
login_usuario()
quest_cadastro = str(input('\nDeseja cadastrar um novo carro no estoque?\n'))
quest_cadastro.upper()

if quest_cadastro.upper() == 'SIM':

    cadastro_marca_para_estoque = str(input('\nInforme a marca do carro que irá cadastrar: '))
    cadastro_marca_para_estoque.upper()
    
    if cadastro_marca_para_estoque in marcas_em_estoque:
        print('\nMarca cadastrada!')

    

    while cadastro_marca_para_estoque.upper() not in marcas_em_estoque:
        quest_cadastrar_nova_marca = str(input('\nEstá marca não está dentro do nosso sistema ainda, deseja adicionar? \n'))
        quest_cadastrar_nova_marca.upper()
        
        if quest_cadastrar_nova_marca.upper() == 'SIM':
            marcas_em_estoque.append(cadastro_marca_para_estoque)

        elif quest_cadastrar_nova_marca.upper() == 'NÃO' or quest_cadastrar_nova_marca.upper() == 'NAO':

            print(f'\nOk, a marca "{cadastro_marca_para_estoque}" não será cadastrada!')

    cadastro_placa_para_estoque = str(input('\nInforme a placa do carro que deseja cadastrar: '))
    cadastro_placa_para_estoque.upper()
    
    while cadastro_placa_para_estoque.upper() in placas_em_estoque:
        print('\nEsta placa já está cadastrada em seu estoque, tente novamente!')

        cadastro_placa_para_estoque = str(input('\nInforme a placa do carro que deseja cadastrar: '))
        cadastro_placa_para_estoque.upper()

    placas_em_estoque.append(cadastro_placa_para_estoque.upper())

    cadastro_carro_para_estoque = str(input('\nInforme o carro que deseja cadastrar: '))
    cadastro_carro_para_estoque.upper()

    informacoes_carro_para_estoque = (cadastro_carro_para_estoque.upper(), cadastro_placa_para_estoque.upper())

    if cadastro_marca_para_estoque.upper() == 'FORD':
        carros_ford_em_estoque.append(informacoes_carro_para_estoque)

    elif cadastro_marca_para_estoque.upper() == 'CHEVROLET':
        carros_chevrolet_em_estoque.append(informacoes_carro_para_estoque)

    elif cadastro_marca_para_estoque.upper() == 'FIAT':
        carros_fiat_em_estoque.append(informacoes_carro_para_estoque)

    elif cadastro_marca_para_estoque.upper() == 'VOLKSWAGEN':
        carros_volkswagen_em_estoque.append(informacoes_carro_para_estoque)

    
    print(f'Seu cadastro está assim: \nMarcas: {marcas_em_estoque} \nPlacas: {placas_em_estoque} \nCarros da Ford: {carros_ford_em_estoque} \nCarros da Chevrolet: {carros_chevrolet_em_estoque} \nCarros da Fiat: {carros_fiat_em_estoque} \nCarros da Volkswagen: {carros_volkswagen_em_estoque}')

elif quest_cadastro.upper() == 'NÃO' or quest_cadastro.upper() == 'NAO':
    print(f'Certo, obrigado pelo acesso!')
    exit()


#adicionar bd
