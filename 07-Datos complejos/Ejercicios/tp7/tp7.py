""" 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios. """

precio_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300, 'Melon': 2800}

frutas = list(precio_frutas.keys())

print(frutas)

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:
contactos = {"Juan": "123456","Ana":"987654"}
Consultar "Juan" muestra "123456" """

contactos = {}
while len(contactos) < 5:
    nombre_invalido = False
    nombre = input("Ingrese el nombre del contacto: ")
    if not nombre.isalpha():
        print("Nombre invalido, vuelve a intentar")
        continue
    else:
        numero = input(f"Ingrese numero de telefono del contacto '{nombre}': ")
        if not numero.isdigit():
            print("Numero invalido, vuelve a intentar")
            continue
        contactos[nombre] = numero
    
print (contactos)

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

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno. """

# Inicializamos un diccionario vacío para guardar los datos
alumnos_notas = {}
numero_alumnos = 3
numero_notas = 3

# 1. Solicitamos los datos de los alumnos
for i in range(numero_alumnos):
    print(f"\n--- Alumno {i + 1} de {numero_alumnos} ---")
    
    # Solicitamos el nombre
    nombre = input("Ingresá el nombre del alumno: ")
    
    # Solicitamos y almacenammos las 3 notas en una tupla
    notas_lista = []
    for j in range(numero_notas):
        # Solicitamos la nota y la convertimos directamente a float 
        nota = float(input(f"Ingresá la nota {j + 1}: "))
        notas_lista.append(nota)
                
    # Convertimos la lista de notas a una tupla y la guardamos en el diccionario
    alumnos_notas[nombre] = tuple(notas_lista)

# 2. Calculamos y mostramos el promedio de cada alumno
print("\n" + "="*30)
print("Promedios de los Alumnos")
print("="*30)

# Iteramos sobre el diccionario (clave=nombre, valor=notas_tupla)
for nombre, notas_tupla in alumnos_notas.items():
    # Calculamos la suma de las notas y el promedio
    suma_notas = sum(notas_tupla)
    promedio = suma_notas / len(notas_tupla)
    
    # Mostramos el resultado
    print(f"El promedio de **{nombre}** es: **{promedio:.2f}** (Notas: {notas_tupla})")

    """ 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

aprobados_parcial_1 = {101, 103, 105, 107, 109, 110}
aprobados_parcial_2 = {103, 104, 105, 106, 110, 111}

print(f"Aprobaron Parcial 1: {aprobados_parcial_1}")
print(f"Aprobaron Parcial 2: {aprobados_parcial_2}")

# 1. Alumnos que aprobaron AMBOS parciales (Intersección)
ambos_parciales = aprobados_parcial_1.intersection(aprobados_parcial_2)

print("\nResultados:")
print(f"Aprobaron ambos parciales (Intersección): {ambos_parciales}")

# --- 2. Alumnos que aprobaron SOLO UNO de los dos (Diferencia Simétrica) ---
solo_uno = aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)

print(f"Aprobaron solo uno de los dos (Diferencia Simétrica): {solo_uno}")
# --- 3. Lista total que aprobó AL MENOS UN parcial (Unión) ---
total_aprobados = aprobados_parcial_1.union(aprobados_parcial_2)

print(f"Total que aprobó al menos uno (Unión): {total_aprobados}")

""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. """

# Diccionario inicial de inventario: Clave = Producto, Valor = Stock
inventario = {
    "manzanas": 50,
    "plátanos": 35,
    "naranjas": 20
}

def consultar_stock(nombre_producto):
    """Consulta y muestra el stock de un producto."""
    # Convertimos a minúsculas 
    producto = nombre_producto.lower()
    
    if producto in inventario:
        print(f"\nStock de {producto.capitalize()}: {inventario[producto]} unidades.")
    else:
        print(f"\nProducto '{nombre_producto}' no encontrado en el inventario.")
        
def agregar_unidades(nombre_producto, cantidad):
    """Agrega unidades a un producto existente o lo crea si no existe."""
    producto = nombre_producto.lower()
    
    if producto in inventario:
        # El producto existe, solo actualizamos el stock
        inventario[producto] += cantidad
        print(f"\nSe agregaron {cantidad} unidades a {producto.capitalize()}.")
        print(f"   Nuevo stock: {inventario[producto]} unidades.")
    else:
        # El producto no existe, lo agregamos al diccionario
        inventario[producto] = cantidad
        print(f"\nNuevo producto {producto.capitalize()} agregado con {cantidad} unidades.")

# Bucle principal

print("Sistema de Gestión de Inventario")
while True:
    print("\n--- Opciones ---")
    print("1. Consultar Stock")
    print("2. Agregar Unidades / Nuevo Producto")
    print("3. Mostrar Inventario Completo y Salir")
    
    opcion = input("Ingrese una opción (1, 2, o 3): ")

    if opcion == '1':
        # Consultar Stock
        nombre = input("Ingrese el nombre del producto a consultar: ")
        consultar_stock(nombre)

    elif opcion == '2':
        # Agregar Unidades / Nuevo Producto
        nombre = input("Ingrese el nombre del producto (existente o nuevo): ")
        # Solicitamos la cantidad y la convertimos directamente a entero
        cantidad = int(input("Ingrese la cantidad de unidades a agregar: ")) 
        agregar_unidades(nombre, cantidad)

    elif opcion == '3':
        # Salir
        print("\n=== Inventario Final ===")
        print(inventario)
        print("Saliendo del sistema...")
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora. """

# Diccionario de la agenda: Clave = tupla (día_semana, hora_24h)
agenda = {
    ("lunes", 9): "Gimnasio",
    ("martes", 14): "Crear proyectos laborales",
    ("miércoles", 11): "Presentación de proyectos",
    ("jueves", 17): "Estudiar matematica",
    ("viernes", 14): "Revisión de código"
}

print("Consultar Eventos de la Agenda")
print("Días: Lunes a Viernes. Horas: 0 a 23.")

# 1. Solicitamos la entrada al usuario
dia_input = input("Ingresá el día de la semana (ej: martes): ").lower()

# Solicitamos la hora y la convertimos directamente a entero
hora_input = int(input("Ingresá la hora (ej: 9): "))

# 2. Creamos la clave de búsqueda como una tupla
clave_busqueda = (dia_input, hora_input)

# 3. Consultamos el diccionario
print("\nResultado de la Consulta")

if clave_busqueda in agenda:
    # Si la tupla existe como clave
    evento = agenda[clave_busqueda]
    print(f"Evento programado para el **{dia_input.capitalize()}** a las **{hora_input:02d}:00**:")
    print(f" '{evento}' ")
else:
    # Si la tupla no existe
    print(f"No hay actividad programada para el **{dia_input.capitalize()}** a las **{hora_input:02d}:00**.")

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