# copia los numeros en la lista
numeros=[]
# extrae en un set todas la varibales del estudio
variable={numero for numero in numeros}
# Determina la frecuencia de cada variable y la retorna
for frecuencia_variable in variables:
    print(frecuencia_variable,numeros.count(frecuencia_variable),sep=": ")