#Definir una lista por asignación con 5 enteros. Mostrar por pantalla 
# solo los elementos con valor iguales o superiores a 7.

list=[10,7,3,7,2]

for x in range(len(list)):
    if list[x]>=7:
        print("El elemento ", list[x], "es mayor o igual a 7")
    else:
        print("El elemento ", list[x], "es menor a 7")