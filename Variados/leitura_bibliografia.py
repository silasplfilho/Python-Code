import pandas as pd

path = r'/home/silas/Documents/GIT/Python-Codes/Variados/prior keywords.csv'
biblio = pd.read_csv(path, sep=';', header = None, names = ['title', 'keywords'])

pd.unique(biblio.keywords)
biblio.keywords.split(',')
.str.split(',')
