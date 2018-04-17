import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


amostra = [181.37984274, 154.80600659, 182.33424888, 170.32065307, 179.82634437, 168.73723578, 164.28520413, 171.93415101, 171.71090179, 177.69136458,
 153.38183565, 151.13269527, 166.4994225, 828.37581774 ,168.02278222, 169.29065423, 138.46062748, 174.88588464, 155.01472584, 164.27356639]

amostra2 = [181.37984274, 154.80600659, 182.33424888, 170.32065307, 179.82634437, 168.73723578, 164.28520413, 171.93415101, 171.71090179, 177.69136458,
 153.38183565, 151.13269527, 166.4994225, 168.02278222, 169.29065423, 138.46062748, 174.88588464, 155.01472584, 164.27356639]

# 1) Qual a média da amostra?
media = np.mean(amostra)

# 2) Qual o desvio padrão da amostra?
desvio_padrao = np.std(amostra)

# 3) Faça um histograma com os dados.
plt.hist(amostra, bins=300)
plt.show()
#------------------------------
# 4) Qual distribuição se enquadra melhor para os dados?
# Normal

# 5) Infira a média da população a partir da amostra.
media_pop = np.mean(amostra)

# 6) Infira o desvio padrão da população a partir da amostra.
std_pop = np.sqrt( np.sum((amostra - media)**2) / len(amostra)-1 )

# 7) Considerando a média e desvio padrão que você inferiu a partir da amostra
# e a distribuição que você hipotetizou sobre os dados,  qual a probabilidade de:
# a) encontrar o valor 200.00
# b) o valor ser maior que 180
# c) o valor ser menor que 120 e maior que 190
