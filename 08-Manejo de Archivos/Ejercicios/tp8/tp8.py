""" 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30 """

nombre_archivo = "C:/Users/gonza/OneDrive - TUPAD UTN/UTN/Programacion-1/08-Manejo de Archivos/Ejercicios/productos.txt"
# 1. Abrimos el archivo en modo lectura ('r')
with open(nombre_archivo, "r") as archivo:
# 2. Iteramos sobre cada línea del archivo
    for linea in archivo:
        # 3.Procesar la línea:
        # a) Eliminar espacios en blanco alrededor de la línea (.strip())
        linea_limpia = linea.strip()
        
        # b) Dividir la cadena por la coma (.split(","))
        # Esto resulta en una lista de 3 elementos: [producto, precio, cantidad]
        datos = linea_limpia.split(",")
        
        # Verificar que tengamos 3 elementos para evitar errores
        if len(datos) == 3:
            producto = datos[0]
            # Convertir precio y cantidad a números para un formato correcto
            precio = float(datos[1])
            cantidad = int(datos[2])
            
            # 5. Mostrar el producto en el formato solicitado
            # Utilizamos f-strings para formatear el precio con dos decimales.
            print(f"Producto: '{producto}' | Precio: ${precio} | Cantidad: {cantidad}")
        else:
            print(f"Línea con formato incorrecto ignorada: {linea_limpia}")

""" 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente. """

nombre_archivo = "C:/Users/gonza/OneDrive - TUPAD UTN/UTN/Programacion-1/08-Manejo de Archivos/Ejercicios/productos.txt"

def mostrar_productos():
    """Lee y muestra los productos del archivo."""
    print(f"\nListado de Productos desde '{nombre_archivo}'")

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            datos = linea_limpia.split(",")
            
            if len(datos) == 3:
                producto = datos[0]
                # Convertir a números
                precio = float(datos[1])
                cantidad = int(datos[2])
                
                # Mostrar el producto en el formato solicitado
                print(f"Producto: '{producto}' | Precio: ${precio} | Cantidad: {cantidad}")
        
def agregar_producto():
    """Pide datos al usuario y los agrega al final del archivo."""
    print("\n=== Agregar Nuevo Producto ===")
    
    # 1. Solicitar datos del usuario
    nombre_nuevo = input("Ingrese el nombre del nuevo producto: ").strip()
    precio_nuevo = float(input("Ingrese el precio: "))
    cantidad_nueva = int(input("Ingrese la cantidad (stock): "))

    # 2. Damos formato a la nueva línea de datos
    nueva_linea = f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n"
    
    # 3. Abrir el archivo en modo AGREGADO ('a')
    with open(nombre_archivo, "a") as archivo:
            archivo.write(nueva_linea)
            print(f"\n✅ Producto '{nombre_nuevo}' agregado exitosamente a {nombre_archivo}.")
  
# Ejecución del Programa
# A. Mostrar los productos existentes
mostrar_productos()

# B. Pedir y agregar un nuevo producto
agregar_producto()

""" 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
 """

nombre_archivo = "C:/Users/gonza/OneDrive - TUPAD UTN/UTN/Programacion-1/08-Manejo de Archivos/Ejercicios/productos.txt"

def cargar_productos_en_lista_simple():
    """
    Lee el archivo de productos y carga los datos en una lista de diccionarios.
    """
    productos = []
    print(f"\nCargando productos desde '{nombre_archivo}'")
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            
            # Omitir líneas vacías
            if not linea_limpia:
                continue

            datos = linea_limpia.split(",")
            
            if len(datos) == 3:
                nombre = datos[0].strip()
                precio = float(datos[1]) 
                cantidad = int(datos[2])   
                
                # Creamos el diccionario y lo agregamos a la lista
                producto_dict = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto_dict)
            else:
                # Las líneas mal formadas simplemente se omiten.
                pass 
                
    print(f"Carga finalizada. Se cargaron {len(productos)} productos.")
    return productos

# --- Ejecución del programa ---

lista_de_productos_simple = cargar_productos_en_lista_simple()

print("\nEstructura de la Lista de Productos Cargada")
for p in lista_de_productos_simple:
    print(f"Nombre: '{p['nombre']}' | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

""" 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
 """
nombre_archivo = "productos.txt"

def cargar_productos_en_lista_simple():
    """
    Lee el archivo de productos y carga los datos en una lista de diccionarios.
    """
    productos = []
    print(f"\n⚙️ Cargando productos desde '{nombre_archivo}'...")

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            
            if not linea_limpia:
                continue

            datos = linea_limpia.split(",")
            
            if len(datos) == 3:
                nombre = datos[0].strip()
                precio = float(datos[1])
                cantidad = int(datos[2])   
                
                producto_dict = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto_dict)
            
    print(f"Carga finalizada. Se cargaron {len(productos)} productos.")
    return productos


def buscar_producto_por_nombre(lista_productos):
    """
    Pide al usuario un nombre, busca el producto en la lista de diccionarios y muestra sus datos si lo encuentra.
    """
    print("\nBúsqueda de Producto")
    
    # Pedimos el nombre a buscar
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    
    # 1. Recorremos la lista de productos
    producto_encontrado = None
    
    # Hacemos la búsqueda
    nombre_buscado_lower = nombre_buscado.lower()
    
    for producto in lista_productos:
        if producto['nombre'].lower() == nombre_buscado_lower:
            producto_encontrado = producto
            break
    
    # 2. Mostrar resultado
    if producto_encontrado:
        print("\nProducto Encontrado:")
        print(f"Nombre: '{producto_encontrado['nombre']}'")
        print(f"Precio: ${producto_encontrado['precio']}")
        print(f"Cantidad (stock): {producto_encontrado['cantidad']}")
    else:
        print(f"\nError: El producto '{nombre_buscado}' no se encontró en el inventario.")


# --- Ejecución del Programa Principal ---

# 1. Cargar todos los productos del archivo a la lista de diccionarios
inventario = cargar_productos_en_lista_simple()

# 2. Recorremos el inventario
if inventario:
    buscar_producto_por_nombre(inventario)

""" 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista. """

nombre_archivo = "productos.txt"

# Funciones de Archivo y Lista

def cargar_productos_en_lista(nombre_archivo):
    productos = []
    print(f"\nCargando productos desde '{nombre_archivo}'")

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            
            if not linea_limpia:
                continue

            datos = linea_limpia.split(",")
            
            if len(datos) == 3:
                nombre = datos[0].strip()
                precio = float(datos[1])
                cantidad = int(datos[2])   
                
                producto_dict = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto_dict)
            
    print(f"Carga finalizada. Se cargaron {len(productos)} productos.")
    return productos

def guardar_productos(lista_productos, nombre_archivo):
    """
    Sobrescribe el archivo de texto con los productos actualizados desde la lista.
    """
    print(f"\nGuardando {len(lista_productos)} productos en '{nombre_archivo}'...")
    
    # Abrir el archivo en modo 'w' (escritura) para sobreescribir
    with open(nombre_archivo, "w") as archivo:
        for p in lista_productos:
            # Le damos formato a la línea: Nombre,Precio,Cantidad
            linea_a_escribir = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea_a_escribir)
            
    print("Guardado exitoso.")

def agregar_producto(lista_productos):
    """Pide datos al usuario y los agrega a la lista de diccionarios."""
    print("\nAgregar Nuevo Producto")
    
    # 1. Solicitamos datos del usuario
    nombre_nuevo = input("Ingrese el nombre del nuevo producto: ").strip()
    precio_nuevo = float(input("Ingrese el precio: "))
    cantidad_nueva = int(input("Ingrese la cantidad (stock): "))

    # 2. Creamos el nuevo diccionario y lo agregamos a la lista
    nuevo_producto = {
        "nombre": nombre_nuevo,
        "precio": precio_nuevo,
        "cantidad": cantidad_nueva
    }
    lista_productos.append(nuevo_producto)
    
    print(f"\nProducto '{nombre_nuevo}' agregado exitosamente a la lista en memoria.")

def mostrar_productos(lista_productos):
    """Muestra los productos desde la lista de diccionarios."""
    print("\nListado de Productos Actualizados")
    if not lista_productos:
        print("La lista de productos está vacía.")
        return
        
    for p in lista_productos:
        print(f"Producto: '{p['nombre']}' | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Ejecución del Programa
# 1. Cargamos la informacion inicial
inventario = cargar_productos_en_lista(nombre_archivo)

# 2. Mostramos la informacion actual
mostrar_productos(inventario)

# 3. Pedimos y agregamos un nuevo producto 
agregar_producto(inventario)

# 4. Mostramos la lista con la nueva adición
mostrar_productos(inventario)

# 5. Guardamos los productos actualizados
guardar_productos(inventario, nombre_archivo)