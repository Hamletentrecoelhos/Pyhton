print('ATENÇÃO: Sempre pressione "Enter" após digitar em uma opsção')
r = float(input('Digite a razão da progreção: '))
p = float(input('Digite o ponto de partida: '))
v = int(input('Digite em quantas vezes você quer que o padrão se repita: '))
d = p
t = str()
while p < (v * r + d) and t != '1':
    print(p)
    p += r
    if p == (v * r + d):
        print()
        t = str(input("""Digite 1 para sair
e 2 para adicionar 
mais vezes à progreção.
Digite aqui: """))
        if t == '2':
            print()
            v += int(input("""Quantas vezes a mais?
Digite aqui: """))
print('Foram {} termos, e o resultado foi {}'.format(v, p))
