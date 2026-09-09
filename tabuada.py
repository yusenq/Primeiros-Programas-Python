numero_escolhido = int(input('Informe o número e descubra a tabuada toda dele: '))
limite_tabuada = int(input('Informa também, até qual número a tabuada irá: '))
for multiplicador in range (limite_tabuada + 1):

    print(f"{numero_escolhido} x {multiplicador} = {numero_escolhido * multiplicador}")