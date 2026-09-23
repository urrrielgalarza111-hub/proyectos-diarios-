#Ejercicio A9 — Menú interactivo
#Desarrollar un programa que muestre este menú y funcione en un ciclo while hasta que el usuario elija la opción 4.
# Cada opción se resuelve con match/case:
#1. Alta de alumno
#2. Baja de alumno
#3. Listar alumnos
#4. Salir
#Opción 1: mostrar "Alta de alumno". Opción 2: "Baja de alumno". Opción 3: "Listado de alumnos".
#Opción 4: finalizar el programa. Cualquier otro caso: "Opción inválida" (comodín _).
#Atención: decidí si la opción la guardás como int o como str, y sé consistente: si leés con input() sin convertir,
# los case deben comparar contra "1", "2"... (con comillas).

opcion=(input("Ingrese la opcion que desee"))
print("1. Alta de alumno")
print("2. Baja de alumno")
print("3. Listar alumnos")
print("4. Salir")

while opcion !=4:
    match opcion:
        case "1":
            print("Alta de alumno")
            print("-----------------------")
            opcion=(input("Ingrese la opcion que desee"))
            print("1. Alta de alumno")
            print("2. Baja de alumno")
            print("3. Listar alumnos")
            print("4. Salir")
        case "2":
            print("Baja de alumno")
            print("-----------------------")
            opcion=(input("Ingrese la opcion que desee"))
            print("1. Alta de alumno")
            print("2. Baja de alumno")
            print("3. Listar alumnos")
            print("4. Salir")
        case "3":
            print("Lista de alumnos")
            print("-----------------------")
            opcion=(input("Ingrese la opcion que desee"))
            print("1. Alta de alumno")
            print("2. Baja de alumno")
            print("3. Listar alumnos")
            print("4. Salir")
            
        