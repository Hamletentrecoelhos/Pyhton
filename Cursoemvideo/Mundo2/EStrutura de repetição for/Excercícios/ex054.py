acima = 0
for c in range(1, 8):
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    if idade < 21:
        acima += 1
print('Há {} maiores e {} menores'.format(7 - acima, acima))
