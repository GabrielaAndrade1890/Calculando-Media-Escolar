print()
print('CALCULANDO MÉDIA ESCOLAR')
print('==========================')

nome_aluno = input('Diga seu nome: ')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))

media = ((nota1 + nota2 + nota3 + nota4)/4)

print()

if media == 10.0:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Excelente💙')
elif media >= 9.5:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Excelente💙')
elif media >= 8.5:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Bom💚')
elif media >= 7.5:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Bom💚')
elif media >= 6.5:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Bom💚')
elif media >= 5.5:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Critico💛')
elif media >= 4.5:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Critico💛')
else:
    print(f'{nome_aluno.title()}, sua média foi {media}')
    print('Seu desempenho escolar foi: Ruim💔')

print()