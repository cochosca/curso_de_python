# estructuras de datos: https://docs.python.org/es/3/tutorial/datastructures.html#using-lists-as-stacks
#---------------
# LISTAS POR COMPRESION
#--------------
#AGREGAR
#-------------
# APPEND (list.append())
#-------------
# funcion .append(), esta agrega un nuevo elemento a las lista y lo coloca al final
xlista=[1,'rojo']
xlista.append('blanco')
print(lista)
# >>> [1,"rojo","blanco"]
# SE PUEDEN CREAR LISTAS VACIAS, QUE PUEDEN SER RELLENADAS CON .append
lista_vacia=[]
lista_vacia.append(1)
print(lista_vacia)
# >>> [1]
# con la funcion for se puede automatizar el rellenado
los_numeros=[]
for i in range(2):
    numero=int(input("escribe un numero:" ))
    los_numeros.append(numero)
print(los_numeros)
# >>> escribe un numero: 2
# >>> escribe un numero: 3
# >>> [2,3]
#-----------
# INSERT (list.insert(indice),dato))
#----------
# inserta un elemento en una pocicion especifica de la lista y despaza al que estaba es esa pocicion a la derecha
lista=[1,3,4,5]
lista.insert(2, "caca de vaca") # insert(indice,objeto)
print(lista)
# >>> [1,3,"caca de vaca",4,5] # el 4 estaba en el indice 2 pero paso al indice 3
#-------------
# REMOVE   (.remove(dato para remover))
#-------------
# remueve el primer elemento de la lista que sea igual a x , solamente el primero que encuentra, si hay repetidos no los borra
lista.remove("caca de vaca")
print(lista)
# >>> [1,3,4,5]
# si quieres elminiar duplicados en una lista con remove se puede hacer la siguiente iteracion
los_numeros=[1,2,3,2,2,2,4,3]
for i in los_numeros:
    los_numeros.remove(2)
print(los_numeros)
# >>> [1,3,4,3]
#------------
# POP (.pop([indice]))
#-----------
#Quita el ítem en la posición dada de la lista y lo retorna. Si no se especifica un índice, a.pop() quita y retorna el último elemento de la lista
lista.pop()# elimina el ultimo elemento de la lista
# >>> 5 
lista.pop([1])
# >>> 3
#---------------
# CLEAR
#-------------
# elimina todos los elementos de la lista
lista.clear()
print(lista)
# >>> []
#--------------
# EXTEND
#--------------
# Extiende la lista agregándole todos los ítems del iterable,  es como sumar dos listas
x=[1,2,3,4]
z=['caca','vaca']
x.extend(z)
print(x)
# >>> [1,2,3,4,'caca','vaca']
#--------------
# COUNT
#-------------
# retorna el numero de veces que aparece x elemento en una lista
gg=[1,2,2,2,5,2,4,2]
print(gg.count(2))
# >>> 5
#------------
# DEL
#------------
# Elimina un item de una lista sin retornar su valor como la funcion pop, tambien tiene la capacidad de eliminar secciones de una lista indicando un intervalo
del lista[1]
print(lista)
# >>>  [3,4,5]
del lista[:2]
# >>> [] # elimino todos los elementos 
# tambien se pude usar para eleminar varibles
del lista