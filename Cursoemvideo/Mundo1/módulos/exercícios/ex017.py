from math import sqrt
print('\033[1:32m!'*7, 'Hipotenusa', '!'*7, '\033[m')
print('\033[1:35m<>|<>'*5, '\033[m')
hnum1 = float(input("Digite o cateto adjacente: "))
hnum2 = float(input("Digite o cateto oposto:    "))
print('A hipotenusa é: \033[4:32m{}\033[m'.format(sqrt((hnum1*hnum1)+(hnum2*hnum2))))
print('\033[1:35m<>|<>'*5, '\033[m')
