"""
    CI-5437 Inteligencia Artificial II
    Daniel Marín 10-10419
    Dayana Rodrigues 10-10615
    Luis Carlos <apellido> <carnet>

    Implementación del algoritmo de Descenso del Gradiente
    para la resolución de una Regresión Lineal Múltiple.

"""

import numpy as np

""""
theta: vector de costos
values: matriz de valores

"""


def multiple_linear_regression(values, theta, results, alpha, max_iter=100):
    final_cost = []
    iterations = 0

    while iterations < max_iter:

        aux_theta = np.random.random(values.shape[0])

        for i in range(values.shape[0]):
            aux_theta[i] = derived_cost(values, results, theta, alpha, i)

        theta = aux_theta
        print(theta,values,results)
        cost_value = cost(values, results, theta)
        final_cost.insert(iterations, cost_value)
        iterations += 1

    return iterations, final_cost


# función de costo

def cost(values, results, theta):
    cost_value = 0
    for i in range(values.shape[0]):
        cost_value += (h(values[i], theta) - results[i]) ** 2

    return cost_value / 2 * values.shape[0]


def derived_cost(values, results, theta, alpha, j):
    cost = 0
    for i in range(values.shape[0]):
        cost += (h(values[i], theta) - results[i]) * values[i,j]

    return theta[j] - alpha * cost / 2 * values.shape[0]


# función auxiliar para el producto punto

def h(value, theta):
    return np.dot(value, theta)


# función que normaliza los datos

def normalization(values):
    max_value = np.max(values)  # maximo valor de la matriz
    for i in range(values.shape[0]):
        values[i] = (values[i] / max_value)
    return values
