#Ejercicio A3 — Optimización de código  ★
#El siguiente código usa if anidados para clasificar una nota. Copialo, probalo, y reescribilo de manera más clara y eficiente.
#nota = int(input("Ingrese la nota (0 a 10): "))
 
#if nota >= 9:
#    print("Excelente")
#else:
#    if nota >= 7:
#       print("Muy bueno")
#   else:
#       if nota >= 4:
#           print("Aprobado")
#       else:
#           print("Desaprobado")
#Pista: en la teoría vimos que un else: seguido inmediatamente de un if se puede escribir como elif.
#Verificá que tu versión produce exactamente la misma salida para las notas 10, 8, 5

nota = int(input("Ingrese la nota (0 a 10): "))

if nota >=9:
    print("exelente")
elif nota >=7:
        print("muy bueno")
elif nota >=4:
            print("aprobado")
elif nota <4:
            print("desaprobado")