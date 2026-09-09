nome_usuario = str(input('Informe seu nome: '))
idade_usuario = int(input('Informe sua idade apenas com números: '))

if idade_usuario <= 3:
    
    print(f'Parabéns! \nCom {idade_usuario} anos, você ({nome_usuario}) já é um bebê!')

elif idade_usuario > 3 and idade_usuario <= 9:

    print(f'Parabéns! \nCom {idade_usuario} anos, você ({nome_usuario}) já é uma criança!')

elif idade_usuario > 9 and idade_usuario <= 14:

    print(f'Parabéns! \nCom {idade_usuario} anos, você ({nome_usuario}) já é Pré-Adolescente!')

elif idade_usuario > 14 and idade_usuario <= 18:

    print(f'Parabéns! \nCom {idade_usuario} anos, você ({nome_usuario}) já é Adolescente!')

elif idade_usuario > 18 and idade_usuario <= 25:

    print(f'Parabéns! \nCom {idade_usuario} anos, você ({nome_usuario}) já é Jovem-Adulto(a)!')

elif idade_usuario > 25 and idade_usuario <= 60:

    print(f"Parabéns! \nCom {idade_usuario} anos, você ({nome_usuario}) já é um(a) Adulto(a) consolidado(a)!")

elif idade_usuario > 60 and idade_usuario <= 99:

    print(f'Parabéns! \nCom {idade_usuario} anos, você ({nome_usuario}) já é um(a) Idoso(a)!')

elif idade_usuario > 99:

        print(f'Parabéns, acredite ou não, mas você ({nome_usuario}), faz parte agora de 0,0073% da população mundial, você ({nome_usuario}), é um(a) gurreiro(a)da vida!')

else:
     print('Idade inválida inserida, favor inserir uma idade válida!')