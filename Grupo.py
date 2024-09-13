nombre=input("Ingrese su nombre: ").upper()
sexo=input("Ingrese (F) para femenino y (M) para masculino:").upper()
if sexo=="F" and nombre[0]<"M":
    print("Grupo A")
elif sexo=="M" and nombre[0]>"N":
    print("Grupo A")
else:
    print("Grupo B")