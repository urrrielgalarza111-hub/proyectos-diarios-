#Escribir un programa que solicite ingresar 10 notas de alumnos y
# nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

mayorigual7=0
menor7=0
i=1

while i<=10:
    nota=float(input("ingresar la  nota del alumno: "))
    if nota>=7:
        mayorigual7=mayorigual7+1
    else:
        menor7=menor7+1
        i=i+1
        
print("la cantidad de alumnos con notas mayores o iguales a 7 es: ", mayorigual7)
print("la cantidad de alumnos con notas menores a 7 es: ", menor7)
