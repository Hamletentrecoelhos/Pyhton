def fn(nu, show=False):
    """
    -> A função fn realiza o fatorial de
        um número positivo e inteiro.

    Ex: fn(5)
    >> 120

    Use a opção show=True para que
    o processo de fatoração também
    seja retornado.

    Ex: fn(5, Show=True)
    >> 5 x 4 x 3 x 2 x 1 = 120
    """
    tx = f'{nu} x '
    if show == False:
        for c in range(nu - 1, 0, -1):
            nu *= c
        return f'{nu}'
    elif show == True:
        for d in range(nu - 1, 0, -1):
            nu *= d
            if d > 1:
                tx += (f'{d} x ')
            else:
                tx += (f'{d} = {nu}')
        return tx
x = fn(nu=5, show=True)
print(x)

help(fn)
