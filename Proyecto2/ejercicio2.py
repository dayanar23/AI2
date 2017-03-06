import numpy as np
import matplotlib.pyplot as plt
from network import *


def ejercicio2():
	opcion = ""
	opcion2 = ""
	print('\nIntroduzca el número de neuronas para la capa oculta: ')
	no = input('')
	seed(1)
	while opcion == "":
		print('\nSeleccione el conjunto de entrenamiento: \n')
		print(' 1) 500 patrones dados\n')
		print(' 2) 1000 patrones dados\n')
		print(' 3) 2000 patrones dados\n')
		print(' 4) 500 patrones generados\n')
		print(' 5) 1000 patrones generados\n')
		print(' 6) 2000 patrones generados\n')
		opcion = input('')
		if opcion == "1":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos_P2_EM2017_N500.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			print(n_outputs)
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train(network, train_set, 0.1, 1000, n_outputs)
			print((1/train_set.shape[0])*sum(err))
			print(i)
			errt, val = predict(net,train_set,n_outputs)
			print(errt)
			plt.figure(1)
			plt.plot(np.arange(0,i), err)
			plt.show()
		elif opcion == "2":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos_P2_EM2017_N1000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train_network(network, train_set, 0.1, 1000, n_outputs)
			print((1/train_set.shape[0])*sum(err))
		elif opcion == "3":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos_P2_EM2017_N2000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train_network(network, train_set, 0.1, 1000, n_outputs)
			print((1/train_set.shape[0])*sum(err))
		elif opcion == "4":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos500.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			nn_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train_network(network, train_set, 0.1, 1000, n_outputs)
			print((1/train_set.shape[0])*sum(err))
		elif opcion == "5":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos1000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train_network(network, train_set, 0.1, 1000, n_outputs)
			print((1/train_set.shape[0])*sum(err))
		elif opcion == "6":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos2000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train_network(network, train_set, 0.1, 1000, n_outputs)
			print((1/train_set.shape[0])*sum(err))
		else:
			print('\nDebe introducir \'1\', \'2\', \'3\', \'4\', \'5\' o  \'6\'\n')
			opcion = ""
