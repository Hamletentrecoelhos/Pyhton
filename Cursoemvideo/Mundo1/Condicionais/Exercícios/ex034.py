print('CALCULE O AUMENTO DE SALÁRIO')
n1 = float(input('Digite o salário do funcionário: '))
print('O aumento do salário será de R$ {}'.format((n1*15)/100) if n1 < 1250.00 else 'O aumento do salário será de R$ {}'.format((n1*10)/100))
