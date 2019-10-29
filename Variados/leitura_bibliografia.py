import pandas as pd
import numpy as np

path = r'/home/silas/Downloads/articles(2).csv'
biblio = pd.read_csv(path, sep=';', header=0, na_filter=False)
# ---
pd.unique(biblio['source'])
# --------
acm = biblio[biblio['source'] == 'ACM Digital Library']
res = pd.DataFrame(acm[acm['status'].isin(['Unclassified', 'Accepted'])].loc[:, 'doi']).reset_index(drop=True)
res.to_csv(r'/home/silas/Downloads/acm_uncl.csv', sep=';')
# --------
ieee = biblio[biblio['source'] == 'IEEE Digital Library']
res = pd.DataFrame(ieee[ieee['status'].isin(['Unclassified', 'Accepted'])].loc[:, 'doi']).reset_index(drop=True)
res.to_csv(r'/home/silas/Downloads/ieee_uncl.csv', sep=';')

# ----
scopus = biblio[biblio['source']=='Scopus']
scopus['start'] = pd.DataFrame(scopus.pages.values)
scopus = scopus.reset_index(drop='True')
scopus.pages.str.split('-')

scopus
# ---------
pd.unique(biblio.keywords)
biblio.keywords.iloc[1]
for i in biblio.keywords: biblio.keywords.loc[i] = biblio.keywords.loc[i].split(',')

.str.split(',')
