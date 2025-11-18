""" 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista. """

nombre_archivo = "C:/Users/gonza/OneDrive - TUPAD UTN/UTN/Programacion-1/08-Manejo de Archivos/Ejercicios/productos.txt"

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