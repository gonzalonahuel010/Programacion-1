""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """
cont = 0
while cont <= 100:
    print (cont)
    cont += 1



""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """
num = input("Ingrese un numero: ")
cont = 0
for digito in num :
    cont += 1
print (f"El numero {num} tiene {cont} digitos")



""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores. """

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero "))
mayor = 0
menor = 0
suma = 0

if num1 < num2:
    mayor = num2
    menor = num1
else:
    mayor = num1
    menor = num2
for i in range (menor+1,mayor):
    suma += i
    print (suma)
print (suma)



""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0. """
stop = False
suma = 0
while stop == False:
    num = int(input("Ingrese un numero: "))
    suma += num
    if num == 0:
        stop = True
        print (suma)



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



""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente. """

for i in range (100,-1,-1):
    if i % 2 == 0:
        print (i)



""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
 """
num = int(input("Ingrese un numero: "))
suma = 0
for i in range (0, num+1):
    suma += i
    print (suma)
print ("Suma final: ",suma)



""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio). """

contPar = 0
contImpar = 0
contPositivo = 0
contNegativo = 0
cont = 0
while cont < 100:
    num = int(input("Ingrese un numero: "))
    print(num)
    if num % 2 == 0 and num > 0:
        contPar += 1
        contPositivo += 1
    elif num % 2 == 0 and num < 0:
        contPar += 1
        contNegativo += 1
    elif num % 2 != 0 and num > 0:
        contImpar += 1
        contPositivo += 1
    else:
        contImpar += 1
        contNegativo += 1
    cont +=1
print(f"Pares: {contPar}\nImpares: {contImpar}\nPositivos: {contPositivo}\nNegativos: {contNegativo}")



""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor). """
cont = 0
suma = 0
while cont < 5:
    num = int(input("Ingrese un numero: "))
    suma += num
    cont += 1
media = suma / cont
print ("La media de los numeros es: ",media)



""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745 """
num = input("Ingrese un numero: ")
num_reves = ""
for i in range(len(num)-1,-1,-1):
    num_reves += num[i]
print(f"Numero original: {num}\nNumero invertido: {num_reves}")