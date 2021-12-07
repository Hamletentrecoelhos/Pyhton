conjunto1 = {1, 2, 3, 3, 3, 3, 5} #Todos os números três essedentes (após o primeiro número três), serão eliminados
conjunto1.add(4)
conjunto1.discard(5)
print(f'Adicionando e descartando valores: {conjunto1}')
print(f'Tipo: {type(conjunto1)}')
conjunto2 = {5, 7, 9, 100}
print(f'Unindo conjunto2 ao conjunto1: {conjunto1.union(conjunto2)}')
print(f'Puxando os valores que se repetem entre conjunto1 e conjunt2: {conjunto1.intersection(conjunto2)}')
print(f'Entregando os valores de conjunto1 que não estão em conjunt2: {conjunto1.difference(conjunto2)}')
print(f'Entregando valores diferentes de forma cimétrica: {conjunto1.symmetric_difference(conjunto2)}')
print(f'Verificando se todos os elementos de conjunto1 então em conjunto2: {conjunto1.issubset(conjunto2)}')
print(f'verifica se todos os elementos de conjunto2 então em conjunto1: {conjunto1.issuperset(conjunto2)}')
