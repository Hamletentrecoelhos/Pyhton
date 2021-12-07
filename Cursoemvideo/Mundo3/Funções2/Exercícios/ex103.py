def ficha(n='<desconhecido>', g='0'):
    if n.strip() == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    elif g[0] == int():
        g = int(g)
    return f'O jogador {n} fez {g} gol(s).'
f = ficha(n=input('Nome do jogador: '), g=input('N° de gol(s): '))
print(f)
