import numpy as np

def compute_error_for_given_points(b, m, points):

def step_gradient(b_current, m_curent, points, learning_rate):
    #gradient descent

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def run():
    points = genfromtext('data.csv', delimite=',')
    #hyperparameters
    learning_rate = 0.0001
    # y = mx + b (formula da inclinacao)
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b, m] = gradient_descent_runner(points, learning_rate, initial_b, initial_m, num_iterations)
    print(b)
    print(m)

if __name__ = '__main__':
    run()
