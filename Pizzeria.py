from math import e
from multiprocessing import Value

#Seleccion tipo de pizza
print("PIZZERIA BELLA NAPOLI")
tipopizza=int(input("Seleccione un número:\n1) Vegetariana\n2) No Vegetariana\nSeleccion:"))
#Ingredientes Principales
principales="Mozzarella,Tomate"
#Seleccion de ingredientes dependiendo del tipo de pizza
if tipopizza==1:
    tipopizza="Vegetariana"
    print(tipopizza,":")
    ingredientes=int(input("¡Ingrediente!\n1)Pimiento\n2)Tofu\nSeleccion:"))
elif tipopizza==2:
    tipopizza="No Vegetariana"
    print(tipopizza,":")
    ingredientes=int(input("¡Ingredientes!\n1)Peperoni\n2)Jamón\n3)Salmóm\nSeleccion:"))
else:
    print("Opción no valida")
#Mostrar pizza elegida
try:
    if tipopizza=="Vegetariana":
        if ingredientes==1:
            ingredientes="Pimiento"
        elif ingredientes==2:
            ingredientes="Tofu"
        else:
            raise ValueError("Opción no valida")
    elif tipopizza=="No Vegetariana":
        if ingredientes==1:
            ingredientes="Peperoni"
        elif ingredientes==2:
            ingredientes="Jamón"
        elif ingredientes==3:
            ingredientes="Salmón"
        else:
            raise ValueError("Opción no valida")
    print("Pizza",tipopizza,"con los siguientes ingredientes"":","\n",principales,ingredientes)       
except ValueError as e:
    print("Opps opción no encontrada:",e)
