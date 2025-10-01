""" 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero). """

numeros = [1, 4, 6, 7, 8, 9, 3]
print(f"Lista orginal: \n{numeros}")
ultimo = numeros[-1]
for i in range(len(numeros)-1,0,-1):
    numeros[i] = numeros[i-1]
numeros[0] = ultimo
print(f"Lista modificada: \n{numeros}")