import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dtst = pd.read_csv(r'vem amor bate n para com o DB na minha cara - Form Responses 1.csv')
dtst1 = dtst.iloc[:, :15]
# -------
pd.unique(dtst1.Sexo)
pd.unique(dtst1['Bloqueou a comunicação no jogo neste último mês?'])

test1 = dtst1.groupby('Sexo')['Quantidade que jogou League of Legends no último mês?'].value_counts().unstack().fillna(0)
dtst1.groupby('Sexo')['Bloqueou a comunicação no jogo neste último mês?'].value_counts()
dtst1.groupby('Sexo')['Percebeu alguma opressão ou discriminação em qualquer tela neste último mês?'].value_counts()
dtst1.groupby('Sexo')['Qual discriminação percebeu neste último mês? [11 – OPCIONAL]'].value_counts()
dtst1.groupby('Sexo')['Qual frequência você percebeu essa opressão ou discriminação social neste último mês? [11 – OPCIONAL]'].value_counts()

# --- plotting
test1
pd.pivot_table(dtst1,
               values='Quantidade que jogou League of Legends no último mês?',
               index='Sexo',
               aggfunc=np.count_nonzero)

pd.pivot_table(dtst1,
               index=['Sexo', 'Quantidade que jogou League of Legends no último mês?', ],
               aggfunc=np.count_nonzero
               ).reset_index()

# ----
b = test1.to_frame()
b.columns

, value_vars=)
b = dtst1.melt('Sexo')
b.pivot_table(index='Sexo', columns='Quantidade que jogou League of Legends no último mês?')

# ----real plotting
sns.heatmap(test1, annot=True)
plt.show()

sns.heatmap(, cmap="YlGnBu")

test1 = test1.reset_index()
test1.reset_index(col_level=0)
test1.columns

test1 = test1.value_counts()
test1.values
a = test1.to_dict()

test1.reset_index(inplace=True)

test1.plot.kde()
plt.show()
test1.get_values()
test1.get_label
