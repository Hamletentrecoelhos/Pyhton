v = int(input('Digite quantas vezes: '))
c = 0
n = 0
n2 = 0
n3 = 0
while c < v:
    c += 1
    print(n)
    n3 = n + n2
    n2 = n
    n = n3
    if n == 0:
        n = c
