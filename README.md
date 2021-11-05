# El-juego-de-adivinar-3-
Mi dirección de GitHub para este repositorio es la siguiente: GitHub https://github.com/acasasaez/El-juego-de-adivinar-3-.git
Para esta tara hemos resuelto un juego de adivinar con valores entre el 0 y el 99. El diagrama de flujo que tenemos en nuestro código es el siguiente:

![diagrama de flujo del juego de adivinar](https://github.com/acasasaez/El-juego-de-adivinar-3-/blob/main/Nuevofigma.jpg)

El código es:
``` import random
numero = random.randint(0,99)
intento = int(input("Elija un numero del 1 al 99:"))
numero_intento = 0
while intento != numero:
    if intento < numero:
        print ("Demasiado pequeño.")
        numero_intento = numero_intento + 1
        intento = int (input("Elija otro numero:"))
    if intento > numero:
        print( "Demasiado grande.")
        numero_intento = numero_intento +1
        intento = int (input("Elija otro numero:"))
    if intento == numero:
        print("Enhorabuena, has acertado.")
        numero_intento = numero_intento +1
        print("Número de intentos:" +str(numero_intento))
