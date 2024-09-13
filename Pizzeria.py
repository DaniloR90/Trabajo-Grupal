Elección=str(input("Opciones disponibles: \n 1. Pizza vegetariana  \n 2. Pizza no vegetariana \nElija la opcion deseada: "))
if Elección == "1": #Pizza vegetariana
    print("Los ingredientes disponibles son Tofu y Pimiento")
    ingredientes = str(input("Opciones: \n 1. Tofu \n 2. Pimiento  \nElija la opcion deseada: "))
    if ingredientes == "1":
        print("La pizza seleccionada es vegetariana y lleva los siguientes ingredientes: \nMozarrella \nTomate \nTofu")
    else:
        print("La pizza seleccionada es vegetariana y lleva los siguientes ingredientes: \nMozarrella \nTomate \nPimiento")
if Elección == "2": #Pizza no vegana
    print("Los ingredientes dispobiles son: Peperoni Jamon Salmon")
    ingredientes1 = str(input("Opciones: \n 1. Peperoni \n 2. Salmon  \n 3. Jamon \nElija la opcion deseada: "))
    if ingredientes1 == "1":
     print("La pizza es no vegetariana y lleva los siguientes ingredientes \nMozarella \nTomate \nPeperoni")
    elif ingredientes1 == "2":
     print("La pizza es no vegetariana y lleva los siguientes ingredientes \nMozarella \nTomate \nSalmon")
    else:
     print("La pizza es no vegetariana y lleva los siguientes ingredientes \nMozarella \nTomate \nJamon")