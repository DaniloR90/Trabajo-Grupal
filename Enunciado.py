calificacion=int(input("Ingrese la calificacion del estudiante: "))
if calificacion >= 90 and calificacion <= 100 :
    print("Pertenece al grupo A")
elif calificacion >= 80 and calificacion <= 89:
    print("Pertenece al grupo B")
elif calificacion >= 70 and calificacion <= 79:
    print("Pertenece al grupo C")
elif calificacion >= 60 and calificacion <= 69:
    print("Pertenece al grupo D")
else:
    print("Pertenece al grupo F")
