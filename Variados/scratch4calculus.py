import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return (t**-2)


def f2(t):
    return 1/(1 + np.e ** -t)
    
    
def f3(t):
    return np.tanh(t)


t1 = np.arange(-10, 10, .1)
plt.plot(t1, f3(t1), 'k')
