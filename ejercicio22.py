#Ejercicio B10 — Tu primer módulo
#Hasta ahora todas tus funciones viven en el mismo archivo. Vamos a modularizar de verdad:
#a. Creá un archivo nuevo llamado mis_funciones.py en la misma carpeta que semana2_ejercicios.py.
#b. Mové ahí las funciones saludar, maximo3, a_hms y contiene_vocal (¡con sus docstrings!).
#c. Desde semana2_ejercicios.py, probá las tres formas de importar y usá cada función al menos una vez:
#import mis_funciones
#print(mis_funciones.saludar("Ana"))
 
#from mis_funciones import maximo3, a_hms
#print(maximo3(4, 9, 2))
 
#from mis_funciones import contiene_vocal as tiene_vocal
#print(tiene_vocal("xyz"))
#Recordá: el nombre del módulo es el nombre del archivo sin el .py. Si Python dice ModuleNotFoundError,
#casi seguro los dos archivos no están en la misma carpeta, o ejecutaste desde otra ubicación.

def saludar(nombre):
    """Devuelve un saludo personalizado para el nombre dado."""
    return f"Hola, {nombre}!"

def maximo3(num1, num2, num3):
    """Devuelve el mayor de tres números enteros."""
    return max(num1, num2, num3)

def a_hms(segtotal):
    """Convierte una cantidad de segundos a horas, minutos y segundos, devolviendo los tres valores en una tupla."""
    horas = segtotal // 3600
    minutos = (segtotal % 3600) // 60
    segundos = (segtotal % 3600) % 60
    return (horas, minutos, segundos)

def contiene_vocal(cadena):
    """Verifica si una cadena de texto contiene al menos una vocal."""
    vocales = "aeiouAEIOU"
    for char in cadena:
        if char in vocales:
            return True
    return False

print(saludar("Ana"))
print(maximo3(4, 9, 2))
print(a_hms(3661))
print(contiene_vocal("xyz"))
