l1 = []
m = me = 0
while True:
    p = []
    p.append(input('Nome: '))
    p.append(int(input('Peso (Kg): ')))
    l1.append(p[:])
    if p[1] > m:
        m = p[1]
    if len(l1) == 1:
        me = p[1]
    elif p[1] < me:
        me = p[1]
    s = input('Deseja continuar? [S/N]: ')
    if s in 'nN':
        break
print(f'Você inseriu {len(l1)} pessoas.')
print(f'O maior peso registrado foi {m}, por: ', end='')
for c in l1:
    if c[1] == m:
        print(c[0], end='.. ')
print()
print(f'O menor peso registrado foi {me}, por: ', end='')
for c in l1:
    if c[1] == me:
        print(c[0], end='.. ')


