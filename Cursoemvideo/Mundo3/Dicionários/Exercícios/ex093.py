dj = {}
dj['Nome'] = input('Nome: ')
p = int(input('N° de partidas: '))
p1 = []
for c in range(1, p + 1):
    p1.append(int(input(f'N° número de gols na {c}° partida: ')))
dj['Gols'] = p1[:]
dj['Total'] = sum(p1)
print(dj)
for k, v in dj.items():
    print(f'O campo {k} tem o self: {v}')
print(f'O jogador {dj["Nome"]} jogou {len(dj["Gols"])} vezes:')
for c in range(1, len(dj["Gols"]) + 1):
    print(f'=> Na {c}° partida fez {dj["Gols"][c - 1]}.')
print(f'Num um total de {dj["Total"]} gols')
