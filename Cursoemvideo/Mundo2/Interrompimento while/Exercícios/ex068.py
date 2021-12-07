from random import randint
print('JOGUE PAR OU ÍMPAR')
print()
v = 0
while True:
    n = int(input('Escolha um valor: '))
    p = str(input('Digite "I" para ímpar e "P" para par: ')).upper().strip()
    np = randint(1, 2)
    print('=-' * 20)
    if p == 'P':
        if (n + np) % 2 == 0:
            v += 1
        else:
            break
    elif p == 'I':
        if (n + np) % 2 != 0:
            v += 1
        else:
            break
    else:
        print('Resposta inválida')
        print('=-' * 20)
print(f'Você venceu {v} vezes' if v > 0 else 'Você não veceu nenhuma vez')

