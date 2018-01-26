#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:09:33 2017

@author: silas
"""
#------importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#------separando os atributos em dependentes e nao dependentes
dataset = pd.read_csv('/home/silas/Machine Learning - Udemy/Machine Learning A-Z Template Folder/Part 2 - Regression/Section 4 - Simple Linear Regression/Simple_Linear_Regression/Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

#------separando os conjuntos de treino e de teste
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#------importando a biblioteca linearregression do sklearn
##------treinando o regressor com metodo fit e com os conjuntos de treinamento
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#------Prediction of test results
y_pred = regressor.predict(X_test)

#------Visualising the training set results
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

#------Visualising the test set results
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()