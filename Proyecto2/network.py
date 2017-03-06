from random import seed
from random import random
import numpy as np
 
# Initialize a network
def init_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network
 
# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
 
# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + np.exp(-activation))
 
# Forward propagate input to a network output
def forwardpropagation(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs
 
# Calculate the derivative of an neuron output
def transfer_d(output):
	return output * (1.0 - output)
 
# Backpropagate error and store in neurons
def backpropagation(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_d(neuron['output'])
 
# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']
 
# Train a network for a fixed number of epochs
def train(network, train, l_rate, n_epoch, n_outputs):
	err = []
	ep = 0.01
	nconverge = True
	epoch = 0
	while(epoch < n_epoch and nconverge):
		sum_error = 0
		for row in train:
			outputs = forwardpropagation(network, row)
			expected = [0 for i in range(n_outputs)]
			sum_error += 0.5*sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backpropagation(network, expected)
			update_weights(network, row, l_rate)
			#print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
		if(abs(err[-1:] - sum_error) < ep):
			nconverge = False
		err.append(sum_error)
		epoch += 1
	return (network, np.array(err), epoch)

def predict(network,train,n_outputs):
	sum_error = 0
	val = []
	for row in train:
		outputs = forwardpropagation(network, row)
		print(outputs)
		expected = [0 for i in range(n_outputs)]
		sum_error += 0.5*sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
		val.append(outputs)
	for i in range(0,len(val)):
		if(val[i][0] < 0.5):
			val[i][0]= 0
		else:
			val[i][0] = 1
	return((1/train.shape[0])*sum_error, np.array(val))