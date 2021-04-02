#-----------------
# SET
#---------------
# Es una coleccion como las listas o las tuplas, pero NO tienen orden(no se pueden indexar), NO se pueden modificar, NO puede tener elementos duplicados
# se pude eliminar y agregar elementos a los sets
#  SE UTILIZAN LLAVES
seta={1,2,3,4}
# para revisar si un elemento esta dentro del set
print(1 in seta)
# >>> True
print('caca' in seta)
# >>> False
# un set vacio se indica con set()
set_vacio=set()
print(set_vacio)
# >>> <class 'set'>
#-------------
# AGREGAR O ELIMINAR
#-------------
# con .add(valor para agregar) se puede agregar un elemento al set
seta.add("element")
print(seta)
# >>> {1,2,3,4,"element"}
#eliminar .remove y si no se encuentra el elemento te aparece un aviso
seta.remove("element")
print(seta)
# >>> {1,2,3,4}
# eliminar con .discard, elimina tambien pero si no encuentra el elemento en el set no avisa
seta.discard(2)
print(set)
# >>> {1,3,4}
# para eliminar todos los elementos de la lista se usa .clear()
seta.clear()
print(seta)
# para eliminar la variable compelta se usa tambien del
del seta