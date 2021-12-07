import pandas as pd
url_lixo = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'
dlixo = pd.read_csv(url_lixo, compression='zip')
print(dlixo[-5:])
