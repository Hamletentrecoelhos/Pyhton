c1 = l3 = int(0)
x = ((int(input('Digite um número: ')), int(input('Digite outro número: ')),
      int(input('Digite outro número: ')), int(input('Digite mais um número: '))))
print('O valores pares digitados foram: ', end='')
for c in range(0, 4):
    if x[c] == 3:
        l3 += 1
    if x[c] % 2 == 0:
        print(x[c], end='')
print()
print(f"""O self 9 apareceu {x.count(9)} vezes;
Vezes que o self 3 foi digitado: {l3};""")
