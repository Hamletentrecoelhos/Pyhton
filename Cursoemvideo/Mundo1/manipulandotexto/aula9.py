from random import shuffle
frase = str((input('Escreva uma frase: ')))
frase.strip()
frase1 = frase
frase2 = frase
print("""Usando comenados para mudar as partes 
das estrings que serão utilizadas:""")
print('Usando [9]: {}'.format(frase[9]))
print('Usando [9:13]: {}'.format(frase[9:13]))
print('Usando [9:13:12]: {}'.format(frase[9:13:2]))
print('Usando [9]: {}'.format(frase[:5]))
print('Usando [9]: {}'.format(frase[15:]))
print('Usando [9]: {}'.format(frase[9::3]))
print('Usando comandos para modificar a string:')
print('O número de caracteres na frase é {}'.format(len(frase)))
print('usando upper: {}'.format(frase.upper()))
print('Usando capitalige: {}'.format(frase.capitalize()))
print('Usando title: {}'.format(frase.title()))
print('Usando lower: {}'.format(frase.lower()))
frase.split()


print('Mudando caracteres entre as palavras (usando join para juntar novamente com caractere): {}'.format('-'.join(frase.split())))
print('Usando replace: {}'.format(frase2.replace('a', '4')))
print('Exist a "tu" in the frase: {}'.format(frase1.find("tu")))



