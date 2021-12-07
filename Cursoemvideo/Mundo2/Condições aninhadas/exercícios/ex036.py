print('\033[1:31m<'*2, 'Compre sua casa com um imprestimo', '>'*2, '\033[m')
print('\033[1:31:40mx|'*19 + 'x\033[m')
casa = float(input('\033[0::40mDigite o valor da casa: '))
salario = float(input('Digite o valor líquido do seu salártio: '))
anos = int(input('Em quantos anos: '))
casa = (casa / anos) / 12
if casa < ((salario * 30) / 100):
    print('Total do contrato: {} parcelas de R$ \033[:31:40m{:.2f}\033[m'.format(12*anos, casa))
else:
    print("""\033[0:31:40mOferta não pode ser aceita, pois o valor\033[m 
\033[0:31:40mda casa excede 30% o do seu salário.     \033[m""")
    print('\033[1:31:40mx|' * 19 + 'x\033[m')
