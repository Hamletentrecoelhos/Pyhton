lista = 'Tucano', 'Laringe', 'jovem', 'nerd', 'macaco', 'lanceiro', 'pneumoultramicroscopicossilicovulcanoconiótico'
for c in range(0, len(lista)):
    test = lista[c].upper()
    vo = str()
    for c1 in range(0, len(lista[c])):
        if test[c1] in 'AEIOUÀÈÌÒÙÁÉÍÓÚÃẼĨÕŨÂÊÎÔÛ':
            vo += '' + test[c1]
    print(f'A palavra {test} possui as vogais: {vo}')
