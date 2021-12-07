n = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito',
     'dezenove', 'vinte')
print('Saiba como escrever um número de 1 a 20 por extenço')
while True:
    r = int(input('Digite aqui: '))
    if 0 < r < 21:
        print('-*' * 15)
        print(f'Você digitou o número {n[r - 1]}')
        print('-*' * 15)
        break
    print('Digite um número entre 1 e 20')
print('Fim do programa')
