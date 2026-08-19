#Ejercicio A7 — Tabla de multiplicar  ★
#Pedir un número entero y mostrar su tabla del 1 al 10 con un for y range(), con este formato: 5 x 3 = 15. Al final, 
#mostrar "Fin de la tabla del número X".
#Pista: range(1, 11) genera del 1 al 10 (el extremo superior no se incluye).
#Para el formato podés usar f-strings: f"{n} x {i} = {n*i}". El mensaje final va fuera del ciclo (sin indentación).

num= int(input("ingrese un numero entero: "))

for i in range(1, 11):
    print(f"{num} x {i}= {num*i}")
print(f"fin de la tabla del numero {num}")
