import random
import pickle
import subprocess
def ns (c):
    while c != ("s") and c!= ("n"):
        print(chr(7)); c= input ("Escriba solo `\n\`o `\s\` según su opción:")
    return (c)
def OKI (n):
    try:
       n= int(n) 
    except:
         n= OKI (input ("Caracter no valido:"))
    return n
def limites (n,MAX):
    while n<0 or n>MAX:
         n = OKI (input("ERROR:El numero ha de estar entre 0 y "+str(""+str(MAX)+"): ")))
    return n  
def sing_plu (f):
    if f> 1:
       co= ("intentos")
    else:
        co = ("intentos")
    return co 
def paramar(n):
    m=n-1
    return m
while True:
    marca= pickle.load(open("mejor_marca", "rb"))
    print ("ADIVINA EL NUMERO")
    print ("""En este juego el usuario debe adivinar un numero, escogido al azar por la computadora, entre un rango determinado""")
    print("")
    print("""ESCOJA EL NIVEL DE DIFICULTAD 
Nivel 1:Entre 0 y 100 
Nivel 2: Entre 0 y 10000
Nivel 3: Entre 0 y 1000000""")
    level = OKI(input("Escriba su opcion (de 1 a 3):"))
    print("")
    while level != 1 and level !=2 and level != 3:
        level = OKI (input("Escriba un numero entre 1 y 4:"))
    MAX = 100** (level +1)    
    Di = ("0 y" + str(MAX))    
    numero_elegido = random.randint(0, MAX)
    intentos = 0
    tu_numero = limites (OKI(input("Escribe un numero comprendido entre" + Di+ ":")), MAX)
    diferencia = abs (tu_numero - numero_elegido)
    num_anterior = tu_numero
    intentos +=1
    repes = 1
    while tu_numero != numero_elegido :
        tu_numero = (limites (OKI (input("Escribe un numero comprendido entre" + Di +":")), MAX))
        if abs (tu_numero - numero_elegido):
            if tu_numero !=num_anterior:
                if (abs(tu_numero -numero_elegido ))<diferencia:
                    print ("Te estás acercando")
                else:
                    print ("Te estás alejando")
                repes = 1
            else:
                repes += 1
                print("Has introducido el mismo número",repes,"veces seguidas")

    