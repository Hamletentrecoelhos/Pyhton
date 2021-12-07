es = int(input("""CONVERSOR
Digite 1 para converter de decimal para binário
Digite 2 para converter de decimal para hexa
Digite 3 para converter de decimal para octal
Digite aqui: """))
n1 = int(input('Digite um número inteiro para a conversão: '))
if es == 1:
    print('{} convertido para binário é {}'.format(n1, bin(n1)[2:]))
elif es == 2:
    print('{} convertido para binário é {}'.format(n1, hex(n1)[2:]))
elif es == 3:
    print('{} convertido para binário é {}'.format(n1, oct(n1)[2:]))
else:
    print('Opção inválida')
