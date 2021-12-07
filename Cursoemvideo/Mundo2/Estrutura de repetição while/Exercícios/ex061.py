r = float(input('Digite a razão da progreção: '))
p = float(input('Digite o ponto de partida: '))
v = int(input('Digite em quantas vezes você quer que o padrão se repita: '))
d = p
while p < (v * r + d):
    print(p)
    p += r
