nome_admin_cadastrados = ['felipe', 'isadora']
senha_admin_cadastrados = ['admin', 'admin']

cadastro_usuario = str(input('Você já tem cadastro? \n'))
cadastro_usuario.upper()


def exclusao_de_itens_carrinho():

    excluir_itens_do_carrinho = str(input('Você deseja excluir algum item de seu carrinho?'))
    excluir_itens_do_carrinho.upper()

    if excluir_itens_do_carrinho.upper() == 'SIM':
        item_escolhido_para_excluir = str(input('Qual item deseja excluir do carrinho? \n'))
        itens_adicionados_no_carrinho.remove(item_escolhido_para_excluir)

        print(f'Certo, agora sua lista está assim: {itens_adicionados_no_carrinho}.')

        quest_adicionar_novo_item = str(input('Você quer adicionar outro item ao carrinho? \n'))
        quest_adicionar_novo_item.upper()

        if quest_adicionar_novo_item.upper() == "SIM":
            while quantidade_de_itens_adicionados <= 4:
                print('Você pode adicionar apenas 5 (cinco) itens ao carrinho!\n')
                itens_para_carrinho = str(input('\nDigite os itens que deseja colocar no carrinho: '))
            
                quantidade_de_itens_adicionados = quantidade_de_itens_adicionados + 1
                print(f'\nO usuário {cadastro_nome_usuario} tem {quantidade_de_itens_adicionados} itens adicionados ao carrinho!')
                itens_adicionados_no_carrinho.append(itens_para_carrinho)

    elif excluir_itens_do_carrinho.upper() == "NÃO" or excluir_itens_do_carrinho.upper() == "NAO":
        print(f'\nO carrinho {nome_carrinho} ficou assim: {itens_adicionados_no_carrinho}!')

def login_carrinho_admin():
    nome_carrinho = str(input('Agora crie um nome para seu carrinho: '))
                    
    itens_para_carrinho = str()
    quantidade_de_itens_adicionados = (0)
    itens_adicionados_no_carrinho = []
    
    while quantidade_de_itens_adicionados <= 4:
        print('Você pode adicionar apenas 5 (cinco) itens ao carrinho!\n')
        itens_para_carrinho = str(input('\nDigite os itens que deseja colocar no carrinho: '))
    
        quantidade_de_itens_adicionados = quantidade_de_itens_adicionados + 1
        print(f'\nSeu carrinho tem {quantidade_de_itens_adicionados} itens adicionados ao carrinho!')
        itens_adicionados_no_carrinho.append(itens_para_carrinho)
                    
        print(f'\nO carrinho {nome_carrinho} ficou assim: {itens_adicionados_no_carrinho}!')

if cadastro_usuario.upper() == 'NÃO' or cadastro_usuario.upper() == 'NAO':
    cadastro_nome_usuario = str(input('Crie seu nome de usuario: '))
    cadastro_senha_usuario = str(input('Crie uma senha de 8 digitos contendo números e letras: '))

    if len(cadastro_senha_usuario) == 8:
        tentativa_nome_usuario = str(input('\nInforme aqui o nome de usuario criado: '))
        tentativa_senha_usuario = str(input('\nInforme aqui a senha criada: '))

    elif len(cadastro_senha_usuario) != 8:
        print('está senha é inválida, a senha deve conter 8(oito) dígito.')
        exit()
        

        while tentativa_nome_usuario != cadastro_nome_usuario or tentativa_senha_usuario != cadastro_senha_usuario:
                print(f'O nome de usuario ou login estão errados. \nTente novamente!')
                tentativa_nome_usuario = str(input('\nInforme aqui o nome de usuario criado: '))
                tentativa_senha_usuario = str(input('\nInforme aqui a senha criada: '))

        if tentativa_nome_usuario == cadastro_nome_usuario and tentativa_senha_usuario == cadastro_senha_usuario:
            nome_carrinho = str(input('Agora crie um nome para seu carrinho: '))
                
            itens_para_carrinho = str()
            quantidade_de_itens_adicionados = (0)
            itens_adicionados_no_carrinho = []

        
            while quantidade_de_itens_adicionados <= 4:
                print('Você pode adicionar apenas 5 (cinco) itens ao carrinho!\n')
                itens_para_carrinho = str(input('\nDigite os itens que deseja colocar no carrinho: '))

                quantidade_de_itens_adicionados = quantidade_de_itens_adicionados + 1
                print(f'\nO usuário {cadastro_nome_usuario} tem {quantidade_de_itens_adicionados} itens adicionados ao carrinho!')
                itens_adicionados_no_carrinho.append(itens_para_carrinho)

            print(f'\nO carrinho {nome_carrinho} ficou assim: {itens_adicionados_no_carrinho}!')

elif cadastro_usuario.upper() == "SIM":
    tentativa_nome_admin = str(input('\nInforme aqui o nome de usuario criado: '))
    tentativa_senha_admin = str(input('\nInforme aqui a senha criada: '))
    
    if tentativa_nome_admin not in nome_admin_cadastrados and tentativa_senha_admin not in senha_admin_cadastrados:
        print('está senha é inválida, a senha deve conter 8(oito) dígito.')
        exit()         

login_carrinho_admin()