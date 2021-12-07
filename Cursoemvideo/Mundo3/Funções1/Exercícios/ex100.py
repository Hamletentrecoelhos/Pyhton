from random import randint

def sorteia5(s):
    print('Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        s.append(randint(1, 9))
        print(s[c], end=' ')
    print('.')

def somap(list):
    sp = 0
    for c in list:
        if c % 2 == 0:
            sp += c
    list.append(sp)
    print(f'Somando os valores pares de {B[:5]}, temos {B[5]}.')

B = []
sorteia5(B)
somap(B)
