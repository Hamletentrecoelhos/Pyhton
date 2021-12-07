import pandas as pd
url_lixo = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'
dlixo = pd.read_csv(url_lixo, compression='zip')
print('Meu Modo:')
x = int(dlixo['tratamento'].value_counts()['com_droga'])
x /= int(dlixo['tratamento'].value_counts()['com_controle'])
print(f'A quantidade de com_droga é {x} vezes maior que a de com_controle.')
print()
print('Modo Pandas:')
print(dlixo['tratamento'].value_counts(normalize=True))
