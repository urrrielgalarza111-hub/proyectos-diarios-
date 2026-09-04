#Crear y cargar una lista con 5 enteros.
# Implementar un algoritmo que identifique 
# el mayor valor de la lista

lista=[]

for x in range(5):
    num=int(input("Ingrese un numero entero: "))
    lista.append(num)
    
mayor=lista[0]
for x in range(5):
    if lista[x]>mayor:
        mayor=lista[x]
        
print("El mayor valor de la lista es: ", mayor)