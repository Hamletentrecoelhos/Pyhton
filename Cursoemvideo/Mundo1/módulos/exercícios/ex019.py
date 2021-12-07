from random import choice
print('\033[1:31m|°|'*9, '\033[:30m')
n1 = str(input("Digite o nome do 1° aluno: "))
n2 = str(input("Digite o nome do 2° aluno: "))
n3 = str(input("Digite o nome do 3° aluno: "))
n4 = str(input("Digite o nome do 4° aluno: "))
print('\033[:31m|o|'*9, '\033[m')
print('\033[:31m='*24, '>', choice([n1, n2, n3, n4]), '\033[m')
