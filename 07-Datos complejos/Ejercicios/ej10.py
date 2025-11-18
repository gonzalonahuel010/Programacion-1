""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores. """

# Diccionario original: Países como claves, Capitales como valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Colombia": "Bogotá",
    "Uruguay": "Montevideo"
}

# Inicializamos el nuevo diccionario vacío
capitales_paises = {}

# Iteramos sobre el diccionario original
for pais, capital in paises_capitales.items():
    # Asignamos la capital como la nueva clave y el país como el nuevo valor
    capitales_paises[capital] = pais

# Mostramos los resultados
print("Diccionario Original (País: Capital)")
print(paises_capitales)

print("\nDiccionario Invertido (Capital: País)")
print(capitales_paises)