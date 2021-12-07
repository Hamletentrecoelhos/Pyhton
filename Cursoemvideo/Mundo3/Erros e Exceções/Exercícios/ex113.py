f = float()
i = int()
while True:
    try:
        f = float(input('\033[0:32:40mDigite um número real: \033[m'))
    except ValueError:
        print('\033[0:31mErro:: digite um número real válido!\033[m')
    except KeyboardInterrupt:
        print('O usuário não queis digitar o número real = 0.')
        f = 0
        break
    else:
        break
while True:
    try:
        i = int(input('\033[0:33:40mDigite um número inteiro: \033[m'))
    except ValueError:
        print('\033[0:31mErro:: digite um número inteiro válido!\033[m')
    except KeyboardInterrupt:
        print('O usuário não queis digitar o número inteiro = 0.')
        i = 0
        break
    else:
        break
print(f'\033[0:35:40mVocê digitou o número inteiro {i} e o número real {f}...\033[m')
