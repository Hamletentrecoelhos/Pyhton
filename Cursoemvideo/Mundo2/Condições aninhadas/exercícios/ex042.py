print('Suas medidas podem formar um triangulo?')
la = float(input('Digite o tamanho do lado A: '))
lb = float(input('Digite o tamanho do lado B: '))
lc = float(input('Digite o tamanho do lado C: '))
if lb - lc < la < lb + lc and la - lc < lb < la + lc and la - lb < lc < la + lb:
    print('Isso forma um triângulo')
    if la == lb == lc == la:
        print('E ele é Equilátero')
    elif la == lb or lb == lc or la == lc:
        print('E ele é Isósceles')
    else:
        print('E ele é Escaleno')
else:
    print('Isso não forma um triâgulo')
