# Generacion de un pequeño alfabeto tomando como referencia palabras con las que el objetivo se identifique,
# apellido, nombre, nombre de familiares, mascotas, lugares, gustos, etc
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

print('===========================================')
continuar = input("Desea continuar? s/n -> ")
print("Generando diccionario...")

if continuar != 's':		#para continuar ejecucion 's' minuscula
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
imprimir = True

while longitud >= 0:
	if imprimir:
		pal = ''					#resultado para add al diccionario
		for x in range(len(dic)):
			palabra[longitud] = dic[x]
			for y in range(len(palabra)):
				pal = pal + str(palabra[y])
			file.write(pal + os.linesep) 	# envia la palabra generada a un archivo de texto
			pal = ''						# limpia la variable pal
	longitud -= variador 					# baja un espacio para su analisis 
	if longitud == -1:
		break
	if palabra[longitud] != fin:	# compara el caracter en el espacio de posicion con el ultimo caracter del alfabeto
		palabra[longitud] = dic[int(dic.index(palabra[longitud]))+1] #disminuye una posicion en la palabra y avanza un caracter en el alfabeto
		palabra[longitud+1] = dic[0]	# empieza desde la primera posicion del alfabeto, la posicion anterior de la palabra
		longitud += variador 				# retorna posicion a su estado anterior, para generar las palabras con el nuevo caracter en posicion-1
		variador = 1						# retorna variador a 1 para hacer el barrido de hisquierda a derecha con las nuevas modificaciones.
		imprimir = True
	else:
		longitud += variador 			# como la posicion actual llego al final del alfabeto, avanza un espacio para verificar la siguiente posicion
		variador += 1					# var -> variador, suma 1 para desplazar la posicion hacia la izquierda
		imprimir = False
print("Diccionario terminado")
file.close()