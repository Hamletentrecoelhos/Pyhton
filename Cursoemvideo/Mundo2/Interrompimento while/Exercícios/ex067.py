print("""Digite um número para saber sua tabuada;
E pressione "Enter" para reaizar a operação;
Para interromper o programa digite um número negativo.""")
while True:
    t = int(input('Número: '))
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{t} x {c} = {t*c}')
    print('-'*10)
print('Fim')
