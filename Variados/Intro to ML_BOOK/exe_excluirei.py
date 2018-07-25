import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import mglearn

from sklearn.datasets import load_iris
iris_dataset = load_iris()
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys())) # keys aparentemente mostra os atributos
print(iris_dataset['DESCR'][:193]) #  O ATRIBUTO DESCR mostra uma descricao do dataset
print("Type of data: {}".format(type(iris_dataset['data'])))
print("Type of data: {}".format(iris_dataset['feature_names']))

#--------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                    iris_dataset['target'], random_state=0)

print("X_trains shape: {}".format(X_train.shape))
print("y_trains shape: {}".format(y_train.shape))
print("X_trains shape: {}".format(X_test.shape))
print("X_trains shape: {}".format(y_test.shape))

#--------
import pandas as pd
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

grr = pd.plotting.scatter_matrix(iris_dataframe, c = y_train, figsize=(15,15), \
                        marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
