import random
numeros = [random.randint(1,100) for num in range (1,16)]

# - Recorre el número de pasadas necesarias para ordenar la lista.
# - Si la lista tiene n elementos, se hacen n - 1 pasadas como máximo.
for indice_pasada in range(len(numeros)-1):
    
#   Recorre los elementos que aún no están ordenados.
#  	En cada pasada, el mayor valor "flota" hacia el final, así que en la siguiente pasada no hace falta comparar hasta el final.
    for indice_actual in range(len(numeros) - 1 - indice_pasada):
        if numeros[indice_actual] > numeros[indice_actual+1]:
            numeros[indice_actual], numeros[indice_actual+1] = numeros[indice_actual+1], numeros[indice_actual]
            print (numeros)
            
print (numeros)
            