print('CALCULE SUA VIAGEM')
print('='*18)
km = float(input('Digite quantos quilómetros o trejeto possui: '))
print('O preço da sua passagem será: R$ {:.2f}'.format(km * 0.50) if km <= 200 else 'O preço da sua passagem será: {:.2f}'.format(km * 0.40))

