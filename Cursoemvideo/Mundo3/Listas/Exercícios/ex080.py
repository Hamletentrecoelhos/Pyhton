l1 = []
for c in range(0, 5):
    l = int(input('Digite um valor: '))
    if c == 0 or l > l1[-1]:
        l1.append(l)
        print(f'O número {l} foi colocado na última posição.')
    else:
        for d in range(0, len(l1)):
            if l <= l1[d]:
                l1.insert(d, l)
                print(f'O número {l} foi colocado na {d + 1}° posição.')
                break
print(l1)
