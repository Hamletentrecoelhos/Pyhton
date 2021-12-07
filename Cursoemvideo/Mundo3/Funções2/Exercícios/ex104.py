def leiaint(n):
    if n.isnumeric():
        n = int(n)
    else:
        while True:
            print('\033[;31mErro! Digite um número inteiro.\033[m')
            n = input('Digite um n° inteiro: ')
            if n.isnumeric():
                n = int(n)
                break
    print(f'Você digitou o número {n}')
    return n
leiaint(input('Digite um n°: '))
