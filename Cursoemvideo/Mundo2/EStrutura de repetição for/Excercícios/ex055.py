p1 = int(0)
p2 = int(0)
for c in range(1, 6):
    peso = int(input('Digite o peso da {}° pessoa em kilogramas: '.format(c)))
    if peso < p1 or p1 == 0:
        p1 = peso
    elif peso > p2:
        p2 = peso
print('O menor peso foi {} kg e o maior peso foi {} kg'.format(p1, p2))
