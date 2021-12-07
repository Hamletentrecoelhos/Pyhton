cont = f = int()
for formato in range(0, 4):
    if formato == 2:
        f = 4
    elif formato == 3:
        f = 7
    else:
        f = formato
    for cortx in range(29, 38):
        for corfundo in range(40, 49):
            cont += 1
            print(f'\033[m{cont:<3}: \!033[{f};{cortx};{corfundo}m = \033[{f};{cortx};{corfundo}mOlá Mundo! (^_^)')
print('\033[mTire o "!" (ponto de esclamação) do padrão ANSI para funcionar!')
