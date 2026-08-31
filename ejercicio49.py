#Se cuenta con la siguiente información:
#Las edades de 5 estudiantes del turno mañana.
#Las edades de 6 estudiantes del turno tarde.
#Las edades de 11 estudiantes del turno noche.
#Las edades de cada estudiante deben ingresarse por teclado.
#a) Obtener el promedio de las edades de cada turno (tres promedios)
#b) Imprimir dichos promedios (promedio de cada turno)
#c) Mostrar por pantalla un mensaje que indique cual de los tres turnos 
#tiene un promedio de edades mayor

promMa=0
promTa=0
promNo=0
edadMa=0
edadTa=0
edadNo=0
suma1=0
suma2=0
suma3=0
print("TURNO MAÑANA")
for x in range(5):
    edadMa=int(input("Ingrese las edades de los alumnos turno mañana: "))
    suma1=suma1+edadMa

promMa=suma1/5
print("TURNO TARDE")
for x in range(6):
    edadMa=int(input("Ingrese las edades de los alumnos turno tarde: "))
    suma2=suma2+edadTa

promTa=suma2/6
print("TURNO NOCHE")
for x in range(11):
    edadMa=int(input("Ingrese las edades de los alumnos turno noche: "))
    suma3=suma3+edadNo

promNo=suma3/11

print("Promedio de edades de los alumnos de turno mañana: ")
print(promMa)
print("Promedio de edades de los alumnos de turno tarde: ")
print(promTa)
print("Promedio de edades de los alumnos de turno noche: ")
print(promNo)

if promMa > promTa:
    print("el mayor promedio es del turno Mañana.")
else:
    if promTa > promMa:
        print("el mayor promedio es del turno Tarde.")
    else:
        print("el mayor promedio es del turno Noche.")