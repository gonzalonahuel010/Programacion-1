""" 1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja. """

notas = []
suma = 0
max_nota = 1
min_nota = 10
while len(notas) < 10:
    nota = int(input("Ingrese una nota: "))
    if nota <1 or nota > 10 :
        nota = int(input("Ingrese una nota valida (1-10): "))
    notas.append(nota)
    if nota > max_nota:
        max_nota = nota
    if nota < min_nota :
        min_nota = nota
print(notas)
for nota in range(len(notas)):
    suma += notas[nota]
    print (suma)
promedio = suma / len(notas)
print("promedio: ",promedio)
print("max: ",max_nota)
print("min: ",min_nota)

""" 2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.  """
products = []
while len(products) < 5:
    product = input("Ingrese un producto: ")
    products.append(product)
print("Lista original: ", products)
products_alf = sorted(products)
print("Lista ordenada alfabeticamente: ", products_alf)
eliminar = input("¿Que producto desea eliminar? " )
if eliminar in products:
    products_alf.remove(eliminar)
else:
    eliminar = input("¿Que producto desea eliminar? " )

print ("Lista ordenada alfabeticamente: ",products_alf)

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

""" 5)Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada. """

estudiantes = ['Juan', 'Jose', ' Javier', 'Gonzalo', 'Roberto', 'Carlos', 'Joaquin', ' Tomas']
opcion = int(input("Ingrese una opcion: \n1) Agregar un nuevo estudiante\n2)Eliminar uno existente\n3)Mantener igual"))
if opcion == 1:
    nuevo_estudiante = input("Ingrese nombre del estudiante a agregar: ")
    estudiantes.append(nuevo_estudiante)
    print(estudiantes)
if opcion == 2:
    eliminar_estudiante = input("Ingrese nombre del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if eliminar_estudiante == estudiante:
            estudiantes.remove(estudiante)
    print(estudiantes)
if opcion == 3:
    print(estudiantes)

""" 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero). """

numeros = [1, 4, 6, 7, 8, 9, 3]
print(f"Lista orginal: \n{numeros}")
ultimo = numeros[-1]
for i in range(len(numeros)-1,0,-1):
    numeros[i] = numeros[i-1]
numeros[0] = ultimo
print(f"Lista modificada: \n{numeros}")

""" 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica. """
suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0
temperaturas = [[5,4,5,6,10,11,12],[20,30,33,31,24,28,29]]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]
promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)
print(f"Promedio de temperaturas minimas: {promedio_min}")
print(f"Promedio de temperaturas maximas: {promedio_max}")

for i in range(len(temperaturas)):
    # calculamos la aplitud maxima y minima del dia
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud :
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i

print("Mayor amplitud térmica:", mayor_amplitud, "°C")
print("Día con mayor amplitud:", dias_semana[dia_mayor_amplitud])

""" 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia. """
notas = [[10,5,7],[10,10,10],[8,6,7],[10,9,9],[6,5,8]]
estudiantes = ["Juan", "Jose", "Carlos", "Roberto", "Diego"]
materias = ["Lengua", "Fisica", "Biologia"]
# i recorre estudiantes
for i in range(len(notas)):
    suma = 0
    #j recorre cada materia
    for j in range(len(notas[i])):
        #accedemos a la nota i en la materia j
        suma+= notas[i][j]
    promedio = suma / len(notas[i])
    print(f"{estudiantes[i]} -> Promedio: {promedio}")
    
""" 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada """

tablero = [["-" for _ in range(3)] for _ in range(3)]

for turno in range(6):
    jugador = 'x' if turno % 2 == 0 else 'o'
    for fila in tablero:
        print(" ".join(fila))
    print()
    fila = int(input(f"{jugador} ingrese la fila (0-2): "))
    columna = int(input(f"{jugador} ingrese la columna (0-2): "))

    if tablero [fila][columna] == '-':
        tablero [fila][columna] = jugador
    else: 
        ocupado = True
        print("casilla ocupada, vuelve a probar otra")
        while ocupado:
            fila = int(input(f"{jugador} ingrese la fila (0-2): "))
            columna = int(input(f"{jugador} ingrese la columna (0-2): "))
            if tablero [fila][columna] == '-':
                tablero [fila][columna] = jugador
                ocupado = False
            else:   
                print("esta casilla tambien esta ocupada, vuelve a probar otra")
print("Estado final del tablero:")
for i, fila in enumerate(tablero):
    print(f"{i} | " + " ".join(fila))
print("   0 1 2")
print("¡Fin del juego!")

""" 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana. """

ventas = [
    [100, 50, 60, 60, 76, 13, 100],  # PC
    [100, 50, 60, 60, 76, 63, 100],  # Notebook
    [100, 10, 60, 40, 56, 43, 100],  # Celular
    [100, 60, 60, 60, 76, 98, 100]   # Bicicleta
]

productos = ["PC", "Notebook", "Celular", "Bicicleta"]

# 1. Mostrar el total vendido por cada producto
print("🔹 Total vendido por cada producto:")
totales_productos = []
for i in range(len(ventas)):
    producto = productos[i]
    lista_ventas = ventas[i]
    total = 0
    for venta in lista_ventas:
        total += venta
    totales_productos.append(total)
    print(f"{producto}: {total} unidades")

# 2. Mostrar el día con mayores ventas totales
mayor_total = 0
dia_mayor = 0
for dia in range(7):
    total_dia = 0
    for producto in range(4):
        total_dia += ventas[producto][dia]
    if total_dia > mayor_total:
        mayor_total = total_dia
        dia_mayor = dia
print(f"\n🔹 El día con mayores ventas totales fue el día {dia_mayor + 1} con {mayor_total} unidades vendidas.")

# 3. Indicar cuál fue el producto más vendido en la semana
indice_max = 0
maximo = totales_productos[0]
for i in range(1, len(totales_productos)):
    if totales_productos[i] > maximo:
        maximo = totales_productos[i]
        indice_max = i
print(f"\n🔹 El producto más vendido en la semana fue {productos[indice_max]} con {maximo} unidades.")
