numeros=[5, 2, 4, 9, 7, 4, 5, 6, 5, 7, 7, 5, 5, 2, 10, 5, 6, 5, 4, 5, 8, 8, 4, 0, 8, 4, 8, 6, 6, 3, 6, 7, 6, 6, 7, 6, 7, 3, 5, 6, 9, 6, 1, 4, 6, 3, 5, 5, 6, 7]
variables=set()
# extrae en un set todas la varibales del estudio
for numero in numeros:
    variables.add(numero)
# Determina la frecuencia de cada variable y la retorna
for frecuencia_variable in variables:
    print(frecuencia_variable,numeros.count(frecuencia_variable),sep=": ")



