nt1 = float(input('Digite a nota da P1: '))
nt2 = float(input('Digite a nota da p2: '))
if (nt1 + nt2) / 2 < 5:
    print('REPROVADO')
elif 5 <= ((nt1 + nt2) / 2) < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
