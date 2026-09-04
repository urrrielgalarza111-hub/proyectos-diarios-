#En un curso de 4 alumnos se registraron las notas de sus exámenes 
# y se deben procesar de acuerdo a lo siguiente:
#a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos 
# listas paralelas)
#b) Realizar un listado que muestre los nombres, notas y condición 
# del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor 
# o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar 
# "Insuficiente" si la nota es inferior a 4.
#c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

alumnos=[]
notas=[]
condicion=[]
for x in range(4):
    alumno=input("Ingrese el nombre del alumno: ")
    nota=int(input("ingrese la nota del alumno: "))
    alumnos.append(alumno)
    notas.append(nota)
    
    if notas[x]>=8:
        condicion.append("Muy bueno")
    else:
        if notas[x]>=4 and notas[x]<8:
            condicion.append("Bueno")
        else:
            condicion.append("Insuficiente")
            
print("Listado de alumnos, notas y condicion: ")
for x in range(4):
    print("alumno: ",alumnos[x], "/ nota: ",notas[x],  "/ condicion: ",condicion[x])

cantidad=0
for x in range(4):
    if condicion[x]=="Muy bueno":
        cantidad=cantidad+1
        
print("La cantidad de alumnos con la leyenda 'Muy Bueno' es: ",cantidad)