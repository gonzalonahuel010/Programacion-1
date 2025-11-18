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