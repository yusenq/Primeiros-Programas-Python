cadastro_nome = str(input('Cadastre seu nome de usuario: '))
cadastro_senha = str(input('Cadastre uma senha: '))
tentativa_senha = str(input('Digite a senha que você criou: '))
numero_de_tentativas = 0

while cadastro_senha != tentativa_senha and numero_de_tentativas < 5:
        numero_de_tentativas = numero_de_tentativas + 1
        print(f'Esta é sua tentativa de número {numero_de_tentativas}, você tem 5 tentativas, para acertar.')
        print('\nSENHA INCORRETA! Tente novamente!')
        tentativa_senha = str(input('Digite a senha que você criou: '))

if numero_de_tentativas > 4:

        print('Você extrapolou o número de tentativas, tente mais tarde!')


else:

    print(f'Bem vindo(a) {cadastro_nome}!')