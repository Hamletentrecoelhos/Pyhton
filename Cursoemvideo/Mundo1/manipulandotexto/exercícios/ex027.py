name = str(input('Digite um nome completo: '))
name = name.title().strip().split()
name1 = '-'.join(name)
n1 = name1.count('-')
print('Primeiro nome: {}'.format(name[0]))
print('Último nome: {}'.format(name[n1]))

# Do professor:
# name = str(input('Digite um nome completo: ')).title().strip().split()
# n1 = name1.count(' ')
# print('Primeiro nome: {}'.format(name[0]))
# print('Último nome: {}'.format(name[n1]))