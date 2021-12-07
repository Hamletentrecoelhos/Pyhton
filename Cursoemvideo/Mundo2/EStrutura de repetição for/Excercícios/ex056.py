idadem = int(0)
idadef = int(0)
nomevelho = ''
m = int(0)
for c in range(1, 5):
    print('______ {}° Pessoa ______'.format(c))
    n = str(input('Digite o nome da pessoa: ')).strip()
    na1 = str(input('Sexo [M/F]: ')).strip()
    na2 = int(input('Digite a idade da pessoa: '))
    if na1 in 'Mm' and na2 > idadem:
        idadem = na2
        nomevelho = n
    elif na1 in 'Ff' and na2 < 20:
        idadef += 1
    m += na2

print("""
Média da idade: {};
O homem mais velho possui {} anos;
{} mulher(es) são menores que 20 anos.""".format(m / 4, idadem, idadef))
