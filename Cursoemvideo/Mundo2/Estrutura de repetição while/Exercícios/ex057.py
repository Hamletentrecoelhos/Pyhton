sx = ''
while sx not in 'MFO':
    sx = str(input('Digite o sexo [M/F/O]: ')).strip().upper()[0]
print('Sexo {} redistrado.'.format(sx))




# My way:
# sx = ''
# while sx != 'M' and sx != 'm' and sx != 'F' and sx != 'f' and sx != 'O' and sx != 'o':
#     sx = str(input('Digite o sexo [M, F, O]: '))
