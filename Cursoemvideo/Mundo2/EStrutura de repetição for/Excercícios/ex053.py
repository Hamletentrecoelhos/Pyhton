frase = str(input('Escreva uma frase: ')).strip().upper().split()
frase = ''.join(frase)
f1 = frase[::-1]
print('É palindromo' if f1 == frase else 'Não é palindromo')

# Classic way:
# frase = str(input('Escreva uma frase: ')).strip().upper().split()
# frase = ''.join(frase)
# f1 = str('')
# for c in range(len(frase) - 1, -1, -1):
#     f1 += frase[c]
# print('É palindromo' if f1 == frase else 'Não é palindromo')
