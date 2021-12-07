from ex111utilidadesCeV import Moeda
v = float(input('Digite o valor da carteira: '))
print(f"""A carteira dividida por dois é {Moeda.metade(v, False)};
A carteira vezes dois é {Moeda.duplicar(v), False};
A carteira aumentada em 13% é {Moeda.aumentar(v, 13, False)};
A carteira diminuida em 10% é {Moeda.diminuir(v, 10, False)}.""")
