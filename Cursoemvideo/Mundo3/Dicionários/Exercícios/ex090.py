aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = int(input('Média: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Rreprovado'
elif aluno['Média'] > 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Recuperação'
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
