l1 = []
lp = []
li = []
while True:
    l1.append(int(input('Digite um número: ')))
    s = input('Deseja continuar? [S/N]: ')
    if s.upper() == 'N':
        break
for c, v in enumerate(l1):
    if v % 2 == 0:
        lp.append(v)
    else:
        li.append(v)
print(f'lp: {lp}')
print(f'li: {li}')
print(f'l1: {l1}')
