""" 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
• Crear una lista con los pares y otra con los impares. 
• Mostrar cuántos números tiene cada lista. """
import random
numeros = [random.randint(1,100) for num in range (1,16)]
pares=[]

impares=[]
for numero in range(len(numeros)):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Pares: \n{pares}")
print(f"Impares: \n{impares}")