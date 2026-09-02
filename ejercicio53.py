#Definir una lista que almacene 5 enteros.
# Sumar todos sus elementos y mostrar dicha suma.

list=[10,7,3,7,2]
suma=0
x=0
while x<len(list):
    suma=suma+list[x]
    x=x+1
    
print("La lista es: ", list)
print("La suma de los elementos de la lista es: ", suma)
