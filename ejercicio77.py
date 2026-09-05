#Confeccionar un programa que permita cargar
# los nombres de 5 alumnos y sus notas respectivas. 
# Luego ordenar las notas de mayor a menor.
# Imprimir las notas y los nombres de los alumnos.

alumnos=[]
notas=[]

for x in range(5):
    alumno=input("ingrese el nombre del alumno: ")
    nota=float(input("Ingrese la nota del alumno: "))
    alumnos.append(alumno)
    notas.append(nota)
    
for k in range(4):
    for j in range(4-k):
        if notas[j]<notas[j+1]:
            aux1=notas[j]
            notas[j]=notas[j+1]
            notas[j+1]=aux1
            aux2=alumnos[j]
            alumnos[j]=alumnos[j+1]
            alumnos[j+1]=aux2
            
print("Lista ordenada de mayor a menor:")

for x in range(5):
    print("Alumno: ",alumnos[x]," Nota: ",notas[x])