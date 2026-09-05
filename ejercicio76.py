#Cargar una lista con 5 elementos enteros.
# Ordenarla de menor a mayor y mostrarla por pantalla, 
# luego ordenar de mayor a menor e imprimir nuevamente.

numeros=[]

for x in range(5):
    num=int(input("Ingrese un numero: "))
    numeros.append(num)
    
for k in range(4):
    for j in range(4):
        if numeros[j]>numeros[j+1]:
            aux=numeros[j]
            numeros[j]=numeros[j+1]
            numeros[j+1]=aux
            
print("Lista ordenada de menor a mayor:")
print(numeros)

for k in range(4):
    for j in range(4):
        if numeros[j]<numeros[j+1]:
            aux=numeros[j]
            numeros[j]=numeros[j+1]
            numeros[j+1]=aux
            
            
print("Lista ordenada de mayor a menor:")
print(numeros)  