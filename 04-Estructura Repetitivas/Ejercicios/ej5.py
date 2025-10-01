""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. """
import random
intentos = 0
stop = False
azar = int(random.randint(0,9))
while stop == False:
    num = int(input("Ingrese un numero: "))
    print ("azar = ",azar)
    if num != azar:
        intentos +=1
    else:
        stop = True