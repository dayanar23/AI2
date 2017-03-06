#!/usr/bin/env python
import random

# datos de entrenamiento
nombre_archivo = "datosP2EM2017/datos500.txt"

archivo = open(nombre_archivo, 'w')

for i in range(0,500):

	x = random.uniform(0,20)
	y = random.uniform(0,20)

	z = (x-10)**2 + (y-10)**2
	if (z < 36 or z == 36):
		r = 1
	else:
		r = 0

	archivo.write(str(x) + " " + str(y) + " " + str(r) + "\n")


nombre_archivo = "datosP2EM2017/datos1000.txt"

archivo = open(nombre_archivo, 'w')

for i in range(0,1000):

	x = random.uniform(0,20)
	y = random.uniform(0,20)

	z = (x-10)**2 + (y-10)**2
	if (z < 36 or z == 36):
		r = 1
	else:
		r = 0

	archivo.write(str(x) + " " + str(y) + " " + str(r) + "\n")


nombre_archivo = "datosP2EM2017/datos2000.txt"

archivo = open(nombre_archivo, 'w')

for i in range(0,2000):

	x = random.uniform(0,20)
	y = random.uniform(0,20)

	z = (x-10)**2 + (y-10)**2
	if (z < 36 or z == 36):
		r = 1
	else:
		r = 0

	archivo.write(str(x) + " " + str(y) + " " + str(r) + "\n")

# datos de prueba 

nombre_archivo = "datosP2EM2017/datosPrueba.txt"

archivo = open(nombre_archivo, 'w')

x = 0
while x < 20:
    y = 0
    while y < 20:
        z = (x - 10) ** 2 + (y - 10) ** 2
        if  z < 36 or z == 36 :
            r = 1
        else:
            r = 0

        archivo.write(str(x) + " " + str(y) + " " + str(r) + "\n")
        y += 0.2
    x += 0.2