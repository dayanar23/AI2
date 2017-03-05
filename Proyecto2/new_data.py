#!/usr/bin/env python
import random

nombre_archivo = "datos500.txt"

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


nombre_archivo = "datos1000.txt"

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


nombre_archivo = "datos2000.txt"

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
