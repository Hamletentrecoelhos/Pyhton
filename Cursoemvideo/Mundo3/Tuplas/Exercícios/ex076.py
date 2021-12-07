ls = 'pão de forma', 7, 'Geleia de uva', 12, 'ovo', 10, 'leite', 4, 'farinha', 7
for c in range(1, len(ls), 2):
    print(f'{ls[c - 1]:.<30}R$ {ls[c]:.2f}')
