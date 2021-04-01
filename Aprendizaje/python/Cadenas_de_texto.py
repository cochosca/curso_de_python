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