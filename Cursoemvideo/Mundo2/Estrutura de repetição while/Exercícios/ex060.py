print()
print('CALCULADORA DE  FATORIAL')
print()
n = int(input("""Você quer usar a estrutura de repetição "for" ou "while"?
Digite [1] para "for" e [2] para "while" e pressione "Enter". 
Digite aqui: """))
print()
if n == 1:
    f1 = int(input("""Entregue um número inteiro para saber seu fatoraial 
e pressione "Enter" em seguida. 
Digite aqui: """))
    print()
    fat = f1
    for c in range(f1 - 1, 0, -1):
        fat *= c
    print('Usando for: {}'.format(fat))
elif n == 2:
    f1 = float(input("""Entregue um número real para saber seu fatoraial 
e pressione "Enter" em seguida. 
Digite aqui: """))
    print()
    r = 1
    while f1 > 0:
        print('{}'.format(f1), end='')
        print(' x ' if f1 > 1 else ' = ', end='')
        r *= f1
        f1 -= 1
    print('{}'.format(r), end='')
else:
    print('Seleção inválida')


