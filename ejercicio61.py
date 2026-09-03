#Almacenar en una lista los sueldos (valores float) de 5 operarios.
# Imprimir la lista y el promedio de sueldos.

sueldos=[]
suma=0

for x in range(5):
    sueldo=float(input("Ingrese el sueldo del operario: "))
    sueldos.append(sueldo)
    suma=suma+sueldos[x]

print("La lista de sueldos es: ", sueldos)

promedio=(suma)/len(sueldos)
print("El promedio de sueldos es: ", promedio)