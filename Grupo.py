nombre, sexo =str(input("Ingrese su nombre y su sexo: ")).upper().split()
if nombre[0] < "M" and sexo == "FEMENINO" or nombre[0] > "N" and sexo == "MASCULINO":
    print("A usted le corresponde el grupo A")
else:
    print("A ustes le corresponde el grupo B")