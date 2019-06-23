#! /bin/python
# Generacion de un peque;o alfabeto tomando como referencia palabras con las que la victima se identifique,
# apellido, nombre, nombre de familiares, mascotas, lugares, gustos, etc

var = input("Palabras a manejar -> ").lower()
longitud = input("Longitud -> ")

dic = ""

#el siguiente for crea el alfabeto, elimina letras repetidas
for x in var:
	if dic.find(x) == -1:
		dic = dic + x 

print (f'letras del alfabeto -> {len(dic)}')
numero_de_claves = len(dic)**int(longitud)
print(f'Ultima letra del alfabeto -> {dic[len(dic)-1]}')
print(f'El numero de palabras generadas sera -> {numero_de_claves}')
print('===========================================')
input("Pulsa una tecla para continuar...") 

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
		print(f'{pal}')
		pal = ''
	comprobacion(posicion, var)

def comprobacion(posicion, var):
	print(var)
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