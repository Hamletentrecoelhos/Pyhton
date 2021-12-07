m = float()
c = int()
print("""SOMA NÚMEROS
Digite números continuamente para acrescentar ao montante
ou digite 999 para terminar e obter o resultado""")
print()
while True:
    n = float(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    m += n
print('Total: {}; vezes: {}'.format(m, c))
