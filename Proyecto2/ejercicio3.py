# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from network import *

def ejercicio3(option):
	opcion = ""
	opcion2 = ""
	if option == "1":
		outs = 1
	if option == "2":
		outs = 3
	print('\nIntroduzca el número de neuronas para la capa oculta: ')
	no = input('')
	seed(1)
	#network = init_network(4,int(no),outs)
	while opcion == "":
		print('\nSeleccione el conjunto de entrenamiento: \n')
		print(' 1) 50% de los datos\n')
		print(' 2) 60% de los datos\n')
		print(' 3) 70% de los datos\n')
		print(' 4) 80% de los datos\n')
		print(' 5) 90% de los datos\n')
		opcion = input('')
		if opcion == "1":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris50training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train(network, train_set, 0.1, 1000, n_outputs)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris50test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			predict(net,test_set,n_outputs)
		elif opcion == "2":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris60training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net,err, i = train(network, train_set, 0.1, 1000, n_outputs)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris60test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			predict(net,test_set,n_outputs)
		elif opcion == "3":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris70training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train(network, train_set, 0.1, 1000, n_outputs)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris70test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			predict(net, test_set,n_outputs)
		elif opcion == "4":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris80training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train(network, train_set, 0.1, 1000, n_outputs)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris80test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			predict(net, test_set,n_outputs)
		elif opcion == "5":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris90training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			n_inputs = len(train_set[0]) - 1
			n_outputs = len(set([row[-1] for row in train_set]))
			network = init_network(n_inputs,int(no),n_outputs)
			net, err, i = train(network, train_set, 0.1, 1000, n_outputs)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris90test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			predict(net, test_set,n_outputs)
		elif opcion == "6":
			for z in range(1,3):
				print ("DATOS: ", z)
				zeta = str(z)
				if z == 1:
					outs = 1
				else:
					outs = 3
				for y in range(4,11):
					print ("NEURONAS:", y)
					ye = str(y)
					for x in range(5,10):
						equis = str(x)
						print ("DATOS DE ENTRENAMIENTO: ", 15*x)
						#net = init_network(4, y, outs)
						train_set = np.array(np.loadtxt('datosP2EM2017/iris'+zeta+'/iris'+equis+'0training'+zeta+'.txt'),dtype=np.float)
						train_set = train_set/train_set.max(axis=0)
						n_inputs = len(train_set[0]) - 1
						n_outputs = len(set([row[-1] for row in train_set]))
						network = init_network(n_inputs,y,n_outputs)
						net, err, i = train(network, train_set, 0.1, 1000, n_outputs)
						test_set = np.array(np.loadtxt('datosP2EM2017/iris'+zeta+'/iris'+equis+'0test'+zeta+'.txt'),dtype=np.float)
						test_set = test_set/test_set.max(axis=0)
						predict(net,test_set,n_outputs)
		else:
			print('\nDebe introducir \'1\', \'2\', \'3\', \'4\' o  \'5\'\n')
			opcion = ""
