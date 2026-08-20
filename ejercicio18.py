#Ejercicio B6 — Alcance de variables  ★
#Copiar, probar y explicar el error del siguiente código:
#def cuadrado(n):
#    return n * n
 
#def suma_cuadrados(n):
#    suma = 0
#    for x in range(1, n+1):
#        suma = suma + cuadrado(x)
#    return suma
 
#print(suma)
#Recordá: las variables definidas dentro de una función son locales: no existen fuera de su ámbito.
# Fuera de la función solo se puede acceder al valor que devuelve mediante return. ¿Qué habría que escribir en la última línea para que funcione?

def cuadrado(n):
    return n * n
 
def suma_cuadrados(n):
    suma = 0
    for x in range(1, n+1):
        suma = suma + cuadrado(x)
    return suma
 
print(suma_cuadrados(5))  # Llamamos a la función suma_cuadrados con un argumento, por ejemplo 5, para obtener el resultado.
