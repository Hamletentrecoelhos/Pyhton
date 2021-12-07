n = str()
nu1 = int(input('Informe o primeiro valor: '))
nu2 = int(input('Informe o segundo valor: '))
while n != 'Sim':
    print()
    n = str(input("""Selecione o que fazer com os valores
1 para somar
2 para subitrair
3 para multiplicar
4 para dividir
5 para sair
Digite aqui: """))
    print()
    if n == '1':
        print(nu1 + nu2)
    elif n == '2':
        print(nu1 - nu2)
    elif n == '3':
        print(nu1 * nu2)
    elif n == '4':
        print(nu1 / nu2)
    elif n == '5':
        n = str('Sim')
    else:
        print('Resposta inválida, tente novamente')
print('Fim')
