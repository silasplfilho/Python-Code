# Data Preprocessing

#%%
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%
# Importing the dataset
dataset = pd.read_csv('/home/silas/Documents/GIT/Python-Codes/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#%%
# Taking care of missing data
from sklearn.preprocessing import Imputer # importando a classe Imputer q trata de dados faltosos
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
