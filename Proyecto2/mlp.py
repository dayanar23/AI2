# Implementacion de un perceptrón multicapas 
# entrenado con backpropagation
#
# Daniel Marín 10-10419
# Dayana Rodrigues 10-10615
# Luis Carlos Díaz 11-10293

import numpy as np

# functions of transfer
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0 - x**2

#class for MLP
class MLP:

    def __init__(self, layers):
        self.activation = sigmoid
        self.activation_prime = sigmoid_prime

        # Set weights
        self.weights = []

        for i in range(1, len(layers) - 1):
            r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
            self.weights.append(r)

        r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
        self.weights.append(r)

    # train network
    def train(self, X, y, learning_rate=0.2, epochs=1000):
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)
        err = 0
        conv = []
        for k in range(epochs):
            e = []
            if k % 10000 == 0: print ('epochs:', k)
            
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            # fordwarpropagation
            for l in range(len(self.weights)):
                dot_value = np.dot(a[l], self.weights[l])
                activation = self.activation(dot_value)
                a.append(activation)

            # output layer
            error = y[i] - a[-1]
            e.append(error)
            deltas = [error * self.activation_prime(a[-1])]

            for l in range(len(a) - 2, 0, -1): 
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))

            deltas.reverse()

            # backpropagation
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

            err += 0.5*sum([e[i]**2 for i in range(len(e))])
            conv.append(0.5*sum([e[i]**2 for i in range(len(e))]))
        print((1/epochs)*err)
        return np.array(conv)

    # predict class
    def predict(self, x): 

        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)      
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a