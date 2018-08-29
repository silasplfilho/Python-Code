# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable of the State
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3]) # Posso usar o metodo unique do pandas
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:] # armadilha da variavel idiota - se tenho 3 categorias, eu devo deixar 2

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print("{} \n {}".format(dataset.head(), X[1:5, :])) # Imprimindo os valores do dataset e X
print("{} \n {}".format(y_pred[0:5], y_test[0:5])) # imprimindo os valores de y_teste e y_pred

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)
# creation of a new dataset of optimal independent variables
X_opt =  X[:, [0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
#-- Executando sem a variavel x2 (q tem o maior p-value)
X_opt =  X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
#-- Executando sem a variavel x1 (q tem o maior p-value)
X_opt =  X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
#-- Executando sem a variavel x4 (q tem o maior p-value)
X_opt =  X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
#-- Executando sem a variavel x5 (q tem o maior p-value)
X_opt =  X[:, [0,3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

pd.DataFrame(X_train) # visualizing the dataset as a DataFrame
#---------
plt.scatter(X_train[:,3], y_train, color = 'red')

y_axis = regressor_OLS.predict(np.shape(X_train[:,3]))
plt.plot(X_train[:,3], , color='blue')
plt.show()
