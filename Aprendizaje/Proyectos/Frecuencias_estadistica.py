# copia los datos(numeros o cadenas) en la lista
datos_bruto=[1,2,2,3,3,3,4,4,4,3,3,3,3,5,4,6,4,6,6,6,7,7,7,8,8,8,9,9,9,9,12,12,12,23,23,23,34,3,53,35,3,4]
# extrae en un set todas la varibales del estudio
variable={dato for dato in datos_bruto}
# Determina la frecuencia de cada variable y la retorna
for frecuencia_variable in variable:
    print(frecuencia_variable,datos_bruto.count(frecuencia_variable),sep=", ")