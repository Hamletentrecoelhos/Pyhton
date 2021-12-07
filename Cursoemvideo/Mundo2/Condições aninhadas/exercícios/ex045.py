from random import randrange
es = int(input("""JOGUE PEDRA, PAPEL E TESOURA
Digite 1 para Pedra
Digite 2 para Papel
Digite 3 para Tesoura
Digite aqui: """))
n1 = randrange(1, 3)
if n1 == 1 and es == 2:
    print('Você vencel! Computador escolheu pedra')
elif n1 == 1 and es == 3:
    print('Você perdeu! Computador escolheu pedra')
elif n1 == 2 and es == 1:
    print('Você perdeu! Computador escolheu papel')
elif n1 == 2 and es == 3:
    print('Você venceu! Computador escolheu papel')
elif n1 == 3 and es == 1:
    print('Você venceu! Computador escolheu tesoura')
elif n1 == 3 and es == 2:
    print('Você perdeu! Computador escolheu tesoura')
elif es != 1 and es != 2 and es != 3:
    print('Opsão digitada não registrada')
else:
    print('Empate')

