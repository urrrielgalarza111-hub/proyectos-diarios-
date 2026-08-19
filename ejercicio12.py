#Ejercicio A8 — Números pares
#Imprimir los números pares entre 1 y 50 usando un for. Consigna: recorrer range(1, 51) y usar continue para saltear los impares.
#Pista: un número i es impar si i % 2 != 0. Cuando termines, pensá: ¿cómo lo resolverías sin continue, 
#usando solo el tercer parámetro de range? Dejá esa alternativa como comentario.

for i in range(1,51):
    if i % 2 != 0:
        continue
    print(i)