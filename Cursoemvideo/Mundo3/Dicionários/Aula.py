from random import randint
print('Rolagem dos jogadores:')
jg = {}
for c in range(0, 4):
    jg[f'{c}'] = randint(1, 6)
    print(f'O jogador {c} tirou: {jg[f"{c}"]}')
l1 = []
l1.append(jg.copy())
print(l1[0])
