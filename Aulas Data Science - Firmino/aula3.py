import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------
num_points = int(10e5)
mean = 0
variance = 1
std = (variance)**0.5

points = np.random.normal(mean, std, num_points)

plt.plot(points)
plt.show()

plt.hist(points, bins=100)
plt.show()
#--------------------------------------
file_path = r'/home/silas/Documents/GIT/Python-Codes/Aulas Data Science - Firmino/Tarefa Pokemon/pokemon.csv'
pokemon_data = pd.read_csv(file_path)
pokemon_data.describe()
attack = pokemon_data['sp_attack']
#--------------------------------------
plt.plot(attack)
plt.show()
plt.hist(attack, 10)
plt.show()
#--------------------------------------
def gauss_value(points, mu, std):
    y_gauss = (1/(std * np.sqrt(2 + np.pi)) ) * np.e**(-0.5 * (points-mu)**2 / std**2 )
    return(y_gauss)

mean_attack = 175.305868
std_attack = 32.353826

x_base = np.arange(0,200)
y_gauss = gauss_value(x_base, mean_attack, std_attack)

plt.plot(attack, np.zeros(attack.shape[0]), 'ro')
plt.plot(x_base, y_gauss)

plt.show()
#--------------------------------------
mu_range = np.arange(50, 150, 0.5)
std_range = np.arange(30, 80, 0.5)

best_mu = -np.inf
best_std = -np.inf
max_likelihood = -np.inf

for mu_t in mu_range:
    for std_t in std_range:
        y_gauss = gauss_value(attack, mu_t, std_t)
        log_likelihood = np.sum(-np.log(y_gauss))

        if (log_likelihood - max_likelihood) > 0.0001:
            max_likelihood = log_likelihood
            best_mu = mu_t
            best_std = std_t

print("melhor mu: ", best_mu)
print("melhor std: ", best_std)
#--------------------------------------
mean_attack = 175.305868
std_attack = 32.353826

mean_opt = 149
std_opt = 30

x_base = np.arange(0,200)
y_gauss_sample = gauss_value(x_base, mean_attack, std_attack)
y_gauss_max = gauss_value(x_base, mean_opt, std_opt)

plt.plot(attack, np.zeros(attack.shape[0]), 'ro')
plt.plot(x_base, y_gauss_sample, 'r')
plt.plot(x_base, y_gauss_max, 'g')

plt.show()
