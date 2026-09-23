#Ejercicio B3 — Conversión de tiempo  ★
#Definir una función a_hms(segundos) que convierta una cantidad de segundos a horas, minutos y segundos,
#devolviendo los tres valores juntos en una tupla (múltiples resultados, como en la teoría).
#Recordá: los operadores // (división entera) y % (resto) hacen todo el trabajo. Al llamarla podés 
#desempaquetar: h, m, s = a_hms(3661) → (1, 1, 1).

def segundos_a_hms(segundos):
    horas=segundos//3600
    minutos=(segundos%3600)//60
    segundos_restantes=segundos%60
    return horas, minutos, segundos_restantes

#bloque principal
h, m, s =segundos_a_hms(24002034)
print(f"Horas: {h}, Minutos: {m}, Segundos: {s}")