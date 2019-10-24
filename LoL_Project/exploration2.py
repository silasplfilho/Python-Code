import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dtst = pd.read_csv(r'vem amor bate n para com o DB na minha cara - Form Responses 1.csv')
dtst1 = dtst.iloc[:, :15]
# ---------------------
dtst1.iloc[:5, 2:9]
pers_data = pd.crosstab([dtst1["Sexo"], dtst1["Idade"]],
                        [dtst1["Orientação sexual"], dtst1["Cor pele"]])
sns.heatmap(pers_data, fmt="d", annot=True)
# ---------------------
sns.countplot(x='Cor pele', data=dtst1)
plt.show()


dtst1.loc[:, ["Sexo", "Idade", "Orientação sexual", "Cor pele"]].plot()
# ---------------------
test1 = pd.crosstab(dtst1['Sexo'], dtst1[("Quantidade que jogou "
                                          "League of Legends no último mês?")])

test2 = pd.crosstab(dtst1['Sexo'], dtst1[("Percebeu alguma opressão ou discriminação em "
                                          "qualquer tela neste último mês?")])
# ---------------------
tips = sns.load_dataset("tips")
tips.head()
# ---------------------
sns.heatmap(test1, fmt="d", annot=True)
plt.xticks(rotation=30)
plt.show()
sns.heatmap(test2, fmt="d", annot=True)
plt.show()
