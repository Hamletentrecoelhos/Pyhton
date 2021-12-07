mtx = []
con = sp = s3c = m2l = 0
for c in range(0, 3):
    for d in range(0, 3):
        l1 = []
        l1.append(int(input(f'Digite o n° da posição [{c}, {d}]: ')))
        mtx.append(l1[:])
        if l1[0] % 2 == 0:
            sp += l1[0]
        if d == 2:
            s3c += l1[0]
        if c == 1 and l1[0] > m2l:
            m2l = l1[0]
for c in range(0, 3):
    print()
    for d in range(0, 3):
        print(mtx[con], end=' ')
        con += 1
print()
print(f"""A soma dos números pares é: {sp};
A soma dos números da terceira coluna foi: {s3c};
O maior número da segunda linha foi: {m2l}.""")
