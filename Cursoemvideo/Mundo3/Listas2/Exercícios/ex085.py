l1 = [[], []]
for c in range(0, 7):
    l = int(input(f'Digite o {c + 1}° número: '))
    if l % 2 == 0:
        l1[0].append(l)
    else:
        l1[1].append(l)
l1[0].sort()
l1[1].sort()
print(f"""Lista completa: {l1};
Apenas pares: {l1[0]};
Apenas ímpares: {l1[1]}.""")
