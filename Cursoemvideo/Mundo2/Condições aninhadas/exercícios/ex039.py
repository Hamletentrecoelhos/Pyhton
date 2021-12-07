idade = int(input('Informe sua idade cidadão: '))
if 17 <= idade <= 23:
    print('Está na hora de se alistar')
elif idade < 17:
    print('Faltam {} anos para você poder se alistar'.format(17 - idade))
else:
    print('É tarde demais para se alistar {} anos se passaram'.format(idade - 23))
