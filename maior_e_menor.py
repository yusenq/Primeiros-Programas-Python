lista_numeros_escolhidos = []
quantidade_de_numeros = int(0)
quantidade_restante = int(5)

while quantidade_de_numeros <= 4:
    numeros_escolhidos = [float(input('\nInforme um número (limite de 5 números): \n'))]
    lista_numeros_escolhidos.append(numeros_escolhidos)
    quantidade_de_numeros = quantidade_de_numeros + 1
    quantidade_restante = quantidade_restante - 1
    print(f'\nVocê já escolheu {quantidade_de_numeros}, restam {quantidade_restante} \n')


print(f'Sua lista ficou assim: \n{lista_numeros_escolhidos}')
print(f'\nO maior número da sua lista é: \n{max(lista_numeros_escolhidos)}')
print(f'\nO menor número da sua lista é: \n{min(lista_numeros_escolhidos)}')