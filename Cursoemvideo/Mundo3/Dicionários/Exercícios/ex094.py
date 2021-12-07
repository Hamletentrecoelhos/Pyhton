l1 = []
cid = iff = count = 0
while True:
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo [M/F/O]: ').strip()
        if sexo.upper() not in 'MFO':
            print(f'Resposta {sexo} inválida.')
        else:
            break
    p = {'Nome': nome, 'Idade': idade, 'Sexo': sexo}
    l1.append(p.copy())
    while True:
        s = input('Deseja continuar? [S/N]: ').strip()
        if s.upper() not in 'SN':
            print(f'Resposta {s} inválida.')
        else:
            break
    cid += idade
    if sexo in 'Ff':
        iff += 1
    if s in 'nN':
        break
print(f"""O grupo tem {len(l1)} pessoas;
A média de idade é {cid / len(l1):.2f};""")
if iff > 0:
    print('As mulheres cadastradas foram: ', end='')
    for c in (l1):
        if c['Sexo'] in 'Ff':
            count += 1
            if count < iff:
                print(c['Nome'], end=', ')
            else:
                print(f"{c['Nome']}.")
print()
print('Lista de pessoas acima da média: ')
for c1 in l1:
    if c1['Idade'] > cid / len(l1):
        count = 0
        for k, v in c1.items():
            count += 1
            if count < len(c1.keys()):
                print(f'{k} = {v}', end='; ')
            else:
                print(f'{k} = {v}.')

print()
print('Fim')
