# copia los numeros en la lista
numeros=[]
variables=set()
# extrae en un set todas la varibales del estudio
for numero in numeros:
    variables.add(numero)
# Determina la frecuencia de cada variable y la retorna
for frecuencia_variable in variables:
    print(frecuencia_variable,numeros.count(frecuencia_variable),sep=": ")