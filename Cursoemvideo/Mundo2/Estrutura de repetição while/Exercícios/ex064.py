m = float()
c = int()
print("""SOMA NÚMEROS
Digite números continuamente para acrescentar ao montante
ou digite 999 para terminar e obter o resultado""")
print()
n = float(input('Digite um número: '))
while n != 999:
    m += n
    c += 1
    n = float(input('Digite um número: '))
print('Total: {}; vezes: {}'.format(m, c))










