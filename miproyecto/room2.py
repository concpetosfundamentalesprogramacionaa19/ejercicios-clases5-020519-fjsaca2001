"""
	File: room2.py
	Autor: Frank J. Saca Q,
"""
# creacion de variables importantes

# importacion de misvariables.py

from misvariables import*

# requerimiento de datos
nota = input("Ingrese una nota: ")
nota2 = input("Ingrese una segunda nota: ")

nota = int (nota)
nota2 = int (nota2)

# condicional si/no entonces

if nota == 18:
	print("%s, su nota es: %d" % (mensaje,nota))
else: 
	print("%s, su nota es: %d" % (mensaje,nota2))

if nota2 >= 18:
	print("%s, su nota es: %d" % (mensaje,nota))
else: 
	print("%s, su nota es: %d" % (mensaje2,nota))
