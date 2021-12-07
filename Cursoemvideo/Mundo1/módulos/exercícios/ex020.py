from random import shuffle
Cores = {'Amarelo': '\033[:33m', 'Magenta': '\033[:35m', 'Limpar': '\033[m'}
print(Cores['Magenta'])
n1 = str(input("Digite o nome do 1° aluno: "))
n2 = str(input("Digite o nome do 2° aluno: "))
n3 = str(input("Digite o nome do 3° aluno: "))
n4 = str(input("Digite o nome do 4° aluno: "))
print(Cores['Limpar'])
lista = [n1, n2, n3, n4]
shuffle(lista)
print(Cores['Amarelo'], lista, Cores['Limpar'])
