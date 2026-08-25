#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

n=int(input("Cuantos empleados tiene la empresa:"))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
    sueldo=float(input("Ingrese el sueldo del empleado:"))
    if sueldo<=300:
        conta1=conta1+1
    else:
        conta2=conta2+1
    gastos=gastos+sueldo
    x=x+1
print("Cantidad de empleados con sueldos entre 100 y 300")
print(conta1)
print("Cantidad de empleados con sueldos mayor a 300")
print(conta2)
print("Gastos total de la empresa en sueldos")
print(gastos)