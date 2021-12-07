print('SAQUE ELETRÔNICO')
t = v = int(input('Digite o valor do saque: '))
c = 50
cc = 0
print(f'{v} será dividido em: ')
while True:
    if t >= c:
        cc = t // c
        t %= c
    else:
        if cc > 0:
            print(f'{cc} em notas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        cc = 0
        if t == 0:
            break

# My way:
#c50 = c20 = c10 = c1 = int()
#v = int(input('Quanto: '))
#t = v
#while True:
#    if v >= 50:
#        v -= 50
#        c50 += 1
#    elif 50 > v >= 20:
#        v -= 20
#        c20 += 1
#    elif 20 > v >= 10:
#        v -= 10
#        c10 += 1
#    elif 10 > v >= 1:
#        v -= 1
#        c1 += 1
#   if v == 0:
#        break
#print(f"""R${t} em notas será:
#{c50} notas de R$50;
#{c20} notas de R$20;
#{c10} notas de R$10;
#{c1} notas de R$1""")
