frase = str(input('Escreva uma frase: '))
f1 = str('@')
frase = (f1+(frase.upper().strip()))
print('Vezes que as letras "a" ou "A" apareceram: {}'.format(frase.count('A')))
print('Primeira posição de a na string: {}'.format(frase.find('A')))
print('Ultima posição de a na string: {}'.format(frase.rfind('A')))

# Do Professor:
# frase = str(input('Escreva uma frase: ')).upper().strip()
# print('Vezes que as letras "a" ou "A" apareceram: {}'.format(frase.count('A')+1))
# print('Primeira posição de a na string: {}'.format(frase.find('A')+1))
# print('Ultima posição de a na string: {}'.format(frase.rfind('A')+1))