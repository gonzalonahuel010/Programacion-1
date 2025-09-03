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