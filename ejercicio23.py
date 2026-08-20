#Ejercicio B11 — Integrador: menú con funciones
#Reescribí el menú del ejercicio A9 para que sea un programa principal que coordina módulos,
#como en la diapositiva de modularización de la Clase 4:
#Opción 1: pedir un nombre y mostrar el resultado de saludar(nombre).
#Opción 2: pedir tres números y mostrar maximo3(a, b, c).
#Opción 3: pedir una cantidad de segundos y mostrar el resultado de a_hms(segundos) con el formato "X horas, Y minutos, Z segundos".
#Opción 4: salir. Otro valor: "Opción inválida".
#Las funciones deben importarse desde mis_funciones.py (ejercicio B10): el menú solo pide datos, llama funciones y muestra resultados.
#Para pensar: fijate el reparto de responsabilidades:
#    las funciones devuelven valores y no usan input ni print; el programa principal es el único que habla con el usuario.
#   Esa separación es exactamente lo que las hace reutilizables.

def main():
    from mis_funciones import saludar, maximo3, a_hms

    while True:
        print("\nMenú:")
        print("1. Saludar")
        print("2. Máximo de tres números")
        print("3. Conversión de segundos a horas, minutos y segundos")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            nombre = input("Ingrese un nombre: ")
            print(saludar(nombre))
        elif opcion == "2":
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            num3 = int(input("Ingrese el tercer número: "))
            print(f"El mayor es: {maximo3(num1, num2, num3)}")
        elif opcion == "3":
            segundos = int(input("Ingrese la cantidad de segundos: "))
            h, m, s = a_hms(segundos)
            print(f"{h} horas, {m} minutos, {s} segundos")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")