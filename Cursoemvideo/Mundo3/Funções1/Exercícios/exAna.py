from time import sleep
c = 0
while True:
    sleep(2)
    c += 1
    if c > 2:
        c = 0
    if c % 2 == 0:
        print('S2 ANA ROMEIRO')
    else:
        print('ANA ROMEIRO GOSTOSA')
