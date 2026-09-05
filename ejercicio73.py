1#Se debe crear y cargar una lista donde almacenar 5 sueldos.
# Ordenar de menor a mayor la lista.

sueldos=[]

for x in range(5):
    sueldo=float(input("Ingrese el sueldo: "))
    sueldos.append(sueldo)
    
for k in range(4):
    for j in range(4):
        if sueldos[j]>sueldos[j+1]:
            aux=sueldos[j]
            sueldos[j]=sueldos[j+1]
            sueldos[j+1]=aux

print("Lista ordenada de menor a mayor:")
print(sueldos)