tupla=(13,1,8,3,2,5,8)
lista=[]
for numero_lista in tupla:
    if numero_lista > 4:
        continue
    lista.append(numero_lista)
print(lista)