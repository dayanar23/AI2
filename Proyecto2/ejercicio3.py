# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from mlp import *

def ejercicio3(option):
	t = False
	opcion = ""
	opcion2 = ""
	if option == "1":
		outs = 1
	if option == "2":
		outs = 3
		t = True
	print('\nIntroduzca el número de neuronas para la capa oculta: ')
	no = input('')
	net = MLP([4,int(no),outs])
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
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = train_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = train_set.T[:-1].T
				y = train_set.T[-1]
			net.train(X, y)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris50test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = test_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = test_set.T[:-1].T
				y = test_set.T[-1]
			for e in X:
				print(e,net.predict(e))
		elif opcion == "2":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris60training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = train_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = train_set.T[:-1].T
				y = train_set.T[-1]
			net.train(X, y)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris60test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = test_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = test_set.T[:-1].T
				y = test_set.T[-1]
			for e in X:
				print(e,net.predict(e))
		elif opcion == "3":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris70training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = train_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = train_set.T[:-1].T
				y = train_set.T[-1]
			net.train(X, y)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris70test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = test_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = test_set.T[:-1].T
				y = test_set.T[-1]
			for e in X:
				print(e,net.predict(e))
		elif opcion == "4":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris80training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = train_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = train_set.T[:-1].T
				y = train_set.T[-1]
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris80test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = test_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = test_set.T[:-1].T
				y = test_set.T[-1]
			for e in X:
				print(e,net.predict(e))
		elif opcion == "5":
			train_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris90training'+option+'.txt'),dtype=np.float)
			train_set = train_set/train_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = train_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = train_set.T[:-1].T
				y = train_set.T[-1]
			net.train(X, y)
			test_set = np.array(np.loadtxt('datosP2EM2017/iris'+option+'/iris90test'+option+'.txt'),dtype=np.float)
			test_set = test_set/test_set.max(axis=0)
			if(t):
				x1,x2,x3,x4,y1,y2,y3 = test_set.T
				X = np.vstack([x1,x2])
				X = np.vstack([X,x3])
				X = np.vstack([X,x4]).T
				y = np.vstack([y1,y1])
				y = np.vstack([y,y3]).T
			else:
				X = test_set.T[:-1].T
				y = test_set.T[-1]
			for e in X:
				print(e,net.predict(e))
		elif opcion == "6":
			for z in range(1,3):
				print ("DATOS: ", z)
				zeta = str(z)
				if z == 1:
					outs = 1
				else:
					outs = 3
					t = True
				for j in range(4,11):
					print ("NEURONAS:", j)
					ye = str(j)
					for x in range(5,10):
						equis = str(x)
						print ("DATOS DE ENTRENAMIENTO: ", 15*x)
						net = MLP([4, j, outs])
						train_set = np.array(np.loadtxt('datosP2EM2017/iris'+zeta+'/iris'+equis+'0training'+zeta+'.txt'),dtype=np.float)
						train_set = train_set/train_set.max(axis=0)
						if(t):
							x1,x2,x3,x4,y1,y2,y3 = train_set.T
							X = np.vstack([x1,x2])
							X = np.vstack([X,x3])
							X = np.vstack([X,x4]).T
							y = np.vstack([y1,y1])
							y = np.vstack([y,y3]).T
						else:
							X = train_set.T[:-1].T
							y = train_set.T[-1]
						net.train(X, y)
						test_set = np.array(np.loadtxt('datosP2EM2017/iris'+zeta+'/iris'+equis+'0test'+zeta+'.txt'),dtype=np.float)
						test_set = test_set/test_set.max(axis=0)
						if(t):
							x1,x2,x3,x4,y1,y2,y3 = test_set.T
							X = np.vstack([x1,x2])
							X = np.vstack([X,x3])
							X = np.vstack([X,x4]).T
							y = np.vstack([y1,y1])
							y = np.vstack([y,y3]).T
						else:
							X = test_set.T[:-1].T
							y = test_set.T[-1]
						for e in X:
							print(e,net.predict(e))
		else:
			print('\nDebe introducir \'1\', \'2\', \'3\', \'4\' o  \'5\'\n')
			opcion = ""
