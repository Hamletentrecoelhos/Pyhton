def verificanum(n=''):
    while not n.isnumeric():
        n = input(f' \033[1;31;48mErro: A idade "{n}" não é uma reposta válida! \n Tente novamente...\033[m \nIdade: ')
    return n


def verificatx(t='0'):
    if1 = True
    for c in t:
        if c.isnumeric():
            if1 = False
    if if1 == False:
        while if1 == False:
            if1 = True
            t = input(f' \033[1;31;48mErro: O nome "{t}" não é válido! \n Tente novamente...\033[m \nNome: ')
            for c in t:
                if c.isnumeric():
                    if1 = False
    t = ' '.join(t.split()).strip().title()
    return t


def verificaop(o):
    while o not in '123':
        o = input(f' \033[1;31;48mErro: Opição {o} invalálida! \n tente novamente... \n\033[1;33mSua opção:\033[m ')
    return int(o)
