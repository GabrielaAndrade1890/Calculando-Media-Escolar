print('CALCULANDO MÉDIA ESCOLAR')
print('==========================')

nome_aluno = input('Diga seu nome: ')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))

media = ((nota1 + nota2 + nota3 + nota4)/4)

print(f'{nome_aluno.title()}, sua média foi {media}')

# testando breach nova, teste teste