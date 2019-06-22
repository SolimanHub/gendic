#! /bin/python
# Generacion de un peque;o alfabeto tomando como referencia palabras con las que la victima se identifique,
# apellido, nombre, nombre de familiares, mascotas, lugares, gustos, etc

var = input("Palabras a manejar -> ").lower()
longitud = input("Longitud -> ")

#diccionario = "0123456789.#$"
"""d1 = ""
for x in var:
	if x != " ":
		if diccionario.find(x) == -1:
			d1 = d1 + x
			pass
		pass
	pass
d1 = d1 + d1.upper()
diccionario = diccionario + d1

print(f'{len(diccionario)}{" "}{diccionario}')
"""
dic = ""
#el siguiente for crea el alfabeto, elimina letras repetidas
for x in var:
	if dic.find(x) == -1:
		dic = dic + x 

print (f'letras del alfabeto -> {len(dic)}')
numero_de_claves = len(dic)**int(longitud)
print(f'El numero de palabras probables es: {numero_de_claves}')

palabra ="" # esta variable contiene la nueva palabra del diccionar
dic = list(dic)

for x in range(int(longitud)):
	palabra = palabra + dic[len(dic)-1]

palabra = list(palabra)
longitud = int(longitud)
variador = 0
comodin = 1

while longitud > 0:
	for x in range(len(dic)):
		palabra[longitud-1] = dic[x]
		print(palabra)
	longitud = longitud -1