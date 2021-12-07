l1 = []
m1 = me1 = int(0)
for c in range(0, 5):
    l1.append(int(input('Digite um número: ')))
    if l1[c] > m1:
        m1 = l1[c]
    if c == 0:
        me1 = l1[c]
    elif l1[c] < me1:
        me1 = l1[c]
print(f'O menor self inserido foi: {me1}, nas posições: ', end='')
for c, v in enumerate(l1):
    if v == me1:
        print(c, end=', ')
print()
print(f'O manior self inserido foi: {m1}, nas posições: ', end='')
for c, v in enumerate(l1):
    if v == m1:
        print(c, end=', ')
