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