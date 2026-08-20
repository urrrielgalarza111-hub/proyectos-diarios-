#Ejercicio B7 — Proposiciones lógicas con and, or, not
#Pedir al usuario su edad (entero) y si tiene licencia de conducir (ingresar True o False). El programa debe:
#1. Usar un if con and para determinar si puede conducir (edad ≥ 18 y licencia).
#2. Usar un if con or para detectar si hay alguna condición que le impida manejar (edad < 18 o sin licencia).
#3. Usar not para mostrar un mensaje adicional si no tiene licencia.
#Atención: input() devuelve str, y la cadena "False" ¡se evalúa como verdadera por no estar vacía! 
#Convertí con una comparación: licencia = respuesta == "True".

edad=int(input("Ingrese su edad: "))
licencia = input("¿Tiene licencia de conducir? (True/False): ") == "True"

if edad >= 18 and licencia:
    print("Puede conducir.")
if edad< 18 or not licencia:
    print("No puede conducir.")
    
    