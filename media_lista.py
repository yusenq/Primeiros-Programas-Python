lista_de_numeros = []
quantidade_numeros = int(0)
total_de_escolhas = (5)

while quantidade_numeros <= 4:
    quest_escolha_numeros = float(input('Informe um número de sua escolha (Limite de 5 números): \n'))
    quantidade_numeros = quantidade_numeros + 1
    escolhas_restantes = total_de_escolhas - quantidade_numeros
    print(f'\nBoa escolha, faltam {escolhas_restantes} \n')

    lista_de_numeros.append(quest_escolha_numeros)

somatoria = sum(lista_de_numeros)
media_geral = sum(lista_de_numeros) / len(lista_de_numeros)
numeros_acima_media = []

print(f'\nParabéns, sua lista é: \n{lista_de_numeros}')
print(f'\nA soma total de sua lista é: \n{somatoria}')
print(f'\nA media geral de sua lista é: \n{media_geral}')

for numeros in lista_de_numeros:
    if numeros > media_geral:
        numeros_acima_media.append(numeros)

print(f'{numeros_acima_media}')


#Tive muita dificuldade para reconhecer o uso do FOR para selecionar os números maiores que a média dentro da lista.