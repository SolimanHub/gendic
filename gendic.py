#! gendic/bin/python3
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
var = var + var.upper()
longitud = input("Longitud -> ")

dic = ""

#el siguiente for crea el alfabeto, elimina letras repetidas
for x in var:
	if dic.find(x) == -1:
		dic = dic + x 

print(f'alfabeto -> {dic}')
print (f'Se generara un archivo llamado > {nombre} < que contendra el diccionario')
numero_de_claves = len(dic)**int(longitud)
B = numero_de_claves*int(longitud)+numero_de_claves
MB = B/1048576
print(f'El numero de palabras generadas sera -> {numero_de_claves}')
print(f'El archivo pesara {B} B /{B/1024} kB /{MB} MB /{MB/1024} GB' )
print('===========================================')
continuar = input("Desea continuar? s/n -> ")
print("Generando diccionario...")

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
posicion = int(longitud)-1	#parsea longitudo para trabajarlo como entero 
variador = 1				#controla ultimo caracter para el desplazamiento
fin = dic[len(dic)-1]		#ultima letra del alfabeto
imprimir = True

while posicion >= 0:
	if imprimir:
		pal = ''					#resultado para add al diccionario
		for x in range(len(dic)):
			palabra[posicion] = dic[x]
			for y in range(len(palabra)):
				pal = pal + str(palabra[y])
			file.write(pal + os.linesep) 	# envia la palabra generada a un archivo de texto
			pal = ''						# limpia la variable pal
	posicion -= variador 					# baja un espacio para su analisis 
	if posicion == -1:
		break
	if palabra[posicion] != fin:	# compara el caracter en el espacio de posicion con el ultimo caracter del alfabeto
		palabra[posicion] = dic[int(dic.index(palabra[posicion]))+1] #disminuye una posicion en la palabra y avanza un caracter en el alfabeto
		for x in range(int(longitud)-1): # rellena con la primer letra del alfabeto todos los campos a la izquierda, cada que el script da un salto de posicion.
			if int(longitud)-x-1>posicion:
				palabra[int(longitud)-x-1] = dic[0]	
		posicion += variador 				# retorna posicion a su estado anterior, para generar las palabras con el nuevo caracter en posicion-1
		variador = 1						# retorna variador a 1 para hacer el barrido de hisquierda a derecha con las nuevas modificaciones.
		imprimir = True
	else:
		posicion += variador 			# como la posicion actual llego al final del alfabeto, avanza un espacio para verificar la siguiente posicion
		variador += 1					# var -> variador, suma 1 para desplazar la posicion hacia la izquierda
		imprimir = False

file.close()