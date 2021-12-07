def nota(*list1, sit=False):
    """
    nota() devolve a média da turma.
    :param list1: Digite várias notas separadas por virgula.
    :param sit: True (Para retornar o valor qualitativo da média)
    :return: Média da turma, maior nota, menor nota.
    """
    re = {'Total': sum(list1), 'Menor': min(list1), 'Maior': max(list1), 'Média': sum(list1) / len(list1)}
    if sit:
        if re['Média'] < 5:
            re['Situação'] = 'Ruim'
        elif re['Média'] > 6:
            re['Situação'] = 'Boa'
        else:
            re['Situação'] = 'Razoavel'
    return re


print(nota(3.4, 5.6, 9, 7.3, 5.9, sit=True))
