""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra. 
Entrada -> "Hola mundo hola"
salida:
palabras_unicas: {'hola','mundo'}
recuento:{'hola':2,'mundo':1}
"""

frase = input("Ingrese una frase: ")

nueva = set(frase)

print(nueva)
