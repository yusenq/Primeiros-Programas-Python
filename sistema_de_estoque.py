quantia_iphones_13_em_estoque = []
serial_iphones_13_em_estoque = []

quantia_iphones_14_em_estoque = []
serial_iphones_14_em_estoque = []

quantia_iphones_15_em_estoque = []
serial_iphones_15_em_estoque = []

quantia_iphones_16_em_estoque = []
serial_iphones_16_em_estoque = []

quantia_iphones_17_em_estoque = []
serial_iphones_17_em_estoque = []

quantia_iphones_18_em_estoque = []
serial_iphones_18_em_estoque = []

nome_administradores_estoque = ("felipe")
senha_administradores_estoque = int(3101)

tentativa_login_estoque = str(input('Informe seu nome de usuario: '))
tentativa_senha_estoque = int(input('\nInforme sua senha para login: '))

if tentativa_login_estoque != nome_administradores_estoque and tentativa_senha_estoque != senha_administradores_estoque:
    print('\nEste usuario não tem acesso ao estoque!')
    exit

else:
    print('\nBem vindo ao sistema de estoque!')

    acao_escolha = str(input('\nEscolha oque deseja fazer: \n1. Inserir um Produto \n2. Alterar um Produto  \n3. Excluir um Produto'))
    acao_escolha.upper()

    if acao_escolha.upper() == "INSERIR" or acao_escolha.upper() == '1':
        categoria_produto_recebido = str(input('\nInsira a categoria do produto recebido: \n1. Iphone 13 \n2. Iphone 14 \n3. Iphone 15 \n4. Iphone 16 \n5. Iphone 17 \n6. Iphone 18'))
        categoria_produto_recebido.upper()
        
        if categoria_produto_recebido.upper() == "1" or categoria_produto_recebido.upper() == "IPHONE 13":
            quantidade_produto_recebido = int(input('Insira quantos produtos desta categoria foram recebidos: '))
            serial_produto_recebido = str(input('\nInsira o número de série do produto recebido: '))
            quantia_iphones_13_em_estoque.append(quantidade_produto_recebido)
            serial_iphones_13_em_estoque.append(serial_produto_recebido)

            print('O produto foi inserido com sucesso no estoque!')


        elif categoria_produto_recebido.upper() == "2" or categoria_produto_recebido.upper() == "IPHONE 14":
            quantidade_produto_recebido = int(input('Insira quantos produtos desta categoria foram recebidos: '))
            serial_produto_recebido = str(input('\nInsira o número de série do produto recebido: '))

    elif acao_escolha.upper() == "ALTERAR" or acao_escolha.upper() == '2':