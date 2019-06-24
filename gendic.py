#! /bin/python
# Generacion de un peque;o alfabeto tomando como referencia palabras con las que la victima se identifique,
# apellido, nombre, nombre de familiares, mascotas, lugares, gustos, etc
import sys
import os
import time
nombre = time.strftime("%d_%m_%y-%H_%M_%S") #genera el nombre que tendra el diccionario
'''
Este archivo de diccionario tendrá un nombre compuesto por la fecha y hora del sistema
los primeros tres parametros separados por guiones bajos representan la fecha
en formato dd/mm/yyyy
los siguientes tres representan horas, minutos y segundos respectivamente
fecha y hora esta separado por un guión normal.

este archivo tendrá un nombre con este formato para evitar conflictos con archivos existentes
si el usuario desea hacer mas de un diccionario

si el usuario lo desea, puede renombrar el archivo a un nombre con el que se sienta mas cómodo.
'''

var = input("Palabras a manejar -> ").lower()
longitud = input("Longitud -> ")

dic = ""

#el siguiente for crea el alfabeto, elimina letras repetidas
for x in var:
	if dic.find(x) == -1:
		dic = dic + x 

print (f'Se generara un archivo llamado > {nombre} < que contendra el diccionario')
numero_de_claves = len(dic)**int(longitud)
print(f'El numero de palabras generadas sera -> {numero_de_claves}')

sys.setrecursionlimit(numero_de_claves) # modifica el limite de iteraciones de una funcion recursiva, limite de python 1000
print('===========================================')
continuar = input("Desea continuar? S/N -> ")

if continuar != 's':
	print('adios...')
	exit()

file = open(nombre, "w")	#se genera el archivo externo que contendra las contrase;as

palabra ="" # esta variable contiene la nueva palabra del diccionar
dic = list(dic)

for x in range(int(longitud)):
	palabra = palabra + dic[0]

#control de variables
palabra = list(palabra)		#convierte palabra a lista para poder modificar sus elementos
longitud = int(longitud)-1	#parsea longitudo para trabajarlo como entero 
variador = 1				#controla ultimo caracter para el desplazamiento
fin = dic[len(dic)-1]		#ultima letra del alfabeto


def recursivo(posicion, var):	
	pal = ''					#resultado para add al diccionario
	for x in range(len(dic)):
		palabra[posicion] = dic[x]
		for y in range(len(palabra)):
			pal = pal + str(palabra[y])
		file.write(pal + os.linesep)
		#print(f'{pal}')
		pal = ''
	comprobacion(posicion, var)

def comprobacion(posicion, var):
	#print(var)
	posicion -= var
	if posicion >= 0:
		if palabra[posicion] != fin:
			palabra[posicion] = dic[int(dic.index(palabra[posicion]))+1]
			palabra[posicion+1] = dic[0]			
			posicion += var
			var = 1
			recursivo(posicion, var)			
		else:
			posicion += var
			var += 1
			comprobacion(posicion, var)

recursivo(longitud, variador)
file.close()