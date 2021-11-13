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
