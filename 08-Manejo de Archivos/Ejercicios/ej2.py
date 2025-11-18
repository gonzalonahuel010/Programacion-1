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
                