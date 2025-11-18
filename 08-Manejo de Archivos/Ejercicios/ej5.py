""" 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
 """
nombre_archivo = "C:/Users/gonza/OneDrive - TUPAD UTN/UTN/Programacion-1/08-Manejo de Archivos/Ejercicios/productos.txt"

def cargar_productos_en_lista_simple():
    """
    Lee el archivo de productos y carga los datos en una lista de diccionarios.
    """
    productos = []
    print(f"\nCargando productos desde '{nombre_archivo}'...")

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