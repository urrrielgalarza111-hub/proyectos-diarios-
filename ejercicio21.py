#Ejercicio B9 — Return en bucles  ★
#Escribir una función contiene_vocal(cadena) que:
#Recorra la cadena con un for.
#Devuelva True apenas encuentre una vocal (return dentro del bucle, como el "early return" de la teoría).
#Si termina de recorrer sin hallar vocales, devuelva False.
#Probarla con varias palabras: "python" → True; "xyz" → False; "" → False.
#Atención: el error clásico es poner return False dentro del for (en el else del if): así la función decide mirando solo la primera letra. 
#El return False va después del ciclo, cuando ya se revisó toda la cadena.

def contiene_vocal(cadena):
    for letra in cadena:
        if letra.lower() in "aeiou":
            return True
    return False

print(contiene_vocal("python"))  # → True
print(contiene_vocal("xyz"))     # → False
print(contiene_vocal(""))        # → False