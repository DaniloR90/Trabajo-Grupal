#Bienvenida al juego.
from pickle import FALSE, TRUE


print("Bienvenido forastero, te encuentras en las puertas del castillo de DrownedHead.")
print("Tu mision es encontrar el tesoro que se encuentra en el salon del trono y salir de ahi!!.")

#Pregunta inicial

pregunta1=int(input("\n""¿Quieres ingresar al castillo?" "\n" "1)Si""\n""2)No""\n""Respuesta:"))
if pregunta1==1:
    print("!!Adelante¡¡ Pero ten cuidado por que cada puerta puede esconder una trampa.")
    print("Avanzas dentro del castillo, y te encuentras en una sala oscura.")
elif pregunta1==2:
    print("Das media vuelta y vuelves por tu camino, hoy no sientes ganas de tener una aventura.")
    print("\n""Gracias por jugar Castillo DrownedHead.")
    raise
    
else:
    print("Esto es blanco o negro, 1 o 2")

#Pregunta 2

castillo = TRUE
while castillo:
    print("Entre las penumbras ves dos puertas y varias antorchas sin prender!!")
    pregunta2=int(input("\n""¿Quieres enceder la antorcha?""\n" "1)Si""\n""2)No""\n""Respuesta:"))
    if pregunta2==1:
        print("Enciendes la antorcha y ves con claridad las dos puertas!")
    elif pregunta2==2:
        print("Te mueves a oscuras")
    else:
        print("Esto es blanco o negro, 1 o 2")

#Pregunta 3

    print("Piensas cual puerta te convence mas!")
    pregunta3=int(input("\n""¿Que puerta eliges?""\n""1)Izquierda""\n""2)Derecha""\n""Respuesta:"))
    if pregunta3==1 and pregunta2==1:
        print("Abres la puerta y ves el tesoro al final!!")
        print("Corres para agarrar el tesoro y salir de ahi de inmediato!")
        castillo = FALSE
        break
    elif pregunta3==1 and pregunta2==2:
        print("Abres la puerta y no ves nada dentro")
        pregunta_final=int(input("\n""Entras a la habitacion?""\n""1)Si""\n""2)No""\n""Respuesta:"))
        if pregunta_final==1:
            print("Despues de dar vueltas a oscuras te topas con el cofre!, lo tomas y sales corriendo")
            castillo = FALSE
            break
        elif pregunta_final==2:
            print("Te vuelves a la sala anterior")
        else:
            print("Esto es blanco o negro, 1 o 2")
    elif pregunta3==2 and pregunta2==1:
        print("Abres la puerta y ves una trampa delante tuyo!!")
        print("Te das vuelta rapido y la antorcha se apaga, vuelves a la sala anterior")
    elif pregunta3==2 and pregunta2==2:
        print("Abres la puerta y no ves nada dentro")
        pregunta_final=int(input("Entras a la habitacion?""\n""1)Si""\n""2)No""\n""Respuesta:"))
        if pregunta_final==1:
            print("Entras a la habitacion y caes dentro de un pozo")
            print("Nadie puede escucharte gritar!")
            castillo = FALSE
            break
        elif pregunta_final==2:
            print("Te vuelves a la sala anterior")
        else:
            print("Esto es blanco o negro, 1 o 2")
    else:
        print("Esto es blanco o negro, 1 o 2")
print("\n""Gracias por jugar Castillo DrownedHead.")

