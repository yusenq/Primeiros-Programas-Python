oficinas_mecanicas = {
    'auto_mecanica_duteco': [],
    'oficina_mecanica_araraquara': [],
    'auto_mecanica_7s': []
}

medicos_publicos = {
    'doutor_evaristo_costa': [],
    'doutor_marcelo_jose': []
}

mercados_regionais = {
    'semprevale_supermercado': [],
    'supermercado_jau': []
}

nome_usuario = str(input('Olá usuário, informe seu nome!'))
nome_usuario.upper()

escolha_lista = str(input('\nPara onde deseja ligar? \n1. Oficinas Mecânicas \n2. Médicos Públicos \n3. Mercados Regionais'))
escolha_lista.upper()

if escolha_lista.upper() == '1' or escolha_lista.upper() == 'OFICINAS MECANICAS' or escolha_lista.upper() == 'OFICINAS MECÂNICAS':

    ligacao_desejada_oficinas = int(input(f'\nCerto, {nome_usuario} informe para qual oficina deseja ligar: \n1. auto_mecanica_duteco \n2. oficina_mecanica_araraquara \n3. auto_mecanica_7s'))
    if ligacao_desejada_oficinas == '1':
        print(f'\nOlá, tudo bem? \nAqui é da auto_mecanica_duteco -> {oficinas_mecanicas["auto_mecanica_duteco"][0]}, oque deseja?')
        exit()

    elif ligacao_desejada_oficinas == '2':
        print(f'\nOlá, tudo bem? \nAqui é da oficina_mecanica_araraquara -> {oficinas_mecanicas['oficina_mecanica_araraquara'][0]}, oque deseja?')
        exit()

    elif ligacao_desejada_oficinas == '3':
        print(f'\nOlá, tudo bem? \nAqui é da auto_mecanica_7s -> {oficinas_mecanicas['auto_mecanica_7s'][0]}, oque deseja?')
        exit()

    else:
        print(f'\n{nome_usuario}, esta resposta é inválida, reinicie o sistema!')
        exit()

elif escolha_lista.upper() == '2' or escolha_lista.upper() == 'MÉDICOS PÚBLICOS' or escolha_lista.upper() == ' MEDICOS PUBLICOS':
    ligacao_desejada_medicos = int(input(f'Certo, {nome_usuario} informe para qual médico deseja ligar: \n1. doutor_evaristo_costa \n2. doutor_marcelo_jose'))
    if ligacao_desejada_medicos == '1':
        print(f'\nOlá, tudo bem? \nDoutor Evaristo Costa, em que posso te ajudar?')
        exit()

    elif ligacao_desejada_medicos == '2':
        print(f'\nOlá, tudo bem? \nDoutor Marcelo José, em que posso te ajudar?')

    else:
        print(f'\n{nome_usuario}, esta resposta é inválida, reinicie o sistema!')

elif escolha_lista.upper() == '3' or escolha_lista.upper() == 'MERCADOS REGIONAIS':
    ligacao_desejada_mercados = int(input(f'\nCerto, {nome_usuario} informe para qual mercado deseja ligar: \n1. semprevale_supermercado \n2. supermercado_jau'))
    if ligacao_desejada_mercados == '1':
        print(f'\nOlá, aqui é do Sempre Vale Supermercado, oque deseja comprar hoje?')

    elif ligacao_desejada_mercados == '2':
        print(f'\nOlá aqui é do Super Mercado Jaú, oque deseja pedir?')

    else:
        print(f'\n{nome_usuario}, esta resposta é inválida, reinicie o sistema!')

    