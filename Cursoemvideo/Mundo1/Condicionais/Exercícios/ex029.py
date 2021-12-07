print('Calculadora de multa')
n1 = float(input('Digite a velociadade registrada: '))
if n1 > 80:
    print('Veículo {:.2f} Km acíma da velocidade'.format(n1-80))
    print('Multa de R$ {:.2f}'.format((n1-80)*7))
else:
    print('Veículo abaixo do limite de velocidade')
