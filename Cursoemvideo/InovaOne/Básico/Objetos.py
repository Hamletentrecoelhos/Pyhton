class Dump:
    def __init__(self, valor, aum1=1, dim1=1):
        self.valor = valor
        self.aum1 = aum1
        self.dim1 = dim1

    def reais(self):
        d = self
        """
        -> Formata float em R$.
        :param d: float a ser formatado.
        :return: float formatado.
        """
        d = str(f'R${d:.2f}')
        return d.replace('.', ',') #Por alguma razão essa classe não aceita devolver str :[

    def resumo(self):
        """
        -> Returna um resumo do resultado de operações com o valor inserido.
        :param self: valor a qual será elaborado o resumo.
        :param self.aum1: % de aumento
        :param self.dim1: % de diminuição
        :return: devolve o resumo
        """
        print(f"""-----------------------------------------
            RESUMO DO VALOR
-----------------------------------------
{'Dividido por 2:':<25}{self.metade()};
{'Multiplicado por dois:':<25}{self.duplicar()};
{f'Aumentado em {self.aum1}%:':<25}{self.aumentar(self.aum1)};
{f'Diminuido em {self.dim1}%:':<25}{self.diminuir(self.dim1)}.
-----------------------------------------""")

    def aumentar(self, aum, R=False):
        """
        -> Realiza um aumento em regra de três.
        :param R: formata em R$.
        :param self: self a ser aumentado.
        :param aum: porcentagem a aumentar.
        :return: primeiro self aumentado pelo segundo self(%).
        """
        A = self.valor + (self.valor * aum) / 100
        return A.reais() if R is True else A

    def diminuir(self, dim, R=False):
        """
        -> Realiza uma diminuição em regra de três.
        :param R: Formata em R$.
        :param self: self a ser diminuido.
        :param dim: porcentagem a diminuir.
        :return: primeiro self diminuido pelo segundo self(%).
        """
        B = self.valor - (self.valor * dim) / 100
        return B.reais() if R is True else B

    def metade(self, R=False):
        """
        -> Divide o self recebido por dois.
        :param R: formata em R$.
        :param self: self a ser dividido.
        :return: self dividido por dois.
        """
        C = self.valor / 2
        return C.reais() if R is True else C

    def duplicar(self, R=False):
        """
        -> Multiplicao self por dois.
        :param R: formata em R$.
        :param self: self a ser multiplicado.
        :return: self multiplicado por dois.
        """
        D = self.valor * 2
        return D.reais() if R is True else D


if __name__ == 'main':
    teste = Dump(10, 5, 45)
    print(teste.resumo())
