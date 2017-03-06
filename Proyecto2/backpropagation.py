#!/usr/bin/env python
import numpy as np 


#funciones de activación

def sigmoidal(x):

	return 1/(1 + np.exp(-x))


def tangenteh(x):

	return (1 - np.exp(-x))/(1 + np.exp(-x))

def d_sigmoidal(x):

	return x*(1-x)

def d_tangenteh(x):

	return 1-(np.tanh(x)**2)

#funcion de error de la red para el patron n
# Y vector de salida de la red para el patrón
# S vector de salida esperado para el patrón

"""def error_patron(Y, S):

	suma = 0
	for i in range(1,Y.size()):
		suma += (S[i] - Y[i])^2

	return (1/Y.size())*suma


#funcón de error general (para todos los patrones)
# o error de entrenamiento
# N numero de patrones de la muestra

def error(N):

	suma = 0
	for i in range(1,N):
		suma += error_patron(i)

	return (1/N)*suma"""


class MLP:

	def __init__(self, n_entrada, n_oculta, n_salida):

		# valores de las neuronas
		self.v_entrada = np.ones(1,n_entrada)
		self.v_oculto = np.ones(1,n_oculta)
		self.v_salida = np.ones(1,v_salida)

		# inicializar los pesos con un numero aleatorio 
		# cómo lo hago cercano a 0?
		self.pesos_eo = np.random.rand(n_oculta, self.n_entrada)
		self.pesos_os = np.random.rand(n_salida, self.n_oculta)


	def f_propagation(self, X):

		# activacion de las neuronas de la capa de entrada
		self.v_entrada[0][1:] = X

		#activación de las neuronas de la capa oculta
		v_entrada_t = np.transpose(self.v_entrada)
		z = np.dot(self.pesos_eo, v_entrada_t)
		z_t = np.transpose(z)

		# se aplica la funcion de transferencia

		self.v_oculto[0][0] = 1

		for i in range(0,self.v_oculto.size()):
			self.v_oculto[0][i+1] = sigmoidal(z_t[0][i])


		# activación de las neuronas de la capa de salida
		v_oculto_t = np.transpose(self.v_oculto)
		z = np.dot(self.pesos_os, v_oculto_t)
		z_t = np.transpose(z)

		self.v_salida = sigmoidal(z_t)

		# vector con la salida
		return self.v_salida

	def b_propagation(self, X, Y):

		# para cada patrón
		for i in range(0,X.size()):

			# fordwarpropagation
			self.f_propagation(X[i])

			# se evalua el error de salida para el patron i
			error_i = self.v_salida - Y[i]

			# se calculan los delta
			v_oculto_t = np.transpose(self.v_oculto)
			error_i_t = np.transpose(error_i)
			pesos_os_t = np.transpose(self.pesos_os)
			error_o = np.dot(pesos_os_t, error_i_t)*d_sigmoidal(pesos_os_t)




