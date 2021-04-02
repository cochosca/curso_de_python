#----------------
# WHILE
#---------------
# El bucle while ejecuta un CODIGO cuando la condicion establecida sea verdadera
#IMPORTANTE: cualquier valor entero que no sea cero es verdadero; CERO ES FALSO
x = 20
while x == 20:
    print('es correcto')
# esto va a provocar que se ejecuque infinitamente o hasta donde aguante la computadora
#Para poder para esa ejecucion para evitar que la computadoras se crashee se preciona
#   Ctrl + C, en la consola
# Si quiero realizar un intervalo del 1 al 10
z=1
while z < 11:
    print(z)
    z+=1    # Aqui sumamos a la variable x un 1 para que cada  vez que se ejecute el codigo aumente de valor y no se ejecute de forma infinita
#TAMBIEN SE PUEDE AGREGAR Else para ejecutar un codigo cuando termina el ciclo

while z < 11:
    print(z)
    z+=1    
else:
    print('termino el ciclo')
#---------------------
# CICLO FOR
#---------------------
# ciclo for realiza una iteracion (Iteración significa repetir varias veces un proceso con la intención de alcanzar una meta deseada, objetivo o resultado)
# ITERA sobre los ítems de CUALQUIER SECUENCIA (lista, cadena de texto, rango)en el orden que aparecen en la secuencia, en donde, a cada itearcion se SE EJECUTA UN CODIGO.
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))  # Imprime el primer elemento de la lista y cantidad de elementos de la cadena de caracteres
#>>> cat 3
#>>> window 6
#>>> defenestrate 12
# tambien podemos agregar al final del ciclo for el comando ---ELSE---
y= "comida"
for n in y:
    print(n)
else:
    print('fin del ciclo')
#----
# RANGE
#----
# la funcion integrada range(), hace que el ciclo for ITERE sobre un una secuencia de numeros, que genera una progresion aritmetica
for i in range(9):
    print(i,end="-")    # la funcion end="-" sirve para eviar los saltos de linea y egregamos un simbolo a ese espacio
#>>> 0-1-2-3-4-5-6-7-8-
#----
# BREAK
#-----
# este comando se utiliza para romber el ciclo for, creo que se utiliza para evitar que se realize toda la iteracion, por ejemplo cuando buscas algo y encontras queres que pare la iteracion.
#por ejemplo si a la cadena de caracteres 'caca' queremos que solo imprima la letra a y una sola vez, necesitamos el comando break

for l in 'caca':
    if l == 'a':
        print(l)
# >>> a
# >>> a
# como el ciclo for encontro 2 "a" entonces imprimio 2 veces pero nosotros queremos que sea una sola vez
#Entonces usamos break para que corte el ciclo en la primera vez que el ciclo imprima "a"
for l in 'caca':
    if l == 'a':
        print(l)
        break
# >>> a
# inclusive si agregamos else al final del ciclo o cualquier otro codifo debajo del BREAK no se ejecuta ese comando porque break rompe la cadena, es decir todo lo que este despues de break no se ejecuta.
for nu in ' roberta tototo':
    if nu == 'o':
        print(nu)
        break
        print('caca de vaca')
        uno = 5
        while uno > 0:
            print(uno)
            uno-=1
else:
    print('moco')
# >>> o
#----------------
# CONTINUE
#----------------
# esta funcion hace que se pase al siguiente ciclo cuando se cumple una condicion, todo el codigo que este debajo de continue no se ejecutara sino se saltara al siguiente ciclo
# A diferncia de la funcion break, esta continua con el siguiente ciclo cuando se cumple una condicion y break rompe la iteracion por completo
for i in range(10):
    if i%2 == 0:
        continue #si el residuio de la division es igual que cero se salta a la siguiente iteracion
    print(i,end="-")
# >>> 1-3-5-7-9
#---------------
# PASS
#---------------
#es como una marca de lugar para una función o un cuerpo condicional cuando estás trabajando en código nuevo, lo cual te permite pensar a un nivel de abstracción mayor.
x=24
if x > 34:
    print('vaca')
else:
    pass    
# como nose que poner en else pero no quiero que se rompa el codigo pongo pass, que no hace nada pero permite que se ejecute correctamente
# es un recordatorio de que tengo que poner codigo en donde dice pass