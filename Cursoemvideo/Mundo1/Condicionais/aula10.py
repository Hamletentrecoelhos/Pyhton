nome = str(input('Digite seu nome: ')).title().strip()

# Condição simplificada:
print('Bem vindo de volta {}'.format(nome) if nome == 'Tainam' else 'Não te conheço, saia desse sistema!')

# Comdição somples:
if nome == 'Tainam':
    print('Bem vindo de volta {}'.format(nome))

# Comdição composta:
if nome == 'Tainam':
    print('Bem vindo de volta {}'.format(nome))
else:
    print('Não te conheço, saia desse sistema!')
