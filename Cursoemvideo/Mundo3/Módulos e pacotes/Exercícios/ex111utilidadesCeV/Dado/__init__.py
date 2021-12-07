def valfl(i):
    """
    -> retorna input até que o usuário digite um valor que possa
    ser transformado em float.
    :param i: valor a ser testado.
    :return: o valor em float ou input("tente novamente").
    """
    while True:
        i = str(i.replace(',', '.'))
        lo = i.find('.')
        if (i[:lo].isnumeric() and i[lo+1:].isnumeric()) or i.isnumeric():
            break
        i = input('Resposta inválida tente novamente: ')
    return float(i)
