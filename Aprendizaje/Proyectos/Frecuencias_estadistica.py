# copia los datos(numeros o cadenas) en la lista
datos_bruto=[38,45,45,49,50,51,55,56,56,56,56,58,63,63,63]
# extrae en un set todas la varibales del estudio
variable={dato for dato in datos_bruto}
# Determina la frecuencia de cada variable y la retorna
for frecuencia_variable in variable:
    print(frecuencia_variable,datos_bruto.count(frecuencia_variable),sep=", ")