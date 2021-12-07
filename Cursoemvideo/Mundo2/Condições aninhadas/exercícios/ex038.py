n1 = int(input('Digite um número inteiro: '))
n2 = int(input('DIgite outro número inteiro: '))
if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n2 < n1:
    print('O número {} é maior que o número {}'.format(n2, n1))
else:
    print('O número {} é igual ao número {}'.format(n1, n2))
