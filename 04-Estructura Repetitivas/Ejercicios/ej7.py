""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
 """
num = int(input("Ingrese un numero: "))
suma = 0
for i in range (0, num+1):
    suma += i
    print (suma)
print ("Suma final: ",suma)