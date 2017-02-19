"""
    CI-5437 Inteligencia Artificial II
    Daniel Marín 10-10419
    Dayana Rodrigues 10-10615
    Luis Carlos <apellido> <carnet>

    Implementación del algoritmo de Descenso del Gradiente
    para la resolución de una Regresión Lineal Múltiple.

"""

import numpy as np


def multiple_linear_regression(values, theta, results, cost_value, alpha=0.0000001, max_iter=1000):
    converge = False
    final_cost = []
    iterations = 0

    while not converge and iterations < max_iter:

        aux_theta = np.random.random(values.shape[1])

        for i in range(values.shape[1]):
            aux_theta[i] = derived_cost(values, results, theta, alpha, values.shape[0], i)

        theta = aux_theta
        aux_cost = cost(values, results, theta, values.shape[0])
        final_cost.insert(iterations, cost)
        iterations += 1

        converge = abs(aux_cost - cost_value) <= 0.01
        cost_value = aux_cost

    return converge


# función de costo

def cost(values, results, theta, m):
    cost_value = 0
    for i in range(m):
        cost_value += (h(values[i], theta)-results[i])**2

    return cost_value/2*m


def derived_cost(values, results, theta, alpha, m, j):
    cost = 0
    for i in range(m):
        cost += (h(values[i], theta) - results[i]) * values[i][j]

    return theta[j]-alpha*cost/2*m


# función auxiliar para el producto punto

def h(value, theta):
    return np.dot(value, theta)


# función que normaliza los datos

def normalization(values):
    max_value = np.max(values)  # maximo valor de la matriz
    for i in range(values.shape[1]):
        values[:, i] = (values[:, i] / max_value)

    return values
