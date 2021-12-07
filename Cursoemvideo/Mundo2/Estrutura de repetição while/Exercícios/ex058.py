from random import choice
from time import sleep
m1 = str('Pedra')
m2 = str('Papel')
m3 = str('Tesoura')
q = int()
f = int()
n1 = choice([m1, m2, m3])
while q != 1:
    sx = str(input("""Digite 1 para pedra
Digite 2 para papel
Digite 3 para tesoura
Digite aqui: """))
    f = f + 1
    if n1+sx == "Pedra2" or n1+sx == "Papel3" or n1+sx == "Tesoura1":
        print()
        sleep(0.5)
        print('JÔ')
        sleep(0.5)
        print('QUEM')
        sleep(0.5)
        print('PÔ!')
        print()
        q = 1
        print('Você venceu! Computador escolheu {}'.format(n1))
        if f == 1:
            print('DE PRIMEIRA!')
        else:
            print('Com {} tentativas'.format(f))
    elif n1+sx == 'Pedra3' or n1+sx == 'Papel1' or n1+sx == 'Tesoura2':
        print()
        sleep(0.5)
        print('JÔ')
        sleep(0.5)
        print('QUEM')
        sleep(0.5)
        print('PÔ!')
        print()
        print('Computador escolheu {} você perdeu tente novamente'.format(n1))
        print('=' * 20)
    elif sx != '1' and sx != '2' and sx != '3':
        print('Resposta inválida, tente novamente')
        print('=' * 20)
    else:
        print()
        sleep(0.5)
        print('JÔ')
        sleep(0.5)
        print('QUEM')
        sleep(0.5)
        print('PÔ!')
        print()
        print('Computador escolheu {} o que resultou em empate, tente novamente'.format(n1))
        print('=' * 20)
