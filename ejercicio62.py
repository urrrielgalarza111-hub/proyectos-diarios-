#Cargar por teclado y almacenar en una lista las 
# alturas de 5 personas (valores float)
#Obtener el promedio de las mismas.
# Contar cuántas personas son más altas que el promedio y 
# cuántas más bajas.

alturas=[]
suma=0

for x in range(5):
    altura=float(input("Ingrese la altura de la persona: "))
    alturas.append(altura)
    suma=suma+alturas[x]

print("La lista de alturas es: ", alturas)

promedio=(suma)/len(alturas)
print("El promedio de alturas es: ", promedio)

altos=0
bajos=0

for x in range(len(alturas)):
    if alturas[x]>promedio:
        altos=altos+1
    else:
        bajos=bajos+1

print("Personas más altas que el promedio: ", altos)
print("Personas más bajas que el promedio: ", bajos)