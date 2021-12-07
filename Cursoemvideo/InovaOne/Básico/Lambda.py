funcao_anonima = lambda a, b: a + b
print(funcao_anonima(3, 6))

pacote_anonimo = {
    'soma': lambda a, b: a + b,
    'subitração': lambda a, b: a - b,
    'multiplicação': lambda a, b: a * b,
    'Divisão': lambda a, b: a / b,
}

print(pacote_anonimo['multiplicação'](4, 8))

qualquer = pacote_anonimo['Divisão']
print(qualquer(200, 56))
