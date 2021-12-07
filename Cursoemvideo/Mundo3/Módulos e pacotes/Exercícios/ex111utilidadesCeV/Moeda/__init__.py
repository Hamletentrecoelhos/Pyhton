def reais(d):
    """
    -> Formata float em R$.
    :param d: float a ser formatado.
    :return: float formatado.
    """
    return f'R${d:.2f}'.replace('.', ',')


def resumo(self, aum1, dim1):
    """
    -> Returna um resumo do resultado de operações com o self inserido.
    :param valor: self a qual será elaborado o resumo.
    :param aum1: % de aumento
    :param dim1: % de diminuição
    :return: devolve o resumo
    """
    print(f"""-----------------------------------------
            RESUMO DO VALOR
-----------------------------------------
{'Dividido por 2:':<25}{metade(valor)};
{'Multiplicado por dois:':<25}{duplicar(valor)};
{'Aumentado em 80%:':<25}{aumentar(valor, aum1)};
{'Diminuido em 35%:':<25}{diminuir(valor, dim1)}.
-----------------------------------------""")


def aumentar(self, aum, R=True):
    """
    -> Realiza um aumento em regra de três.
    :param R: formata em R$.
    :param valor: self a ser aumentado.
    :param aum: porcentagem a aumentar.
    :return: primeiro self aumentado pelo segundo self(%).
    """
    valor += (valor * aum) / 100
    return reais(valor) if R is True else valor

def diminuir(self, dim, R=True):
    """
    -> Realiza uma diminuição em regra de três.
    :param R: Formata em R$.
    :param valor: self a ser diminuido.
    :param dim: porcentagem a diminuir.
    :return: primeiro self diminuido pelo segundo self(%).
    """
    valor -= (valor * dim) / 100
    return reais(valor) if R is True else valor


def metade(self, R=True):
    """
    -> Divide o self recebido por dois.
    :param R: formata em R$.
    :param valor: self a ser dividido.
    :return: self dividido por dois.
    """
    valor /= 2
    return reais(valor) if R is True else valor


def duplicar(self, R=True):
    """
    -> Multiplicao self por dois.
    :param R: formata em R$.
    :param valor: self a ser multiplicado.
    :return: self multiplicado por dois.
    """
    valor *= 2
    return reais(valor) if R is True else valor
