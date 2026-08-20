#Ejercicio B3 — Conversión de tiempo  ★
#Definir una función a_hms(segundos) que convierta una cantidad de segundos a horas, minutos y segundos,
#devolviendo los tres valores juntos en una tupla (múltiples resultados, como en la teoría).
#Recordá: los operadores // (división entera) y % (resto) hacen todo el trabajo. Al llamarla podés desempaquetar: h, m, s = a_hms(3661) → (1, 1, 1).

segtotal = int(input("Ingrese la cantidad de segundos: "))

def a_hms(segtotal):
    horas=[segtotal // 3600]
    minutos=[(segtotal % 3600) // 60]
    segundos=[(segtotal % 3600) % 60]
    return (horas, minutos, segundos)

h, m, s = a_hms(segtotal)

print( h[0], "Horas: ", m[0], "Minutos: ", s[0], "Segundos")