from datetime import date
nm = input('Nome: ')
dn = int(input('Data de nascimento: '))
ct = int(input('N° do ctps: '))
p = {'idade': dn + date.today().year, 'nome': nm, 'ctps': ct}
ap = 0
if ct > 0:
    dc = int(input('Data de contratação: '))
    sl = float(input('Salário: '))
    if (dc - dn) + 35 > 65:
        ap = 65
        p['Contratação'] = dc
        p['Salário'] = sl
        p['Aposentadoria'] = ap
    else:
        ap = 35 + (dc - dn)
        p['Contratação'] = dc
        p['Salário'] = sl
        p['Aposentadoria'] = ap
for k, i in p.items():
    print(f'{k} tem o self {i}')
