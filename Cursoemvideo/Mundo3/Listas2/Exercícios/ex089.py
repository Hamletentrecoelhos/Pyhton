ls = []
while True:
    n = input('Nome: ')
    p1 = int(input('P1: '))
    p2 = int(input('P2: '))
    ls.append([n, [p1, p2]])
    s = input('Deseja continuar? [S/N]: ')
    if s in 'nM':
        break
print(f'{"N°":<4}{"Nome:":<10}{"Média":>8}')
for c in range(0, len(ls)):
    print(f'{c:<4}{ls[c][0]:<10}{(ls[c][1][0] + ls[c][1][1]) / 2:>8.1f}')
print()
print('Digite "999" para encerrar.')
while True:
    c = int(input('Digite o n° de um aluno para saber suas notas: '))
    if c == 999:
        break
    print(f'{ls[c]}')
print('Programa encerrado.')
