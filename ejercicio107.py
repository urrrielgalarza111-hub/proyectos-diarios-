#Ejercicio A5 — Expresión condicional (operador ternario)
#Dadas las variables usuario y email (que pueden ser cadenas vacías)
#, construir registro en una sola línea:
#Si ambas contienen texto: la concatenación de usuario y email separados
#por " - ".
#Si alguna está vacía: "Datos incompletos".
#Recordá: la sintaxis es <valor_si_True> if <condición> 
#else <valor_si_False>. Y por la conversión implícita a booleano,
#una cadena vacía se evalúa como False: la condición puede ser
#directamente usuario and email.

usuario="Uriel.1011"
email="urrielgal11@gmail.com"

registro = usuario + " - " + email if usuario and email else "Datos incompletos"
print("A5) Con datos completos:", registro)

email = ""   # ahora falta el email...
registro = usuario + " - " + email if usuario and email else "Datos incompletos"
print("A5) Con email vacío:", registro)
