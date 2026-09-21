#Ejercicio A2 — Calculadora simple
#Pedir dos números y una operación (+, -, *, /). 
# Usar if/elif/else para calcular y mostrar el resultado. 
# Si la operación ingresada no es ninguna de las cuatro,
# mostrar "Operación inválida".
#Atención: ¿qué pasa si el usuario pide dividir por 0? Probalo.
# Un programa robusto lo controla con un if antes de dividir y
# muestra un mensaje en lugar de "explotar" con ZeroDivisionError.

num1=int(input("Ingrese el primer numero "))
ope=input("+,-,*,/ : ")
num2=int(input("Ingrese el segundo numero "))

if ope=="+":
    print(num1+num2)
else:
    if ope=="-":
        print(num1-num2)
    else:
        if ope=="*":
            print(num1*num2)
        else:
            if ope=="/":
                print(num1/num2)