print('Suas medidas podem formar um triangulo?')
la = float(input('Digite o tamanho do lado A: '))
lb = float(input('Digite o tamanho do lado B: '))
lc = float(input('Digite o tamanho do lado C: '))
if lb - lc < la < lb + lc and la - lc < lb < la + lc and la - lb < lc < la + lb:
    print('Isso forma um triângulo')
else:
    print('Isso não forma um triâgulo')