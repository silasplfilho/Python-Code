import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import mglearn
from sklearn.model_selection import train_test_split # modulo que divide o dataset
#-----------
from sklearn.linear_model import LinearRegression
X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

lr =LinearRegression().fit(X_train, y_train)

print("lr.coef_: {}".format(lr.coef_))
print("lr.intercept_: {}".format(lr.intercept_))

print("Training set score: {:.2f}".format(lr.score(X_train, y_train )))
print("Test set score: {:.2f}".format(lr.score(X_test, y_test )))
#-----
X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
lr = LinearRegression().fit(X_train, y_train )

print("Training set score: {:.2f}".format(lr.score(X_train, y_train )))
print("Test set score: {:.2f}".format(lr.score(X_test, y_test )))
