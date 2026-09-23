#Ejercicio B1 — Función saludo  ★
#Definir una función saludar(nombre) que devuelva un string de saludo.
# Probarla con varios nombres.
#Recordá: devolver (return) no es lo mismo que imprimir (print). La función debe devolver la cadena;
# el print se hace afuera, al llamarla. Comprobalo: si tu función usa print, al hacer s = saludar("Ana")
# la variable s queda en None.

def saludar(nombre):
    return(f"Hola! {nombre}")

#bloque principal
print(saludar("uriel"))
print(saludar("mnauel"))
print(saludar("felipe"))