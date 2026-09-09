primeiro_numero = float(input('Insira um número de sua preferência: '))
segundo_numero = float(input('Insira um número de sua preferência: '))

operacao_escolhida = int(input('Escolha uma operação digitando seu número:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potência\n'))

if operacao_escolhida == 1:

    resultado_soma = primeiro_numero + segundo_numero
    print(f'O resultado do seu cálculo é: {resultado_soma}')

elif operacao_escolhida == 2:

    resultado_subtracao = primeiro_numero - segundo_numero
    print(f'O resultado do seu cálculo é: {resultado_subtracao}')

elif operacao_escolhida == 3:

    resultado_multiplicacao = primeiro_numero * segundo_numero
    print(f'O resultado do seu cálculo é: {resultado_multiplicacao}')

elif operacao_escolhida == 4:

    if primeiro_numero and segundo_numero != 0:
        resultado_divisao = primeiro_numero / segundo_numero
        resto_divisao = primeiro_numero % segundo_numero
        print(f'O resultado do seu calculo é: {resultado_divisao}, e o resto deste cálculo é: {resto_divisao}')
    
    else:

        print('Resultado inválido, a divisão por zero nao é possível!')

elif operacao_escolhida == 5:

    resultado_potencia = primeiro_numero ** segundo_numero
    print(f'O resutado do seu calculo é: {resultado_potencia}')

else:
    print('Valor inserido é inválido, coloque outro valor.')




# O comando "is" pergunta: "É o mesmo objeto?" Exemplo: "if Felipe is Felipe:" -> Ai o codigo continua rodando normalmente.
# Já o comando "==" verifica se os valores são iguais "Os valores são iguais?" Exemplo: "if 5 == 5:" -> ai o codigo roda normalmente.