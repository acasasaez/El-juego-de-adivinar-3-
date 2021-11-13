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
       