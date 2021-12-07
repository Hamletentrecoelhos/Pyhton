lt = []
tg = 0
while True:
    no = input('Nome: ')
    p = int(input('N° de partidas: '))
    if p > tg:
        tg = p
    p1 = []
    tot = 0
    for c in range(1, p + 1):
        kk = int(input(f'N° número de gols na {c}° partida: '))
        p1.append(kk)
        tot += kk
    dj = {'Nome': no, 'Gols': p1, 'Total': tot}
    lt.append(dj.copy())
    s = input('Deseja continuar? [S/N]: ')
    if s in 'nN':
        break
print(f'{"Cod:":<3}|{"nome":<10}{"Gols":<{tg * 3}}{"|Total":>8}')
for c, v in enumerate(lt):
    print(f'{c}{"|":>4}{v["Nome"]:<10}|{v["Gols"]}{" ":<{(tg * 3 - len(v["Gols"])*3) + 1}} {v["Total"]}')
print("""Digite o Cod. do jogador para saber seus dados."
Ou digite "999" para parar.""")
while True:
    je = int(input('Cod.: '))
    if je == 999:
        break
    if je < len(lt) > -1:
        for k, v in lt[je].items():
            print(f'O campo {k} tem o self: {v}')
        print(f'O jogador {lt[je]["Nome"]} jogou {len(lt[je]["Gols"])}')
        for c in range(1, len(lt[je]["Gols"]) + 1):
            print(f'=> Na {c}° partida fez {lt[je]["Gols"][c - 1]}.')
        print(f'Foi um total de {tot} gols')
    else:
        print('Resposta inválida!')
print('Programa finalizado')