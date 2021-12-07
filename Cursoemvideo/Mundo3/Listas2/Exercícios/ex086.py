mtx = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for d in range(0, 3):
        mtx[c][d] = int(input(f'Digite o n° da posição [{c}, {d}]: '))
for c in range(0, 3):
    print()
    for d in range(0, 3):
        print(f'[{mtx[c][d]: ^5}]', end='')
