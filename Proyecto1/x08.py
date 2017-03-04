import numpy as np
import multipleLinearRegression as mlr

if __name__ == '__main__':
    file = open("x08.txt", 'r')
    data_set = np.loadtxt(file, usecols=(1,))
    file.close()

    data_set = mlr.normalization(data_set)
    alpha = 0.1
    theta = np.array([1 for i in data_set.shape[1]])
    results = data_set[:, 4]
    iterations, cost_values = mlr.multiple_linear_regression(data_set, theta, results, alpha)
    best_iteration = np.where(cost_values == cost_values.min())
    print("Best iteration: ", best_iteration[0][0])
    print(cost_values[best_iteration[0][0]], iterations)
