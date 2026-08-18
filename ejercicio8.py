#Ejercicio A4 — Decodificación de códigos HTTP
#Leer un número entero correspondiente a un código HTTP y mostrar su significado usando match/case:
#Si es 200, imprimir "OK".
#Si es 404, imprimir "No encontrado".
#Si es 500, 502 o 503, imprimir "Error del servidor" (los tres en un solo case con |).
#En cualquier otro caso, imprimir "Error desconocido" usando el comodín case _:.
#Recordá: match existe desde Python 3.10. Si te da error de sintaxis, verificá tu versión con python --version.

cod_http=int(input("Ingrese un código HTTP: "))

match cod_http:
    case 200:
        print("OK")
    case 404:
        print("No encontrado")
    case 500 | 502 | 503:
        print("Error del servidor")
    case _:
        print("Error desconocido")