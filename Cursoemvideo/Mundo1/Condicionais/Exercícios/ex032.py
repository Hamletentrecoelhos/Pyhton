from datetime import date
ano = int(input('Digite um ano e saiba se ele é bissexto (ou digite zero para utilizar o ano atual): '))
if ano == 0:
    ano = date.today().year
print('O ano {} é bissexto'.format(ano) if ano % 4 == 0 and (ano // 100) % 4 == 0 else 'O ano {} não é bissexto'.format(ano))

# Fórmula do professor (achei a minha melhor)
# print('É bissexto' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'Não é Bissexto')
