#!/usr/bin/env python
import numpy as np 


#funciones de activación

def sigmoidal(x):

	return 1/(1 + np.exp(-x))


def tangenteh(x):

	return (1 - np.exp(-x))/(1 + np.exp(-x))


#funcion de error de la red para el patron n
# Y vector de salida de la red para el patrón
# S vector de salida esperado para el patrón

def error_patron(Y, S, nc):

	suma = 0
	for i in range(1,nc):
		suma += (S[i] - Y[i])^2

	return (1/nc)*suma


#funcón de error general (para todos los patrones)
# o error de entrenamiento
# N numero de patrones de la muestra

def error(N):

	suma = 0
	for i in range(1,N):
		suma += error_patron(i)

	return (1/N)*suma