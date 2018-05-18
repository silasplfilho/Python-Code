import numpy as np

class Perceptron(object):
    """ Perceptron classifier

    Parameters
    ------------
    eta : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.

    Attributes
    -----------
    w_ : 1d-array
        Weights after fitting.
    errors_ : list
        Number of misclassifications in every epoch.
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples
            is the number of samples and n_features
            is the number of features.
        y: array-like, shape = [n_samples]
            Target values

        Returns
        -------
        self:object
        """

        self.w_ = np.zeros
