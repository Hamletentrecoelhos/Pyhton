print('Descubra se o número é primo')
primo = int(input('Digite um número inteiro: '))
n = int(0)
for c in range(1, primo+1):
    if primo % c != 0:
        n += 1
        print('\033[:31m{}\033[m'.format(n), end=' ')
    else:
        print('\033[:33m{}\033[m'.format(c), end=' ')
if n == primo - 2:
    print('\033[:33mÉ PRIMO\033[m')
else:
    print('\033[:31mNÃO É PRIMO\033[m')
