import pandas as pd
url_lixo = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'
dlixo = pd.read_csv(url_lixo, compression='zip')
#print(dlixo['tratamento'].unique())
#x = int(dlixo['tratamento'].value_counts()['com_droga'])
#x /= int(dlixo['tratamento'].value_counts()['com_controle'])
#print(f'A quantidade de com_droga é {x} vezes maior que a de com_controle.') # Desafio 3.
#print(dlixo[-5:]) - Desafio 2.
###drogas = []
###c1 = 0
###for c in dlixo['droga'].unique():
###    if len(drogas) == 0:
###        ponte = ['1']
###    else:
###        ponte = drogas
###    igual = False
###    for d in ponte:
###        if d == c:
###            igual = True
###    if not igual:
###        drogas.append(c)
###print(len(drogas)) # Desafio 4
