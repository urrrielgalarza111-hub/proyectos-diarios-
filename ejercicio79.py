#Crear una lista por asignación. La lista tiene que tener
# cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
#Imprimir sus elementos accediendo de diferentes modos.

lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

print(lista)
#Imprimir el primer elemento de la lista
print(lista[0])
print("-------------------------------")
#Imprimir el segundo elemento de la lista
print(lista[0][0])
print("-------------------------------")
#Imprimir todos los elementos de la primer componente de la lista

for x in range(len(lista[0])):
    print(lista[0][x])
    
print("--------------------------------")
#Imprimir todos los elementos de todos los componente de la lista

for x in range(len(lista)):
    for y in range(len(lista[x])):
        print(lista[x][y])
        
