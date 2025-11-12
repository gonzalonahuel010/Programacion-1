import csv
import os

def cargar_catalogo():
    """Carga el catálogo desde el archivo CSV sin usar excepciones"""
    # Verifica si el archivo existe antes de intentar abrirlo
    if os.path.exists('catalogo.csv'):
        # Abre archivo en modo lectura con codificación UTF-8 para caracteres especiales
        with open('catalogo.csv', 'r', newline='', encoding='utf-8') as archivo:
            # DictReader convierte cada fila en un diccionario usando la primera fila como claves
            lector = csv.DictReader(archivo)
            catalogo = []
            for fila in lector:
                if fila['CANTIDAD'].isdigit():
                    fila['CANTIDAD'] = int(fila['CANTIDAD'])
                    catalogo.append(fila)
            return catalogo
    else:
        return []

def guardar_catalogo(catalogo):
    """Guarda el catálogo en el archivo CSV"""
    with open('catalogo.csv', 'w', newline='', encoding='utf-8') as archivo:
        # Define los nombres de las columnas del CSV
        campos = ['TITULO', 'CANTIDAD']
        # DictWriter escribe diccionarios como filas en el CSV
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        # Escribir la fila de encabezado con los nombres de los headers
        escritor.writeheader()
        for libro in catalogo:
            # Escribe cada libro del catálogo como una fila en el CSV
            escritor.writerow(libro)

def normalizar_titulo(titulo):
    """Normaliza el título para comparaciones"""
    #Elimina espacios al inicio y al final, divide el sring en palabras, une las palabras con un solo espacio y convierte a minusculas.
    return ' '.join(titulo.strip().split()).lower()

def buscar_libro(catalogo, titulo_buscar):
    """Busca un libro en el catálogo"""
    titulo_normalizado = normalizar_titulo(titulo_buscar)
    for i, libro in enumerate(catalogo):
        if normalizar_titulo(libro['TITULO']) == titulo_normalizado:
            return i, libro
    return -1, None

def validar_cantidad(cantidad_str):
    """Valida que la cantidad sea un entero positivo"""
    if cantidad_str.isdigit():
        #Verifica que el string contenga solo dígitos
        cantidad = int(cantidad_str)
        if cantidad >= 0:
            return True, cantidad
    return False, 0

def ingresar_titulos_multiples(catalogo):
    """Permite cargar varios libros de una vez"""
    print("\n" + "="*40)
    print("INGRESO MULTIPLE DE TITULOS")
    print("="*40)
    
    cantidad_libros_str = input("¿Cuántos libros desea cargar? ")
    
    if not cantidad_libros_str.isdigit():
        print("\nError: Debe ingresar un número válido")
        return catalogo
    
    cantidad_libros = int(cantidad_libros_str)
    
    if cantidad_libros <= 0:
        print("\nError: Debe ingresar un número mayor a 0")
        return catalogo
    
    print(f"\nSe cargarán {cantidad_libros} libros...")
    
    for i in range(cantidad_libros):
        print(f"\n" + "-"*30)
        print(f"Libro {i+1} de {cantidad_libros}")
        print("-"*30)
        
        # Solicita título y validar que no esté vacío
        titulo = input("Título del libro: ").strip()
        if not titulo:
            print("Error: El título no puede estar vacío")
            continue
        
        # Verifica si el libro ya existe en el catálogo
        indice, libro_existente = buscar_libro(catalogo, titulo)
        if libro_existente:
            print("Error: Ya existe un libro con ese título")
            continue

        # Solicita y validar cantidad
        cantidad_str = input("Cantidad de ejemplares: ")
        es_valida, cantidad = validar_cantidad(cantidad_str)
        
        if not es_valida:
            print("Error: La cantidad debe ser un número entero >= 0")
            continue

        # Crea nuevo libro como diccionario
        nuevo_libro = {
            'TITULO': titulo,
            'CANTIDAD': cantidad
        }

        # Agrega libro al catálogo
        catalogo.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado con {cantidad} ejemplares")
    
    print(f"\nProceso de ingreso múltiple finalizado")
    return catalogo

def ingresar_ejemplares(catalogo):
    """Suma ejemplares a un título existente"""
    print("\n" + "="*40)
    print("AGREGAR EJEMPLARES A TITULO EXISTENTE")
    print("="*40)
    
    # Solicita título del libro a actualizar
    titulo = input("Título del libro al que sumar ejemplares: ").strip()
    if not titulo:
        print("\nError: El título no puede estar vacío")
        return catalogo

    # Busca libro en el catálogo
    indice, libro = buscar_libro(catalogo, titulo)

    if libro is None:
        print("\nError: No se encontró el libro en el catálogo")
        return catalogo
    
    print(f"\nLibro encontrado: '{libro['TITULO']}'")
    print(f"Ejemplares actuales: {libro['CANTIDAD']}")
    
    cantidad_str = input("\nCantidad de ejemplares a sumar: ")
    es_valida, cantidad = validar_cantidad(cantidad_str)
    
    if not es_valida:
        print("\nError: La cantidad debe ser un número entero >= 0")
        return catalogo
    
    catalogo[indice]['CANTIDAD'] += cantidad
    print(f"\nSe sumaron {cantidad} ejemplares a '{libro['TITULO']}'")
    print(f"Nuevo total: {catalogo[indice]['CANTIDAD']} ejemplares")
    
    return catalogo

def mostrar_catalogo(catalogo):
    """Muestra todo el catálogo"""
    if not catalogo:
        print("\nEl catálogo está vacío")
        return
    
    print("\n" + "="*50)
    print("CATALOGO COMPLETO DE LA BIBLIOTECA")
    print("="*50)
    
    # Muestra cada libro numerado, empezando desde 1
    for i, libro in enumerate(catalogo, 1):
        # Determina estado según cantidad disponible
        estado = "DISPONIBLE" if libro['CANTIDAD'] > 0 else "AGOTADO"
        print(f"{i}. '{libro['TITULO']}' - {libro['CANTIDAD']} ejemplares [{estado}]")
    
    print(f"\nTotal de libros en catálogo: {len(catalogo)}")

def consultar_disponibilidad(catalogo):
    """Consulta la disponibilidad de un título"""
    print("\n" + "="*40)
    print("CONSULTAR DISPONIBILIDAD")
    print("="*40)
    
    titulo = input("Título a consultar: ").strip()
    
    if not titulo:
        print("\nError: El título no puede estar vacío")
        return
    
    indice, libro = buscar_libro(catalogo, titulo)
    
    if libro is None:
        print("\nError: No se encontró el libro en el catálogo")
        return
    
    # Muestra información detallada del libro
    print(f"\n" + "="*30)
    print("INFORMACION DEL LIBRO")
    print("="*30)
    print(f"Título: '{libro['TITULO']}'")
    
    # Muestra disponibilidad según cantidad
    if libro['CANTIDAD'] > 0:
        print(f"Disponibilidad: {libro['CANTIDAD']} ejemplares disponibles")
    else:
        print(f"Disponibilidad: AGOTADO")

def listar_agotados(catalogo):
    """Lista los libros agotados"""
    print("\n" + "="*40)
    print("LIBROS AGOTADOS")
    print("="*40)
    
    agotados = []
    for libro in catalogo:
        if libro['CANTIDAD'] == 0:
            agotados.append(libro)
    
    if not agotados:
        print("\nNo hay libros agotados en el catálogo")
        return
    
    print(f"\nSe encontraron {len(agotados)} libros agotados:")
    
    for i, libro in enumerate(agotados, 1):
        print(f"{i}. '{libro['TITULO']}'")
    
    print(f"\nSugerencia: Considere reponer estos títulos")

def agregar_titulo_individual(catalogo):
    """Agrega un libro individual al catálogo"""
    print("\n" + "="*40)
    print("AGREGAR TITULO INDIVIDUAL")
    print("="*40)
    
    titulo = input("Título del libro: ").strip()
    
    if not titulo:
        print("\nError: El título no puede estar vacío")
        return catalogo
    
    # Verifica si el libro ya existe
    indice, libro_existente = buscar_libro(catalogo, titulo)
    if libro_existente:
        print("\nError: Ya existe un libro con ese título")
        return catalogo
        
    # Solicita y valida cantidad inicial
    cantidad_str = input("Cantidad inicial de ejemplares: ")
    es_valida, cantidad = validar_cantidad(cantidad_str)
    
    if not es_valida:
        print("\nError: La cantidad debe ser un número entero >= 0")
        return catalogo
    
    # Crea y agrega nuevo libro
    nuevo_libro = {
        'TITULO': titulo,
        'CANTIDAD': cantidad
    }
    catalogo.append(nuevo_libro)
    print(f"\nLibro '{titulo}' agregado con {cantidad} ejemplares")
    
    return catalogo

def actualizar_ejemplares(catalogo):
    """Realiza préstamos o devoluciones"""
    print("\n" + "="*40)
    print("ACTUALIZAR EJEMPLARES")
    print("="*40)
    print("1. Prestamo (restar 1 ejemplar)")
    print("2. Devolucion (sumar 1 ejemplar)")
    print("-"*40)
    
    opcion = input("Seleccione una opción: ")
    
    titulo = input("\nTítulo del libro: ").strip()
    
    if not titulo:
        print("\nError: El título no puede estar vacío")
        return catalogo
    
    indice, libro = buscar_libro(catalogo, titulo)
    
    if libro is None:
        print("\nError: No se encontró el libro en el catálogo")
        return catalogo
    
    print(f"\nLibro seleccionado: '{libro['TITULO']}'")
    print(f"Ejemplares actuales: {libro['CANTIDAD']}")
    
    match opcion:
        case '1':  # Préstamo
            if libro['CANTIDAD'] > 0:
                catalogo[indice]['CANTIDAD'] -= 1
                print(f"\nPrestamo realizado de '{libro['TITULO']}'")
                print(f"Ejemplares restantes: {catalogo[indice]['CANTIDAD']}")
            else:
                print("\nError: No hay ejemplares disponibles para préstamo")
        
        case '2':  # Devolución
            catalogo[indice]['CANTIDAD'] += 1
            print(f"\nDevolucion realizada de '{libro['TITULO']}'")
            print(f"Ejemplares disponibles: {catalogo[indice]['CANTIDAD']}")
        
        case _:
            print("\nError: Opción inválida")
    
    return catalogo

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("SISTEMA DE GESTION DE BIBLIOTECA")
    print("="*50)
    print("1. Ingresar títulos (múltiples)")
    print("2. Ingresar ejemplares a título existente")
    print("3. Mostrar catálogo completo")
    print("4. Consultar disponibilidad")
    print("5. Listar libros agotados")
    print("6. Agregar título individual")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    print("-"*50)

def ejecutar_programa():
    """Función principal del programa"""
    catalogo = cargar_catalogo()
    
    print("\n" + "="*50)
    print("Bienvenido al Sistema de Gestión de Biblioteca!")
    print(f"Catálogo cargado: {len(catalogo)} libros")
    print("="*50)
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-8): ").strip()
        
        catalogo_modificado = False
        
        match opcion:
            case '1':
                catalogo = ingresar_titulos_multiples(catalogo)
                catalogo_modificado = True
            
            case '2':
                catalogo = ingresar_ejemplares(catalogo)
                catalogo_modificado = True
            
            case '3':
                mostrar_catalogo(catalogo)
            
            case '4':
                consultar_disponibilidad(catalogo)
            
            case '5':
                listar_agotados(catalogo)
            
            case '6':
                catalogo = agregar_titulo_individual(catalogo)
                catalogo_modificado = True
            
            case '7':
                catalogo = actualizar_ejemplares(catalogo)
                catalogo_modificado = True
            
            case '8':
                print("\n" + "="*50)
                print("Gracias por usar el Sistema de Gestión de Biblioteca!")
                print("Hasta pronto!")
                print("="*50)
                break
            
            case _:
                print("\nError: Opción inválida. Por favor, seleccione 1-8")
        
        # Guarda cambios si el catálogo fue modificado
        if catalogo_modificado:
            guardar_catalogo(catalogo)
            print("\nCambios guardados exitosamente en el archivo 'catalogo.csv'")

ejecutar_programa()