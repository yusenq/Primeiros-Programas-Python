print('Olá Professor(a)!')

alunos = str(input('Insira o nome de seus alunos aqui: '))
lista_alunos = [alunos]


for aluno in lista_alunos:

    nota_primeiro_semestre = float(input(f'Insira aqui a nota do Primeiro Semestre do Aluno "{aluno}": '))
    nota_segundo_semestre = float(input(f'Insira aqui a nota do Segundo Semestre do Aluno {aluno}: '))
    media_notas = (nota_primeiro_semestre + nota_segundo_semestre) / 2
    print(f'A Média Final do Aluno "{aluno}" é: {media_notas}')