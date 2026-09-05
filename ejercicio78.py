#Crear y cargar en un lista los nombres de 5 países y
# en otra lista paralela la cantidad de habitantes del mismo. 
# Ordenar alfabéticamente e imprimir los resultados.
# Por último ordenar con respecto 
# a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

paises=[]
habitantes=[]

for x in range(5):
    pais=input("Ingrese el nombre del pais: ")
    habitantess=int(input("Ingrese la cantidad de habitantes del pais: "))
    paises.append(pais)
    habitantes.append(habitantess)
    
for k in range(4):
    for j in range(4):
        if paises[j]>paises[j+1]:
            aux1=paises[j]
            paises[j]=paises[j+1]
            paises[j+1]=aux1
            aux2=habitantes[j]
            habitantes[j]=habitantes[j+1]
            habitantes[j+1]=aux2
            
print("Lista ordenada alfabéticamente:")
for x in range(5):
    print("Pais: ",paises[x]," Habitantes: ",habitantes[x])
    
for k in range(4):
    for j in range(4):
        if habitantes[j]<habitantes[j+1]:
            aux1=habitantes[j]
            habitantes[j]=habitantes[j+1]
            habitantes[j+1]=aux1
            aux2=paises[j]
            paises[j]=paises[j+1]
            paises[j+1]=aux2
            
print("Lista ordenada por cantidad de habitantes (de mayor a menor):")
for x in range(5):
    print("Pais: ",paises[x]," Habitantes: ",habitantes[x])
    
    
