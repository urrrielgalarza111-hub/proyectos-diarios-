#Ejercicio A2 — Calculadora simple
#Pedir dos números y una operación (+, -, *, /). Usar if/elif/else para calcular y mostrar el resultado. 
#Si la operación ingresada no es ninguna de las cuatro, mostrar "Operación inválida".
#Atención: ¿qué pasa si el usuario pide dividir por 0? Probalo. 
#Un programa robusto lo controla con un if antes de dividir y muestra un mensaje en lugar de "explotar" con ZeroDivisionError.

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))

operacion=input("Ingrese la operacion (+, -, *, /): ")

if operacion =="+":
    resultado=num1+num2
    print("El resultado de la suma es:", resultado)
elif operacion =="-":
    resultado=num1-num2
    print("El resultado de la resta es:", resultado)
elif operacion =="*":
    resultado=num1*num2
    print("El resultado de la multiplicacion es:", resultado)
elif operacion =="/":
    if num2 != 0:
        resultado=num1/num2
        print("El resultado de la division es:", resultado)
    else:
        print("Error: no se puede dividir por cero ")
        


