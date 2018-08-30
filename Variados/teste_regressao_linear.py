import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import datasets
data = datasets.load_boston()

df = pd.DataFrame(data.data, columns = data.feature_names)
target = pd.DataFrame(data.target, columns=["MEDV"])

X = df["RM"]
y = target["MEDV"]

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

model.summary()
#--------
# USANDO UM CASO DO LIVRO PYTHON MACHINE LEARNING - DA EDITORA PACKT
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header=None, sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

df.head()

sns.set(style='darkgrid', context="notebook")
cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
cols2 = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
sns.pairplot(df[cols], size=2.5)
plt.show()

cm = np.corrcoef(df[cols].values.T) # calcula o coeficiente de correlacao das variaveis
sns.set(font_scale=1.5)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={'size':15}, yticklabels=cols, xticklabels=cols)
plt.show()

class LinearRegressionGD(object):

    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)

X = df[['RM']].values
y = df['MEDV'].values
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
X_std = sc_x.fit_transform(X)
y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten() # aqui é diferente do livro - tive q pegar no git deles

lr = LinearRegressionGD()
lr.fit(X_std, y_std)

plt.plot(range(1, lr.n_iter+1), lr.cost_)
plt.ylabel('SSE')
plt.xlabel('Epoch')
plt.show()

def lin_regplot(X, y, model):
    plt.scatter(X, y, c='blue')
    plt.plot(X, model.predict(X), color = 'red')
    return None

lin_regplot(X_std, y_std, lr)
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000 [MEDV]')
plt.show()

num_rooms_std = sc_x.transform([5.0])
#---
