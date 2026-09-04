#Realizar un programa que pida la carga de dos 
# listas numéricas enteras de 4 elementos cada una.
# Generar una tercer lista que surja de la suma de los 
# elementos de la misma posición de cada lista.
# Mostrar esta tercer lista.

lista1=[]
lista2=[]
lista3=[]

for x in range(4):
    num1=int(input("Ingrese un numero para la lista 1: "))
    lista1.append(num1)
    
for x in range(4):
    num2=int(input("Ingrese un numero para la lista 2: "))
    lista2.append(num2)
    
for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)
    
print("La tercer lista es: ",lista3)