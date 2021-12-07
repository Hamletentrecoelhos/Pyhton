from random import randint
from operator import itemgetter
jogo = {'1': randint(1, 6),
        '2': randint(1, 6),
        '3': randint(1, 6),
        '4': randint(1, 6)}
print('Resultados de rolagem (d6):')
for k, v in jogo.items():
    print(f'>>> Jogador{k} tirou {v}.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print('== Ranking dos Jogadores ==')
for v, i in enumerate(ranking):
    print(f'Em {v+1}° lugar: jogador{i[0]} com {i[1]}.')
