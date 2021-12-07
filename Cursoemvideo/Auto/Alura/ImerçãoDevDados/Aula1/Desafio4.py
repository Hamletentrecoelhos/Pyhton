import pandas as pd
url_lixo = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'
dlixo = pd.read_csv(url_lixo, compression='zip')
drogas = []
c1 = 0
for c in dlixo['droga'].unique():
    if len(drogas) == 0:
        ponte = ['1']
    else:
        ponte = drogas
    igual = False
    for d in ponte:
        if d == c:
            igual = True
    if not igual:
        drogas.append(c)
print(len(drogas))
