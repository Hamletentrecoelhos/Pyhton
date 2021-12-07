l = input('Digite um expressão: ')
l1 = []
v = 0
for c in range(0, len(l)):
    l1.append(l[c])
    if l1.count(')') > l1.count('('):
        v = 1
    if c >= 3:
        if l1[c - 1] in '+*/%':
            if l1[c - 2] in ('+*/%.><-{[]}()'):
                v = 1
            elif l1[c] in ('+*/%.><-{[]}()'):
                v = 1
if l1.count('(') == l1.count(')') and v == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')