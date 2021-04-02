#link: https://docs.python.org/es/3/tutorial/introduction.html
#-----------
#NUMEROS
#------------
#IMPORTANTE: cualquier valor entero que no sea cero es verdadero; CERO ES FALSO
#Numeros enteros
int = 2  
# o puede ser negativo
int = -1
#Numeros reales, osea que puede tener decimales
float = 9.8
float = -9.9
#valor absoluto = abs()
print(abs(-15))
#Numeros complejos
complex=3+5j #la j o J se utiliza como el numero imaginario
#------------
#CADENAS DE TEXTO
#------------
#link mas especifico: https://www.mclibre.org/consultar/python/lecciones/python-cadenas.html
str="esta es una cadena de caracteres"
#sumar cadena de caracteres
suma_de_caracteres= "caca"+ " con cara de alpaca"
#------------
#BOOLEANOS
#-----------
#hay dos valores que significan encendido o apagado(true or false), para indicar si es verdadero o es falso, SIEMPRE EN MAYUSCULA LA PRIMERA LETRA
bool=True
bool=False
#-----------
#ENTRADAD DE DATOS
#-----------
#input()
#esto hace que en la terminal tengamos que ingredar un dato, cualquiera sea
caca=int(input("se puede escribir un texto tambien: "))
print (caca)
#----------
#NONE
#---------
#se utiliza con frecuencia para representar la ausencia de un valor
variable=None
# esta varible esta sin ningun valor y tiene el potencial de que se le agrege un valor
