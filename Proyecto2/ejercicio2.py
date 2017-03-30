# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from mlp import *

def ejercicio2():
	opcion = ""
	opcion2 = ""
	print('\nIntroduzca el número de neuronas para la capa oculta: ')
	no = input('')
	net = MLP([2,int(no),1])
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
			X = train_set.T[:-1].T
			y = train_set.T[-1]
			net.train(X, y)
			t_err = 0
			for (i,e) in enumerate(X):
				a = net.predict(e)
				t_err += abs(y[i] - a[0])
				for i in range(len(a)):
					if(a[i] < 0.5):
						v = 0
					else:
						v = 1
				#print(e,v)
			print(t_err/len(y))
		elif opcion == "2":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos_P2_EM2017_N1000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			X = train_set.T[:-1].T
			y = train_set.T[-1]
			net.train(X, y)
			t_err = 0
			for (i,e) in enumerate(X):
				a = net.predict(e)
				t_err += abs(y[i] - a[0])
				for i in range(len(a)):
					if(a[i] < 0.5):
						v = 0
					else:
						v = 1
				#print(e,v)
			print(t_err/len(y))
		elif opcion == "3":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos_P2_EM2017_N2000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			X = train_set.T[:-1].T
			y = train_set.T[-1]
			e =net.train(X, y)
			print(len(e))
			plt.figure(1)
			plt.ylabel('iteration error')
			plt.xlabel('iteration')
			plt.plot(np.arange(0,1000),e, 'k')
			plt.show()
			train_set = np.array(np.loadtxt('datosP2EM2017/datos_P2_EM2017_N2000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			X = train_set.T[:-1].T
			y = train_set.T[-1]
			t_err = 0
			v = []
			for (i,e) in enumerate(X):
				a = net.predict(e)
				print(a)
				t_err += abs(y[i] - a[0])
				for i in range(len(a)):
					if(a[i] < 0.5):
						v.append(0)
					else:
						v.append(1)
				#print(e,v)
			print(t_err/len(y))
		elif opcion == "4":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos500.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			X = train_set.T[:-1].T
			y = train_set.T[-1]
			net.train(X, y)
			t_err = 0
			for (i,e) in enumerate(X):
				a = net.predict(e)
				t_err += abs(y[i] - a[0])
				for i in range(len(a)):
					if(a[i] < 0.5):
						v = 0
					else:
						v = 1
				#print(e,v)
			print(t_err/len(y))
		elif opcion == "5":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos1000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			X = train_set.T[:-1].T
			y = train_set.T[-1]
			net.train(X, y)
			t_err = 0
			for (i,e) in enumerate(X):
				a = net.predict(e)
				t_err += abs(y[i] - a[0])
				for i in range(len(a)):
					if(a[i] < 0.5):
						v = 0
					else:
						v = 1
				#print(e,v)
			print(t_err/len(y))
		elif opcion == "6":
			train_set = np.array(np.loadtxt('datosP2EM2017/datos2000.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			X = train_set.T[:-1].T
			y = train_set.T[-1]
			net.train(X, y)
			t_err = 0
			for (i,e) in enumerate(X):
				a = net.predict(e)
				t_err += abs(y[i] - a[0])
				for i in range(len(a)):
					if(a[i] < 0.5):
						v = 0
					else:
						v = 1
				#print(e,v)
			print(t_err/len(y))
		else:
			print('\nDebe introducir \'1\', \'2\', \'3\', \'4\', \'5\' o  \'6\'\n')
			opcion = ""
