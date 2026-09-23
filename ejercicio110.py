#Ejercicio A8 — Números pares
#Imprimir los números pares entre 1 y 50 usando un for.
# Consigna: recorrer range(1, 51) y usar continue para saltear los impares.
#Pista: un número i es impar si i % 2 != 0. Cuando termines, pensá: 
# ¿cómo lo resolverías sin continue, usando solo el tercer parámetro de range?
# Dejá esa alternativa como comentario.

i=0

for i in range(1,51):
    if i%2!=0:
        continue
    else:
        print(i)

print("Otro for pero sin continue: ")
        
i=0

for i in range(2,51,2):
    print(i)