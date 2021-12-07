no1 = str(input('Digite um nome: '))
print('Nome maiúsculo: {}'.format(no1.upper()))
print('Nome minúculo: {}'.format(no1.lower()))
no1 = no1.strip().split()
n1 = int('-'.join(no1).count('-'))
print('Número de letras no nome: {}'.format((len(no1))))
print('O primeiro nome é {} e o número de letras é: {}'.format(no1[0], len(no1[0])))

##Do professor:

# no1 = str(input('Digite um nome: ')).strip
# print('Nome maiúsculo: {}'.format(no1.upper()))
# print('Nome minúculo: {}'.format(no1.lower()))
# print('Número de letras no nome: {}'.format((len(no1)))-no1.cont(' ')
# no1 = no1.split()
# print('O primeiro nome é {} e o número de letras é: {}'.format(no1[0], len(no1[0])))