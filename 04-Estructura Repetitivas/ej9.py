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