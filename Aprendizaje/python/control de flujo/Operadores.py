#link: https://docs.python.org/es/3/library/stdtypes.html#typesnumeric
#----------
#OPERADORES NUMERICOS
#----------
#suma y resta
s=34+43-55
#multiplicacion y division
x=4*3   #multiplicacion
z=3/4   #division con resultado DECIMAL
d=3//4  #division con resultado ENTERO
v=3%4   # resto o residuo de la division, esto nos puede servir para determinar si es par o impar
#potenciacion y radicacion
b=3**4  #potenciacion 3 con 4 de exponente
n=sqrt(25)  #Raiz al cuadrado, el resultado es decimal siempre
#para que funcione la funcion sqrt tenemos que importar de libreria math
from math import sqrt
#-------------------
# OPERADORES UNARIOS
#-------------------
# Estos operadores modifican a un solo operando
a = -1 # hacer que el valor sea negativo
b = +1 # determinar que el valor es positivo
b = ~b # esto invierte el simbolo
print(b)
# >>> -1
#-------------
# OPERADORES DE ASIGNACION
#-------------
x=3     # el operador "=" sirve para asigan un informacion a la variable
x+= 2   # x = x+2 # El operador "+=" sirve para sumar valores a variables que ya tienen informacion, Funciona para todo tipo de datos
Caca="pepe"
Caca+= "sapo"   # La respuesta va a ser "pepesapo"
x-= 8   #x = x-8 # El operador resta valores a la variable, SOLO FUNCIONA CON NUMEROS
x*= 34  # x=  x*34 # Multiplica un valor por la variable, SOLO FUNCIONA CON NUMEROS
x/= 25  # x = x/25 # Divide un valor por la variable, con resultado DECIMAL, Solo funciona con numeros
x//= 25 # lo mismo pero el resultado es entero
x**=2   # x = x ** 2 # potenciacion a los valores de la variable
x%=3    # x = x % 3 # El resultado es el resto de la divicion entre x y 3
#---------------
#OPERADORES DE COMPARARCION
#--------------
3 < 4   # 3 es estrictamente menor que 4, DONDE LA BOCA APUNTE ES EL MAYOR
3 <= 4  # 3 es  menor o igual que 4
3 > 2   # 3 es estrictamente mayor que 2
3 >= 2  # 3 es mayor o igual que 2
3 == 3  # 3 es igual que 3, Se usa == para comparar valores. Se usa cuando se desea saber si dos variables tienen el mismo valor.
3 != 6  # 3 es diferente que 6
3 is 3  # igualdad a nivel de identidad (Son el mismo objeto), Se usa is para comparar objetos. Se usa cuando se desea saber si dos variables se refieren literalmente al mismo objeto.
3 is not 4 #desigualdad a nivel de identidad (no son el mismo objeto)
vaca=[1,2,3]
3 in vaca # 3 esta en la lista vaca, se utiliza para comprobar que un elemento esta o no detnro de una lista, ES MAYORMENTE UTILIZADO EN FOR PERO SE PUEDE USAR EN IF
4 not in vaca # 4 no esta en la lista vaca
#---------------
#OPERADORES BOOLEANOS O DE LOGICA
#---------------
# ESTOS SE COMPLEMENTAN CON LOS DE COMPARACION EN LOS CICLOS Y SENTECIAS
# estos trabajan con logica cortocircuitada, es decir, como en una corriente electrica para que la corriente continue tiene que dejar pasar la corriente
# De esta manera para que el segundo termino sea evaluado, el primero tiene que cumplir una condicion, ya sea ser VERDADER O FALSO para que se pueda evaluar el segundo
X or y  # X o y, si x es falso, entonces se evalua y, si es verdadero solo x
#ejemplo=23
#w=34
#v=23
#if ejemplo== v or w:
#    print("es correcto")
x and y # x & y, si x es verdadero, entonces evalua y, si es falso solo x
not x   # si x es falso, entonces True, sino False 
#if not x == A: # si x no es igual a A)
#   print ("es diferentes") 