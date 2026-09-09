import random

nome_usuario = str(input('Olá jogador, primeiro insira seu nome para que seja cadastrado: '))
quantidade_de_tentativas = (1)

print('\nAgora irei explicar o jogo à você: \nSeguinte, nesse jogo eu vou escolher um número totalmente aleatorio de 1 a 100, e você tem q ir dando palpites para tentar descobrir qual número é este. \nLógico que, para te ajudar, a cada palpite seu irei dar uma dica, no caso, irei falar se o número é maior ou menor. \n')
numero_aleatorio = random.randrange(1, 101)
numero_escolhido = int(input(f'{nome_usuario}, escolha um número para seu palpite: '))

while numero_aleatorio != numero_escolhido:

    quantidade_de_tentativas = quantidade_de_tentativas + 1
    
    if numero_aleatorio > numero_escolhido:
        print('Dica: Este número é pequeno, talvez um maior?')

    elif numero_aleatorio < numero_escolhido:
        print('Dica: Este número é muito grande, talvez um menor?')

    numero_escolhido = int(input(f'{nome_usuario}, escolha um novo número para seu palpite: '))

print(f'\nParabéns!!! \nVocê acertou o número em apenas {quantidade_de_tentativas} tentativas!')