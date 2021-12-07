from time import sleep
def contar(i, f, p):
    yc = int(0)
    if f < i:
        f -= int(1)
        if p > 0:
            p = int(p - p * 2)
        elif p == 0:
            p = int(-1)
    elif f > i:
        f += int(1)
        if p < 0:
            p = int(p * -1)//1
    if p == 0:
        p = int(1)
    print(f'A contagem de {i} até {f - 1 if f >= 0 else f + 1} de {p} em {p} é:')
    for c in range(i, f, p):
        if c < f - 1 and p > 0:
            sleep(0.2)
            print(f'{c}, ', end='', flush=True)
        elif c > f + 2 and p < 0:
            print(f'{c}, ', end='', flush=True)
            sleep(0.2)
        else:
            sleep(0.2)
            print(f'{c}.', flush=True)
        yc += int(1)
    print(f"{'=-' * (yc * 2)}<>" if (yc * 2) > 34 else f'{"=-" * 18}<>')
contar(1, 11, 1)
contar(10, -1, -2)
print("""Agora tente você:
Ps! só use número inteiros (e pode usar negativos).""")
contar(i=int(input('De: ')), f=int(input('Até: ')), p=int(input('Em: ')))
