# LAS CADENAS DE TEXTO DE PYTHON SON INMUTABLES, ES DECIR, NO SE PUEDEN MODIFICAR SU CONTENIDO
#------------
# INDEXACION
#-----------
# indexar es obtener un indice numerico, en python se cuenta desde 0
# es decir, cada letra de la cadena tiene asignado un indice numerico para que se pueda acceder al ella, esta misma funcion sirve para las listas
# P Y T H O N
# 0 1 2 3 4 5
# Estos con los indices positivos, tambien se pueden usar indices negativos
#   P   Y   T   H   O   N
#  -6  -5  -4  -3  -2  -1
# con los indices negativos se empieza a contar desde el -1, se puede llamar navegacion inversa, te permite navegar por los ultimos indices mas rapidamente
# Para poder indexar en una cadena se tiene que poder el indice entre corchetes
py="python"
print(py[0])
# >>> p
#tambien se puede pedir un rango
print(py[0:3])
# >>> pyth
# hay otras formas de mostrar el rango, si quiero indexar desde el primer indice hasta un determinado indice se pone asi
print(py[:3])
# >>> pyth
# si quiero indexar desde un indice determnado hasta el final se pone asi
print(py[3:])
# >>> hon
# si quiero indexar todos los indices
print(py[:])
# >>> python
#----------
#CARACTELES ESPECIALES
#----------
#PARA QUE FUNCIONEN LOS CARACTELES ESPECIALES TIENEN QUE ESTAR DENTRO DE LA CADENA
#comilla doble: \"
print("Las comillas dobles \" delimitan cadenas.")
# >>> Las comillas dobles " delimitan cadenas.
#comilla simple: \'
print('Las comillas simples \' delimitan cadenas.')
# >>> Las comillas simples ' delimitan cadenas.
# Salto de linea: \n
print("Una línea\nOtra línea")
#>>>Una línea
#>>>Otra línea
#tabulador: \t
print("1\t2\t3")
#>>> 1  2   3
#-----------------
#COMILLAS TRIPLES
#----------------
#Las comillas triples permiten que las cadenas ocupen MAS DE UNA LINEA
print("""Esto es una cadena
que ocupa
  varias líneas""")
#Pero las comillas triples se utilizan sobre todo con una finalidad específica: la documentación de MODULOS, FUNCIONES, CLASES o METODOS.
#Son cadenas que se escriben al principio del elemento describiendo lo que hace el elemento. 
# No producen ningún resultado en el programa, pero las herramientas de documentación de Python pueden extraerlas para generar documentación automáticamente.
def licencia():
    """Escribe la licencia de estos apuntes"""
    print("Copyright 2013 Bartolomé Sintes Marco")
    print("Licencia CC-BY-SA 4.0")
    return
#------------------
#CADENAS LARGAS
#-----------------
#las líneas de código no deben contener más de 79 caracteres, para facilitar la legibilidad.
#Si un programa contiene cadenas muy largas, las cadenas se pueden simplemente partir en varias cadenas.
print("Esta línea está cortada en dos líneas de menos de 79 caracteres "
          "partiendo la cadena en dos")
#>>> Esta línea está cortada en dos líneas de menos de 79 caracteres partiendo la cadena en dos
#También se puede escribir el carácter contrabarra (\) para partir una cadena en varias líneas.
print("Esta línea está cortada en dos líneas de menos de 79 caracteres \
partiendo la cadena en dos")
#>>> Esta línea está cortada en dos líneas de menos de 79 caracteres partiendo la cadena en dos
#--------------------
#CADENAS "f"
#--------------------
#Esta notación para cadenas llamada cadenas "f", simplifica la inserción de variables y expresiones en las cadenas
#contiene variables y expresiones entre llaves ({}) que se sustituyen directamente por su valor, tambien se agrega la letra f al comienzo.
nombre = "Pepe"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años.")
#>>> Me llamo Pepe y tengo 25 años.
#-----------------------
# FUNCION END="-"
#-----------------------
# la funcion en lo que hace es evitar que se realice un salto cuando se imprima una cadena diferente, y le agrega un simbolo entre las cadenas para diferenciarlas, PUEDE SER CUALQUIER CARACTER(2,#,A)
print('caca ',end="%")
print(' vaca')
# >>> caca % vaca
# si no ponemos end="-" se realiza el salto
print('caca')
print('vaca')
# >>> caca
# >>> vaca