#Ejercicio A6 — Contraseña (while con centinela)  ★
#Solicitar al usuario una contraseña hasta que la ingrese correctamente:
#La contraseña válida debe estar guardada en una variable clave_correcta.
#El usuario puede intentar indefinidamente hasta acertar.
#Cuando acierte, mostrar "Acceso concedido".
#Recordá: el esquema con centinela de la teoría: pedir el dato antes del while, 
#y volver a pedirlo como última instrucción dentro del ciclo. Acá el "centinela" que corta el ciclo es la clave correcta.
#Opcional: limitar a 3 intentos con un contador y mostrar "Cuenta bloqueada" si falla los tres.
#¿Conviene resolverlo con and en la condición del while o con break? Probá las dos formas.

contraseña_correcta = "123456"
intentos=0

contraseña_ingresada=input("Ingrese la contraseña: ")
while contraseña_ingresada != contraseña_correcta and intentos <2 :
    print("Contraseña incorrecta. Intente nuevamente.")
    intentos += 1
    contraseña_ingresada=input("Ingrese la contraseña: ")

if contraseña_ingresada == contraseña_correcta:
    print("Acceso concedido")
else:
    print("Cuenta bloqueada")