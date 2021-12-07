def voto(n=2000):
    from datetime import date
    a = date.today().year
    if 16 > a - n < 18 or a - n > 100:
        return f'No ano {a} seu voto é: opcional'
    elif 100 > a - n > 17:
        return f'No ano {a} seu voto é: Obrigatório'
    else:
        return f'No ano {a} seu voto é: Negado'
print(voto(2000))
