""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """
num = input("Ingrese un numero: ")
cont = 0
for digito in num :
    cont += 1
print (f"El numero {num} tiene {cont} digitos")