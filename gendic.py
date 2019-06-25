####! /bin/python
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

for x in range(int(longitud)): # este for genera la primer palabra del diccionario, la cual se usara como base para crear el resto
	palabra = palabra + dic[0]

#control de variables
palabra = list(palabra)		#convierte palabra a lista para poder modificar sus elementos
longitud = int(longitud)-1	#parsea longitudo para trabajarlo como entero 
variador = 1				#controla ultimo caracter para el desplazamiento
fin = dic[len(dic)-1]		#ultima letra del alfabeto


# recursivo() esta funcion toma los datos de comprobacion() y genera la palabra a partir de ellos
# los caracteres de las palabras se van modificando de derecha a izquierda, como un sistema numerico
# posicion indica el subindice que se modifica en la cadena
# var el nivel de variacion
def recursivo(posicion, var):	
	pal = ''					#resultado para add al diccionario
	for x in range(len(dic)):
		palabra[posicion] = dic[x]
		for y in range(len(palabra)):
			pal = pal + str(palabra[y])
		file.write(pal + os.linesep) 	# envia la palabra generada a un archivo de texto
		pal = ''						# limpia la variable pal
	comprobacion(posicion, var)

'''
comprobacion() se encarga de seguir el avance e iteracion a traves de los campos de la cadena
si la cadena tiene tamaño 3, posicion comienza con el subindice 2, recordando que el conteo de subindices comienza en 0
var "desplaza el cursor" hacia la izquierda o derecha segun corresponda.
'''
def comprobacion(posicion, var):
	#print(var)
	posicion -= var 					# baja un espacio para su analisis 
	if posicion >= 0:					# si posicion es menor que cero termina la ejecucion
		if palabra[posicion] != fin:	# compara el caracter en el espacio de posicion con el ultimo caracter del alfabeto
			palabra[posicion] = dic[int(dic.index(palabra[posicion]))+1] #disminuye una posicion en la palabra y avanza un caracter en el alfabeto
			palabra[posicion+1] = dic[0]	# empieza desde la primera posicion del alfabeto, la posicion anterior de la palabra
			posicion += var 				# retorna posicion a su estado anterior, para generar las palabras con el nuevo caracter en posicion-1
			var = 1							# retorna variador a 1 para hacer el barrido de hisquierda a derecha con las nuevas modificaciones.
			recursivo(posicion, var)		# llama a recursivo para tabular las modificaciones y generar las nuevas palabras en el archivo externo.
		else:
			posicion += var 			# como la posicion actual llego al final del alfabeto, avanza un espacio para verificar la siguiente posicion
			var += 1					# var -> variador, suma 1 para desplazar la posicion hacia la izquierda
			comprobacion(posicion, var)	# se llama a si mismo para verificar las posiciones restantes, hasta encontrar un subindice de la palabra que sea diferente al final del alfabeto.

recursivo(longitud, variador)
file.close()