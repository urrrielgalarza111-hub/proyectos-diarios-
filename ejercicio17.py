#Ejercicio B5 — Limpieza y normalización de texto
#Estandarizar la entrada de nombres de usuarios que vienen con errores comunes:
#a. Pedir al usuario su nombre completo.
#b. Eliminar espacios en blanco sobrantes al inicio y al final (strip).
#c. Reemplazar cada ocurrencia de dos espacios seguidos "  " por uno solo " " (replace).
#d. Convertir todo el texto a minúsculas (lower) y a mayúsculas (upper).
#Pregunta: ¿se pueden resolver los pasos a, b y c en una sola línea componiendo las funciones? (Composición: texto.strip().replace("  ", " ")...).
#Para pensar: si el nombre viene con tres espacios seguidos,
# ¿alcanza con un solo replace("  ", " ")? Probalo con "Juan   Pérez" y explicá lo que observás.

usuario = input("Ingrese su nombre completo: ")

usuario = usuario.strip().replace("  ", " ")
print("Nombre en minusculas: ", usuario.lower())
print("Nombre en mayusculas: ", usuario.upper())

