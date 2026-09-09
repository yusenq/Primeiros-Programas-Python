quantia_de_numeros = int(input('Informe quantos números quer inserir: '))

lista_numeros_escolhidos = []

for contador in range (quantia_de_numeros):

    valores_inseridos = int(input('Informe os valores que desejam ser inseridos: '))
    lista_numeros_escolhidos.append(valores_inseridos)

sum(lista_numeros_escolhidos)
media_geral = sum(lista_numeros_escolhidos) / quantia_de_numeros


print(f'Os números inseridos são: {lista_numeros_escolhidos}')
print(f'\nA média de todos os números escolhidos é: {media_geral}')
print(f'\nO tamanho da sua lista é: {len(lista_numeros_escolhidos)} \nA somatória total da sua lista é: {sum(lista_numeros_escolhidos)}')


#Conhecendo a função "sum" muita coisa ficou mais facil, esta função literalmente soma valores agregados ou ja pré-disostos em uma lista.