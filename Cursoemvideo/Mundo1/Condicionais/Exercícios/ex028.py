from random import randrange
print('='*5, 'JOGUE ADIVINHA', '='*5)
print('-'*11, '*', '-'*11)
n1 = int(input('Digite um número de 0 à 5: '))
n2 = randrange(0, 5)
print('Você está sem sorte, quem sabe na próxima' if n1 != n2 else 'Você acertou o número! Ps: Isso não te dá nenhum mérito, foi pura sorte')
