""" 4) Dada una lista con valores repetidos: 
datos =  [1,3,5,3,7,1,9,5,3]
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado. """
datos =  [1,3,5,3,7,1,9,5,3]
datos_no_repetidos = []

for i in range(len(datos)):
    elemento = datos[i]
    if elemento not in datos_no_repetidos:
        datos_no_repetidos.append(elemento)
    r""" epetido = False
    for j in range(len(datos)):
        if j < len(datos_no_repetidos) and elemento == datos_no_repetidos[j]:
            repetido = True
            break
    if not repetido:
        datos_no_repetidos.append(elemento) """

print(f"Datos originales: \n{datos}")
print(f"Datos no repetidos: \n{datos_no_repetidos}")