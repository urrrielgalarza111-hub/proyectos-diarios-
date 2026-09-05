#Solicitar por teclado la cantidad de empleados que tiene la empresa.
# Crear y cargar una lista con todos los sueldos de dichos empleados.
# Imprimir la lista de sueldos ordenados de menor a mayor.

sueldos=[]

emplea=int(input("Ingrese la cantidad de empleados: "))

for x in range(emplea):
    sueldo=float(input("Ingrese el sueldo: "))
    sueldos.append(sueldo)
    
for k in range(emplea-1):
    for j in range(emplea-1):
        if sueldos[j]>sueldos[j+1]:
            aux=sueldos[j]
            sueldos[j]=sueldos[j+1]
            sueldos[j+1]=aux
            
print("Lista ordenada de menor a mayor:")
print(sueldos)