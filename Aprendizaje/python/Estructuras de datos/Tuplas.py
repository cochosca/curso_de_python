#-------------
# TUPLAS
#-------------
# LAS TUPLAS SON INMUTABLES
# Son como las listas pero no se puede modificar una ves declarada y se encierra entre parentesis o tambien se puede ponder sin parentesis
tupla=(1,2,3,4)
tupla2= 1,2,3,4,5
# Con las tuplas se puede hacer todo lo que se pueda hacer con una lista menos las funciones que modifican esa lista
# las funicones que sirven: len(), todas las formas de indexacion que no modificam *ver en documento listas todas las opciones*
# si queremos modificar una tupla tenemos que convertirla a una lista con la funcion list(nombre de la tupla)
tuplalista=list(tupla)
print(tuplalista)
# >>> [1,2,3,4]
# para volver a convertirla en  tupla se usa la funcion tuple(nombre de la lista)
tupla=tuple(tuplalista)
print(tupla)
# >>> (1,2,3,4)
# las tuplas pueden ser eliminadas con del
del tupla
