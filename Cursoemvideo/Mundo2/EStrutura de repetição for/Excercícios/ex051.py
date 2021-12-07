n = int(input('Digite a razão da progressão: '))
d = int(input('Digite o primeiro termo da progressão: '))
for c in range(d, d + n * 10, n):
    print('{} '.format(c), end=' -> ')
print('FIM')
