#Ejercicio A5 — Expresión condicional (operador ternario)
#Dadas las variables usuario y email (que pueden ser cadenas vacías), construir registro en una sola línea:
#Si ambas contienen texto: la concatenación de usuario y email separados por " - ".
#Si alguna está vacía: "Datos incompletos".
#Recordá: la sintaxis es <valor_si_True> if <condición> else <valor_si_False>.
#Y por la conversión implícita a booleano, una cadena vacía se evalúa como False: la condición puede ser directamente usuario and email.

usuario=input("Ingrese el nombre de usuario: ")
email=input("Ingrese el email: ")

registro=usuario + " - " + email if usuario and email else "Datos incompletos"

