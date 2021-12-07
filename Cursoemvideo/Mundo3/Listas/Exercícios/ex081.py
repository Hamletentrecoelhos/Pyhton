l1 = []
while True:
    l1.append(int(input('Digite um número: ')))
    s = input('Deseja continuar? [S/N]: ')
    if s.upper() == 'N':
        break
l1.sort(reverse=True)
print(f"""O número de itens inseridos foi: {len(l1)};
Que resultam na seguinte lista: {l1};
O número 5 está na lista: {5 in l1}.""")
