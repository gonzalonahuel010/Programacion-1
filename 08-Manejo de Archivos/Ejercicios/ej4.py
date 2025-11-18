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