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
# para llamar a la funcion se coloca el nombre y se ecribe el parametro
nombre_funcion(5)
# >>> [0, 1, 2, 3, 4]
