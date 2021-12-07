nme = c = n = str()
me = t = p = float()
pma = int()
while True:
    print('=-' * 10)
    print('INSIRA UM PRODUTO')
    print('-|' * 10)
    n = str(input('Nome: ')).strip()
    p = float(input('Preço: '))
    while True:
        print('--' * 15)
        c = str(input('Deseja continuar? [S/N]: ')).upper().strip()
        if c in 'SN':
            break
        else:
            print(f'>>> {c} não é uma resposta válida')
    t += p
    if p > 1000:
        pma += 1
    if me == 0:
        me = p
        nme = n
    elif p < me:
        me = p
        nme = n
    if c == 'N':
        break
print('==' * 15)
print(f"""Total da compra: R${t:.2};
{pma} produtos custam mais que R$ 1000,00;
O produto mais barato foi "{nme}".""")
