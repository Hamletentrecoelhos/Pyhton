from time import sleep
def cc(v1):
    v2 = 0
    if v1[0] >= 10:
        while v1[0] >= 10:
            v1[0] //= 10
            v2 += 1
        v2 += 1
    else:
        v2 += 1
    v1[0] = v2
def maior(* pop):
    m = 0
    l = 0
    # comtagem para o layout:
    l0 = [len(pop)]
    cc(l0)
    # ----------------------
    for c, v in enumerate(pop):
        if v > m:
            m = v
        print(v, end=' ', flush=True)
        sleep(0.2)
        # comtagem para o layout:
        v1 = [v]
        cc(v1)
        l += v1[0] + 1
        # ----------------------
    # comtagem para o layout:
    m1 = [m]
    cc(m1)
    # ----------------------
    c = (f"""foram digitados {len(pop)} valores; |
O maior self foi {m}.{'|':>{(l + 8 + l0[0]) - m1[0]}}""")
    print(c)
    print(f'{"-" * (l + 26 + l0[0])}')
maior(1, 2, 3, 4, 5, 6)
maior(4, 6, 90, 10)
maior(13, 32, 100, 54, 0)
