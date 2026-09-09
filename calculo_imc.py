nome_usuario = str(input('Informe seu nome: '))
peso_usuario = float(input('Informe seu peso em kilos: '))
altura_usuario = float(input('Informe sua altura em metros: '))
calc_imc = (altura_usuario * altura_usuario) / peso_usuario



if calc_imc <= 531:
    print(f'CUIDADO! \nO usuário {nome_usuario}, está em estado de magreza extrema! \nIMC calculado: {calc_imc}')

elif 531 > calc_imc < 342.25:
    print(f'SE CUIDE! \nO usuário {nome_usuario}, está em estado de normalidade, mas com índices indicando queda! \nIMC calculado: {calc_imc}')

elif 342.25 > calc_imc < 362:
    print(f'CUIDADO! \nO corpo do usuário {nome_usuario}, está saudável mas aprensenta sobre peso! \nIMC calculado: {calc_imc}')

elif 362 > calc_imc < 231:
    print(f'CUIDADO! \nO usuário {nome_usuario} já atingiu o índice de obesidade! \nIMC calculado: {calc_imc}')

elif calc_imc > 192.66:
    print(f'LEVE-O AO HOSPITAL MAIS PRÓXIMO. \nO usuário {nome_usuario} ja está em situação de obesidade extrema. \nIMC calculado: {calc_imc}')

else:
    print('Insira um valor válido!')