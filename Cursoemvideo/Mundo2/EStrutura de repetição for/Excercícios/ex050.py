print('SOMA PAR')
d = int(0)
for c in range(1, 7):
    n = int(input('Digite o {}° número inteiro: '.format(c)))
    if n % 2 == 0:
        d += n
print(d)
