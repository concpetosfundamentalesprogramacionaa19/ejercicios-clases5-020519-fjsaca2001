"""
	File: room3.py
	Autor: Frank J. Saca Q.
	
	nota mayor o igual a 18 -> sobresaliente

	nota mayor o igual a 16 y menor a 19 -> muy buena
	
	nota mayor o igual a 13 y menor a 16 -> bueno

	nota menor o igual a 13 y menor a 16 -> insuficiete

# importacion de misvariables.py
"""
from misvariables import*

# requerimiento de datos
nota = input("Ingrese una nota: ")

nota = int (nota)

# condicional anidado

if nota >= 18:
	print("%s nota: %d" % ("sobresaliente",nota))
else: 
	if (nota >= 16) and (nota < 18):
		print("%s nota: %d" % ("muy buena",nota))
	else: 
		if (nota >= 13) and (nota <16):
			print("%s nota: %d" % ("bueno",nota))
		else:
			print("%s nota: %d" % ("insuficiete",nota))

