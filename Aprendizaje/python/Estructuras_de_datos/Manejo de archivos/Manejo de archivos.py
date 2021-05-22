#---------------------##
# LECTURA Y ESCRITURA
#---------------------##
# Con la funcion open()) abre un objeto archivo, que tiene dos parametros open(nombre_archivo, modo) 
f = open("/home/cocho/Documents/curso_de_python/Aprendizaje/python/Estructuras_de_datos/Manejo de archivos/texto_prueba.txt")
# existen diferentes modos, estos nos permiten realizar diferentes acciones

### r -> Lectura, este esta predeterminado, si no hay un archivo, entonces arroja un error
g = open("/home/cocho/Documents/curso_de_python/Aprendizaje/python/Estructuras_de_datos/Manejo de archivos/texto_prueba.txt", "r")

### a -> Agregar,  abre para agregar contenido a un archivo, si este no existe lo crea
h = open("fil/home/cocho/Documents/curso_de_python/Aprendizaje/python/Estructuras_de_datos/Manejo de archivos/texto_prueba.txte", "a")

### w -> Escritura, abre un archivo para escritura, si no exite lo crea 
j = open("/home/cocho/Documents/curso_de_python/Aprendizaje/python/Estructuras_de_datos/Manejo de archivos/texto_prueba.txt", "w")

### x -> Creacion, crea un archivo especifico, arroja error si este existe
k = open("/home/cocho/Documents/curso_de_python/Aprendizaje/python/Estructuras_de_datos/Manejo de archivos/texto_prueba.txt", "x")

#-- Al lado de las letras de los modos podemos agregar otras dos letras para determinar el tipo de archivo--#

# t -> archivo de texto
q = open("/home/cocho/Documents/curso_de_python/Aprendizaje/python/Estructuras_de_datos/Manejo de archivos/texto_prueba.txt", "wt")

# b -> archivo binario (imagenes,etc.)
t = open("/home/cocho/Documents/curso_de_python/Aprendizaje/python/Estructuras_de_datos/Manejo de archivos/texto_prueba.txt", "xb")