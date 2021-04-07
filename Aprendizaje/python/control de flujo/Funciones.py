#-------##-------#
# FUNCIONES
#-------##-------#
# Una función te permite DEFINIR UN BLOQUE DE CODIGO REUTILIZABLE que se puede ejecutar muchas veces dentro de tu programa.
# Las funciones se definen(darle nombre y crearla) con  def <nombre_de_la_funcion> (parametos para ingresar)
def nombre_funcion(parametro):
    """Descripcion de lo que hace la funcion para la documentacion.""" # lo que se pone aqui es para describir que hace la funcion
    #Esto es para que las herramientas de documentación de Python puedan extraer esto, para generar documentación automáticamentente.
    lista_automatica=[i for i in range(parametro)]
    print(lista_automatica)
# Debajo de la funcion se puede podern CUALQUIER BLOQUE DE CODIGO
# para llamar a la funcion se coloca el nombre y se ecribe el argumento en donde se puso el parametro
nombre_funcion(5)
# >>> [0, 1, 2, 3, 4]
#---------------------------
# PARAMETROS Y ARGUMENTOS
#---------------------------
#  PARAMETRO= variable en donde se ponde los valores
#  ARGUMENTO= valor que se pone en el parametro
# En las funciones se pueden poner multiples parametros
def m(v,s):
    print(v,s,sep=" - ")
m(2, 3)
# >>> 2 - 3
# Se puede PONER ARGUNENTOS al definir la función, pero estos pueden ser reemplazados si agregamos nuevos argumentos al llamar a la función
def caca(a=0,b=0): #SI O SI LOS DOS PARAMETROS TIENENQUE TENER UN ARGUMENTO
    return a + b
caca()
# >>> 0     #SI NO PONGO NADA UTILIZA LOS ARGUMENTOS QUE ESTABLECI DE FORMA PREDETERMINADA
caca(2,3)
# >>> 5
#------------
# RETURN
#-------------
# Su funcion es retorna un valor en una función. 
def h(x):
    return x    # retornara el valor 2 a la funcion, osea esa funcion vale 2 ahora
print(h(2))     # para poder ver lo retornado se tiene que imprimir la funcion
# >>> 2
#  Si la funcion return no se le coloca una expresión como argumento retorna None
def h(x):
    return
print(h(2))
# >>> None