# copia los datos(numeros o cadenas) en la lista
datos_bruto=[58,63,638,45,45,49,50,51,55,56,56,56,56,3,63]

# extrae en un set todas la varibales del estudio
variable={dato for dato in datos_bruto}

# coversion a lista
variable = list(variable)

# Determina la frecuencia de cada variable
frec_variable = [datos_bruto.count(i) for i in variable]

# calcula la frecuencia acumulada
frec_acum = []
acumulacion= int()
for i in frec_variable:
   acumulacion +=i
   frec_acum.append(acumulacion)

# calcula la frecuencia relativa
N = frec_acum[-1]
frec_rela = [round(i/N,2) for i in frec_variable]

# calcula la frecuencia relativa acumulada
frec_rela_acum =[]
acumulacion_rela = float()
for n in frec_rela:
    acumulacion_rela += n 
    frec_rela_acum.append(round(acumulacion_rela,1))

# calcula el porcentaje
porcentaje = ['{:1.1%}'.format(i*1) for i in frec_rela]

# anidar todas las listas
tabla_frec = []
for i,z,x,c,v,b in zip(variable,frec_variable,frec_acum,frec_rela,frec_rela_acum,porcentaje):
  tabla_frec.append([i,z,x,c,v,b])

