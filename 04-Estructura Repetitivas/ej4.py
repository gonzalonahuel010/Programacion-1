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
