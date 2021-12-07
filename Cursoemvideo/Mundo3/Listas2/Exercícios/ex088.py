from random import randrange
print('='*34)
print('8'*5, 'NÚMEROS PARA MEGASSENA', '8'*5)
print('='*34)
print()
n = int(input('Quantos jogos você quer que sejam sorteados?  '))
print('-'*34)
lista = []
for c in range(0, n):
    jg = []
    d = 0
    while d < 6:
        v = randrange(1, 61)
        if v not in jg:
            jg.append(v)
            d += 1
    jg.sort()
    lista.append(jg)
    print(f'Jogo {c + 1: <4}: {lista[c]}')
print('='*34)
print(' '*12, 'Boa sorte!')
print('='*34)
