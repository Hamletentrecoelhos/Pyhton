forma = int(input("""Escolha sua forma de pagamento
Digite 1 para dinheiro
Digite 2 para cheque
Digite 3 para 1x no cartão
Digite 4 para 2x no cartão
Digite 5 para 3x no cartão
Digite aqui: """))
pr = float(input('Infrome o valor do produto: '))
if forma == 1 or 2 and 0 > forma < 3:
    print('Preço = R$ {:.2f}'.format(pr * 0.9))
elif forma == 3:
    print('Preço = R$ {:.2f}'.format(pr * 0.95))
elif forma == 4:
    print('Preço = R$ {:.2f}'.format(pr))
elif forma == 5:
    print('Preço = R$ {:.2f}'.format(pr * 1.2))
else:
    print('Opição não registrada')
