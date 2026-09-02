#Definir por asignación una lista con 8 elementos enteros. 
# Contar cuantos de dichos valores almacenan un valor superior a 100.

lista=[10,200,300,11,99,100,101,102]

for x in range(len(lista)):
    if lista[x]>100:
        print("El elemento ", lista[x], " es mayor a 100")
    else:
        print("El elemento ", lista[x], " es menor o igual a 100")