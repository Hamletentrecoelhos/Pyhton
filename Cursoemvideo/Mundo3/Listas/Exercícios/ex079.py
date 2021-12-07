l1 = []
while True:
    l = int(input('Digite um número: '))
    if l not in l1:
        l1.append(l)
        print('Número adicionado com sucesso...')
    else:
        print('Número repetido, não pode ser adiconado...')
    c = str(input('Deseja continuar? [S/N]: '))
    if c.upper() == 'N':
        break
l1.sort()
print(l1)
