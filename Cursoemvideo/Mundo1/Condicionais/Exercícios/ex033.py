n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))


# My stupd way:

# n1 = float(input('Digite um número: '))
# n2 = float(input('Digite outro número: '))
# n3 = float(input('Digite mais um número: '))
# if n1 > n2 > n3:
#     print('O menor número é: {}'.format(n3))
#     print('O maior número é: {}'.format(n1))
# else:
#     if n2 > n1 > n3:
#         print('O menor número é: {}'.format(n3))
#         print('O maior número é: {}'.format(n2))
#     else:
#         if n3 > n2 > n1:
#             print('O menor número é: {}'.format(n1))
#             print('O maior número é: {}'.format(n3))
#         else:
#             if n1 > n3 > n2:
#                 print('O menor número é: {}'.format(n2))
#                 print('O maior número é: {}'.format(n1))
#             else:
#                 if n3 > n1 > n2:
#                     print('O menor número é: {}'.format(n2))
#                     print('O maior número é: {}'.format(n3))
#                 else:
#                     if n2 > n3 > n1:
#                         print('O menor número é: {}'.format(n1))
#                         print('O maior número é: {}'.format(n2))


