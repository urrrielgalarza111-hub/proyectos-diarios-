#Crear una lista y almacenar los nombres de 5 países.
# Ordenar alfabéticamente la lista e imprimirla

paises=[]

for x in range(5):
    pais=input("Ingrese el nombre del pais: ")
    paises.append(pais)
    
for k in range(4):
    for j in range(4):
        if paises[j]>paises[j+1]:
            aux=paises[j]
            paises[j]=paises[j+1]
            paises[j+1]=aux
            
print("Lista ordenada alfabéticamente:")
print(paises)