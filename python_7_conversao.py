pais_usuario = str(input('Insira aqui o país onde você mora: '))
pais_usuario_upper = pais_usuario.upper()

paises_fahrenheit = ['ESTADOS UNIDOS', 'BELIZE', 'BAHAMAS', 'ILHAS CAYMAN', 'PALAU', 'ILHAS MARSHALL', 'MIANMAR', 'LIBÉRIA']


if pais_usuario_upper in paises_fahrenheit: 
    temp_fahrenheit = float(input('Insira aqui a temperatura atual: '))
    temp_celsius = (temp_fahrenheit - 32) / 1.8
    print(f'A temperatura atual em Celsius é: {temp_celsius}')

else:
    temp_celsius = float(input('Insira aqui a temperatura atual: '))
    temp_fahrenheit = temp_celsius * 1.8 + 32
    print(f'A temperatura atual em Fahrenheit é: {temp_fahrenheit}')


