#--------------
# IF, ELSE Y ELIF
#--------------
# if se utiliza para ejecutar un codigo si se cumple una condicion
# el formato es if nombre_variable operador(=> <= < > == != is is not) y dos pu
variable= 20
if variable == 20:
  print ("tenes razon")
# else se utiliza cuando la condicion es falsa
if variable != 20:
  print('tenes razon')
else:
 print('te equivocaste')
# Elif es parecido al operador or porque si en el primer if es falso entonces se evalua la condicion de Elif y si tambien esa es falsa entonces se ejecuta el codigo dentro del Else
if variable != 20:
  print('tenes razon')
elif  variable == 20:
  print ('tenes razon')
else:
  print('te equivocaste perro')
#-----------------
#COMO FUNCIONA
#-----------------
# lo que hace es que evalua la condicion, osea, si es True o False
# en donde los operadores de comparacion son los utilizados para determinar esa condicion
#----------------
#SINTAXIS SIMPLIFICADA
#---------------
variable_verdadera= True
print('condicion verdadera') if variable_verdadera else print('caca')
# EN ESTA FORMA SOLAMENTE EVALUA SI ES TRUE O FALSE, NO FUNCIONA SI AL IF SE LE AGREGA OPERADORES DE COMPARACION