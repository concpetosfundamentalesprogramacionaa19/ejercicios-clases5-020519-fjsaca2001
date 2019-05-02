"""
	Deseamos obtener el costo de una carrera universitaria 
	el valor promedio de cada ciclo es de: 1200$, el valor
	promedio del seguro educativo es de: 100$ si la edad del estudiante es 
	menor a igual a 20 caso contario sera de 150$, si el estudiante tiene 
	una modalidad a distancia el numero de ciclos es de 10 caso contrario 
	debera seguir 8 ciclos. Obtener la proyeccion del costo de la carrera
	de un estudiante
"""
costo_c = 1200
edad = input("ingrese su edad: ")
edad = int(edad)
modalidad = input("ingrese su modalidad:\n1. Distancia\n2. Presencial  \n")
modalidad = int(modalidad)

if (modalidad == 1):
	ciclos = 10
	costo_c *= 10 
else: 
	ciclos = 8
	costo_c *= 8

if(edad <= 20):
	seguro = 100

else:
	seguro = 150

# Calculo de precios

seguro *= ciclos
costo_c += seguro

print("Su precio final a pagar por la carrera es de: %d" % costo_c)