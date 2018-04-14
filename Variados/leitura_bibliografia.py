import pandas as pd

path = r'/home/silas/Documents/GIT/Python-Codes/Variados/prior keywords.csv'
biblio = pd.read_csv(path, sep=';', header = None, names = ['title', 'keywords'])

pd.unique(biblio.keywords)
biblio.keywords.iloc[1]
for i in biblio.keywords: biblio.keywords.loc[i] = biblio.keywords.loc[i].split(',')

.str.split(',')
