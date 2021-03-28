#----------------
#WHILE
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
#CICLO FOR
#---------------------
# ciclo for realiza una iteracion(Iteración significa repetir varias veces un proceso con la intención de alcanzar una meta deseada, objetivo o resultado)
# ITERA sobre los ítems de CUALQUIER SECUENCIA (una lista o una cadena de texto)en el orden que aparecen en la secuencia.
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))  # Imprime el primer elemento de la lista y cantidad de elementos de la cadena de caracteres
#>>> cat 3
#>>> window 6
#>>> defenestrate 12