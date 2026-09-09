nota_media_minima = float(input('Insira aqui a nota mínima permitida: '))
nome_aluno = str(input('Insira o nome do aluno: '))


nota_primeiro_semestre = float(input(f'Insira a média do aluno {nome_aluno} no primeiro semestre: '))
nota_segundo_semestre = float(input(f'Insira a média do aluno {nome_aluno} no segundo semestre: '))
media_geral_aluno = (nota_primeiro_semestre + nota_segundo_semestre) / 2

if media_geral_aluno < nota_media_minima:

    print(f'O(a) aluno(a) {nome_aluno} teve {media_geral_aluno} como nota final. \nPor isso, o(a) aluno(a) está REPROVADO(A)!')

elif media_geral_aluno >= nota_media_minima:

    print(f'O(a) aluno(a) {nome_aluno} teve {media_geral_aluno} como nota final. \nPor isso, o(a) aluno(a) está APROVADO(A)!')

else:
    print('O valores informados, são inválidos!')