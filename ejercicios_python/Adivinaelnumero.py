#ADIVINA EL NUMERO.
import random

print("Adivina el numero")
minimo=int(input("introduce el intervalo inferior "))
maximo=int(input("introduce el intervalo superior "))
print("tienes 3 intentos, suerte.")
intentos=3

numeroganador=random.randint(minimo,maximo)

print("que comience el juego!!")

while intentos>0:
    
    numerousuario=int(input("introduce un numero "))
    if numeroganador>numerousuario:
        print("El numero es mas alto, intentalo de nuevo")
        intentos -=1
        print (f"quedan {intentos} intentos")
    if numeroganador<numerousuario:
        print("El numero es mas bajo, un intento mas")
        intentos -=1
        print (f"quedan {intentos} intentos")
    if numeroganador==numerousuario:
        print ("ENHORABUENA, NUMERO CORRECTO!!")
        intentos=-1
    if intentos==0:
        print("intentos agotados, mala suerte")