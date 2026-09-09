numero_inicial = int(input('Informe o número inicial de sua contagem: '))
numero_final = int(input('Informe o número final de sua contagem: '))
print('Sua sequência ficou assim: \n')

for numero_inicial in range (numero_final):

    contagem = numero_inicial + 1
    print(f'{contagem}')