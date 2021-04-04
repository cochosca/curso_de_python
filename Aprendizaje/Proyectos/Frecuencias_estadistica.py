# copia los numeros en la lista
datos_bruto=[1,2,2,3,3,3,4,4,4,3,3,3,3,]
# extrae en un set todas la varibales del estudio
variable={dato for dato in datos_bruto}
# Determina la frecuencia de cada variable y la retorna
for frecuencia_variable in variable:
    print(frecuencia_variable,datos_bruto.count(frecuencia_variable),sep=": ")