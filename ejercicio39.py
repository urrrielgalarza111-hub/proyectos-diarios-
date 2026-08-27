#Escribir un programa que solicite por teclado 10 notas de
# alumnos y nos informe cuántos tienen
# notas mayores o iguales a 7 y cuántos menores.

may7=0
men7=0
for x in range(10):
    nota=int(input("ingrese nota del alumno: "))
    if nota>=7:
        may7=may7+1
    else:
        men7=men7+1
        
print("alumnos con nota menor a 7: ")
print(men7)
print("alumnos con nota mayor igual a 7: ")
print(may7)