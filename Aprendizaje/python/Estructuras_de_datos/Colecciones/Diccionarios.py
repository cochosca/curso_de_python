#---------------------
# DICCIONARIOS
#----------------------
# Son como las colecciones como las anteriores pero estas envez de encontrar los inidices con una secuencia se utiliza una clave
# estas se encierran con llaves pero el interior es diferentes, es un conjuento de pares (clave:valor), serparados como cualquier coleccion , por comas
diccionario={"clave1": 2, 45: 3, "clave3": 4}
#  las claves pueden ser tanto CADENAS como NUMEROS y entre la clave y el valor se pone dos puntos(:)
diccionario={
    "clave1": 2,
    45: 3,
    "clave3": 4
}
#--------------
# ACCEDER A LOS VALORES
#------------
#Se puede utilizar len en los diccionarios tambien
print(len(diccionario))
# >>> 3
#para poder acceder a un elemento del diccionario se utliza la clave, esa es su funcion
print(diccionario["clave1"])
# >>> 2
# Otra manera es utilizando la funcion .get()
print(diccionario.get("clave1"))
# >>> 2
#------------
# ITERACIONES
#------------
# Cuando realizamos una iteracion a los diccionarios, lo que se itera son sus calves no sus valores
for i in diccionario:
    print(i,end=",")
# >>> clave1,45,clave3 
# Para poder obtener los valores, usamos la accion de acceder
for n in diccionario:
    print(diccionario[n],end=',')
# >>> 2,3,4
# Otra manera seria con .values()
for n in diccionario.values(): # el problema con esto es que en la iteracion no se almancena la clave somanente el valor
    print(n,end=',')
# >>> 2,3,4
# Con el metodo .items(), se puede obtener la clave como el valor pero hay que poner dos variables
for k,h in diccionario.items():
    print(k,h,end=' - ',sep=':')
# >>> clave1:2 - 45:3 - clave3:4
#----------------
# COMPROVACIONES
#-------------------
# se puede comprobar con los operadores de comparacion de miebros
print('clave1' in diccionario)
# >>> True
print('clave1' not in diccionario)
# >>> False
#---------------
# AGREGAR Y ELIMINAR
#--------------
# Se pueden MODIFICAR LOS VALORES
diccionario[45]= "caca de vaca"
print(diccionario)
# >>> {'clave1':2, 45:'caca de vaca', 'clave3':4}
# para agregar es parecido a modificar pero en esta vos pones una clave unica y un valor unico
diccionario['llave_agregada']= 34
print(diccionario)
# >>> {'clave1':2, 45:'caca de vaca', 'clave3':4, 'llave_agregada': 34}
# Para eliminar se usa la funcion .pop()
diccionario.pop('llave_agregada')
print(diccionario)
# >>> {'clave1': 2, 45: 'caca de vaca', 'clave3': 4}
# Para limpiar completamente el diccionario se usa .clear()
diccionario.clear()
print(diccionario)
# >>> {}
#eliminar el diccionario con del
del diccionario