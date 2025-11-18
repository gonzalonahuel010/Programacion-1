""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra. 
Entrada -> "Hola mundo hola"
salida:
palabras_unicas: {'hola','mundo'}
recuento:{'hola':2,'mundo':1}
"""

frase = input("Ingrese una frase: ")

# 1. Convertimos a minúsculas y dividimos en una lista de palabras
palabras_list = frase.lower().split() 

# 2. Palabras únicas (usando un set)
palabras_unicas = set(palabras_list)

# 3. Diccionario con la cantidad de veces que aparece cada palabra (conteo)
# Iteramos sobre las palabras únicas y contamos cuántas veces aparece cada una en la lista de palabras
recuento = {palabra: palabras_list.count(palabra) for palabra in palabras_unicas}

# Imprimir la salida solicitada
print(f"palabras_unicas: {palabras_unicas}")
print(f"recuento: {recuento}")