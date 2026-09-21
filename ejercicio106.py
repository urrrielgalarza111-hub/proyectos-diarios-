#Ejercicio A4 — Decodificación de códigos HTTP
#Leer un número entero correspondiente a un código HTTP 
#y mostrar su significado usando match/case:
#Si es 200, imprimir "OK".
#Si es 404, imprimir "No encontrado".
#Si es 500, 502 o 503, imprimir "Error del servidor" 
#(los tres en un solo case con |).
#En cualquier otro caso, imprimir "Error desconocido" 
#usando el comodín case _:.
#Recordá: match existe desde Python 3.10. Si te da error de sintaxis, 
#verificá tu versión con python --version.

cod=int(input("ingrese un codigo HTTP: "))

if cod==200:
    print("Ok")
elif cod==404:
    print("No encontrado")
elif cod==500 or cod==502 or cod==503:
    print("Error de servidor")
else:
    print("Error desconocido")