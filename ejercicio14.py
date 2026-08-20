#Ejercicio B1 — Función saludo  ★
#Definir una función saludar(nombre) que devuelva un string de saludo. Probarla con varios nombres.
#Recordá: devolver (return) no es lo mismo que imprimir (print). La función debe devolver la cadena; 
#el print se hace afuera, al llamarla. Comprobalo: si tu función usa print, al hacer s = saludar("Ana") la variable s queda en None.

nombre=input("Ingrese su nombre: ")

def saludar(nombre):
    return "Hola "+ nombre+"!"

print(saludar(nombre))