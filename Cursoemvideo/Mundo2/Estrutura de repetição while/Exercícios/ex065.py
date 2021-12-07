n = str()
c = int()
co = int()
m = float()
maior = float()
menor = float()
print("""MÉDIA DOS NÚMEROS
Digite números continuamente para acrescentar ao montante.
ou digite N para encerar a tarefa e obter a média.
Sempre pressione "Enter" após digitar.""")
print()
while n != 'N':
    m = float(input('Digite um valor: '))
    c += m
    co += 1
    print(co)
    n = str(input('Selecione se deseja/não deseja continuar [S/N]: ')).upper().strip()
    if m > maior:
        maior = m
    if m < menor:
        menor = m
    if co == 1:
        menor = m
print('Média: {}; maior valor: {}; menor valor: {}'.format(c / co, maior, menor))
