import random
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
        print("Número de intentos:" +str(numero_intento) )