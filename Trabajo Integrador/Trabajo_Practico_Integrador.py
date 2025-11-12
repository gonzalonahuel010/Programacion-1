import csv
import os
import re 

# --- Constantes y Configuración ---
# Nombre del archivo CSV que almacena todos los datos de los países.
ARCHIVO_PAISES = 'C:/Users/gonza/OneDrive - TUPAD UTN/UTN/Programacion-1/Trabajo Integrador/dataset_paises.csv'

# Definición estricta de las cabeceras.
CABECERAS_ESPERADAS = ["nombre", "poblacion", "superficie", "continente"]

# --- 1. Funciones de Utilidad y Validación ---

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- 1. Simplificación de es_alfabetico ---
def es_alfabetico(valor):
    """
    Verifica si la cadena contiene solo letras, tildes, ñ y espacios,
    utilizando expresiones regulares (regex).
    """
    if not valor:
        return False
    # La expresión regular ^[...]+$ verifica que toda la cadena solo 
    # contenga letras del español (con tildes), 'ñ' y espacios (\s).
    return re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', valor) is not None

# --- FUNCIONES DE VALIDACIÓN ESPECÍFICA ---

def validar_entero(valor, mensaje_error, rango, permite_cero=False):
    """
    Maneja la validación para enteros positivos.
    """
    # 1. Chequeo de formato: ¿Contiene solo dígitos?
    if not valor.isdigit():
        print(f" {mensaje_error}. Se esperaba un número entero.")
        return None

    # Si es solo dígitos, la conversión a entero es segura.
    valor_casteado = int(valor)

    # 2. Validación de positividad (> 0).
    minimo_permitido = 0 if permite_cero else 1

    if valor_casteado < minimo_permitido:
        print(f" {mensaje_error}. Se esperaba un número entero positivo (mínimo {minimo_permitido:,}).".replace(",", "."))
        return None

    # 3. Validación de rango numérico (si existe)
    if rango:
        min_val, max_val = rango

        if valor_casteado < min_val:
            print(f" El valor debe ser mayor o igual a {min_val:,}.".replace(",", "."))
            return None

        if max_val is not None and valor_casteado > max_val:
            print(f" El valor excede el máximo permitido ({max_val:,}).".replace(",", "."))
            return None

    return valor_casteado # Devuelve el entero si todo es correcto

def validar_cadena(valor, mensaje_error, alfabetico_obligatorio, opciones_permitidas):
    """Maneja la validación específica para cadenas."""

    valor = valor.strip() # Limpiar espacios en blanco al inicio/fin

    if alfabetico_obligatorio:
        if not es_alfabetico(valor):
            print(f" {mensaje_error}. Se esperaba un texto alfabético.")
            return None

    # Manejar el chequeo de opciones permitidas
    if opciones_permitidas:
        if valor.lower() not in opciones_permitidas:
            # Reutiliza el mensaje_error general o genera uno específico
            print(f" {mensaje_error}. Opciones permitidas: {', '.join(opciones_permitidas)}.")
            return None

    return valor

# --- FUNCIÓN PRINCIPAL ESTÁNDAR ---

def validar_y_obtener_entrada(
    prompt,
    tipo_esperado,
    puede_ser_vacio = False,
    mensaje_error = "Entrada inválida.",
    rango = None,
    alfabetico_obligatorio = False,
    opciones_permitidas = None # Argumento clave para validar listas de opciones
):
    """
    Solicita y valida la entrada del usuario de manera centralizada.
    """
    while True:
        entrada = input(prompt).strip()

        # 1. Verificacion de Campo Vacío
        if not entrada:
            if puede_ser_vacio:
                return None
            print(" Este campo no puede estar vacío. Intente de nuevo.")
            continue

        # 2. Despacho de la Validación por Tipo
        resultado_validacion = None

        if tipo_esperado == int:
            resultado_validacion = validar_entero(entrada, mensaje_error, rango, permite_cero=False)

        elif tipo_esperado == str:
            # Llama a la función de validación de cadena, que ahora maneja opciones_permitidas
            resultado_validacion = validar_cadena(entrada, mensaje_error, alfabetico_obligatorio, opciones_permitidas)

        # 3. Verificación del Resultado
        if resultado_validacion is not None:
            # Si la validación fue exitosa, se devuelve el valor.
            return resultado_validacion

        # Si llegamos aquí, falló una validación específica, y el bucle continúa.
        continue

def buscar_pais_por_nombre(lista_paises, nombre, exacto=False):
    """Busca países en la lista por su nombre (no sensible a mayúsculas/minúsculas)."""
    nombre_lower = nombre.lower()
    resultados = []

    for pais in lista_paises:
        nombre_pais_lower = pais['nombre'].lower()

        if exacto:
            if nombre_pais_lower == nombre_lower:
                resultados.append(pais)
                break
        else:
            if nombre_lower in nombre_pais_lower:
                resultados.append(pais)
    return resultados

def mostrar_pais(pais):
    """Muestra la información completa de un único país."""
    print("----------------------------------------")
    print(f" Nombre:        {pais['nombre']}")
    # Uso de replace(",", ".") para formato de miles en español
    print(f" Población:     {pais['poblacion']:,} hab.".replace(",", "."))
    print(f" Superficie:    {pais['superficie']:,} km²".replace(",", "."))
    print(f" Continente:    {pais['continente']}")
    print("----------------------------------------")

def mostrar_lista_paises(lista_paises):
    """
    Muestra la lista de países en un formato de tabla usando anchos fijos.
    """
    if not lista_paises:
        print("\n No se encontraron países que cumplan el criterio de búsqueda/filtro.")
        return

    # Definición de anchos para la tabla
    ANCHO_NOMBRE = 30
    ANCHO_CONTINENTE = 15
    ANCHO_POBLACION = 15
    ANCHO_SUPERFICIE = 18
    # ---------------------------------------------------------------------------------

    print(f"\n--- Resultados ({len(lista_paises)} País{'es' if len(lista_paises) != 1 else ''}) ---")

    # 2. Impresión de la Cabecera (usando los anchos fijos)
    print(f"{'Nombre':<{ANCHO_NOMBRE}} | {'Población':>{ANCHO_POBLACION}} | {'Superficie (km²)' :>{ANCHO_SUPERFICIE}} | {'Continente':<{ANCHO_CONTINENTE}}")

    # Cálculo de la longitud total de la línea de separación
    longitud_separador = ANCHO_NOMBRE + 3 + ANCHO_POBLACION + 3 + ANCHO_SUPERFICIE + 3 + ANCHO_CONTINENTE
    print('-' * longitud_separador)

    # 3. Impresión de las Filas de datos
    for p in lista_paises:
        # Formato de números con puntos como separador de miles
        poblacion_str = f"{p['poblacion']:,}".replace(",", ".")
        superficie_str = f"{p['superficie']:,}".replace(",", ".")

        # Recortar el nombre si es demasiado largo para no romper la tabla
        nombre_recortado = p['nombre'][:ANCHO_NOMBRE]

        # Usamos los anchos fijos
        print(f"{nombre_recortado:<{ANCHO_NOMBRE}} | {poblacion_str:>{ANCHO_POBLACION}} | {superficie_str:>{ANCHO_SUPERFICIE}} | {p['continente']:<{ANCHO_CONTINENTE}}")

    print(f"--- Fin de Resultados ({len(lista_paises)} País{'es' if len(lista_paises) != 1 else ''}) ---\n")

# --- 2. Funcionalidades de Archivo y Carga de Datos ---

def cargar_paises_desde_csv(nombre_archivo):
    """
    Lee datos de países desde un archivo CSV. Retorna la lista de países.
    """
    lista_paises = []

    # Validación de existencia de archivo
    if not os.path.exists(nombre_archivo):
        print(f" Archivo '{nombre_archivo}' no encontrado. Se iniciará con una lista vacía.")
        return []

    # Abrir el archivo de manera segura
    with open(nombre_archivo, mode='r', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')

        # Validación de Cabeceras
        # 1. Obtenemos las cabeceras leídas. Si no hay, es un error.
        if not lector.fieldnames:
             print(f" Error de formato en CSV: Archivo vacío o sin cabeceras.")
             return []
        
        cabeceras_leidas_normalizadas = [h.lower() for h in lector.fieldnames]
        """  if not lector.fieldnames or set(CABECERAS_ESPERADAS) != set(lector.fieldnames):
            print(f" Error de formato en CSV: Las cabeceras del archivo no coinciden con las esperadas.")
            return [] """
        if set(CABECERAS_ESPERADAS) != set(cabeceras_leidas_normalizadas):
            # Opcional: imprimir las cabeceras leídas para debug
            print(f" Error de formato en CSV: Las cabeceras del archivo no coinciden con las esperadas.")
            print(f" Cabeceras esperadas: {CABECERAS_ESPERADAS}")
            print(f" Cabeceras leídas (normalizadas): {cabeceras_leidas_normalizadas}")
            return []
        # Lectura y conversión de Filas
        for i, fila in enumerate(lector):
            
            # Limpieza y validación de campos de texto
            nombre_limpio = fila.get('nombre', '').strip()
            continente_limpio = fila.get('continente', '').strip()
            
            if not nombre_limpio or not continente_limpio:
                 print(f" Advertencia: País en línea {i+2} ignorado por tener nombre o continente vacío.")
                 continue

            # Validación de datos numéricos y que sean > 0 
            poblacion = validar_entero(fila.get('poblacion', '0'), "Dato de Población", None, permite_cero=False)
            superficie = validar_entero(fila.get('superficie', '0'), "Dato de Superficie", None, permite_cero=True)
            
            if poblacion is None or superficie is None:
                 print(f" Advertencia: País en línea {i+2} ignorado por datos no numéricos o <= 0.")
                 continue

            pais = {
                'nombre': nombre_limpio,
                'poblacion': poblacion, # Ya casteado y validado
                'superficie': superficie, # Ya casteado y validado
                'continente': continente_limpio
            }

            lista_paises.append(pais)

    print(f"\n Se cargaron {len(lista_paises)} países exitosamente desde el archivo CSV.")
    return lista_paises

def guardar_paises_a_csv(lista_paises):
    """
    Guarda la lista actual de países en el archivo CSV.
    """
    # Abre el archivo para escritura ('w')
    with open(ARCHIVO_PAISES, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CABECERAS_ESPERADAS)
        escritor.writeheader()
        escritor.writerows(lista_paises)

    print(f"\n Éxito: Se guardaron {len(lista_paises)} países en '{ARCHIVO_PAISES}'.")


# --- 3. Funcionalidades del Sistema  ---

def agregar_pais(lista_paises):
    """Agrega un nuevo país a la lista, validando unicidad y los datos de entrada."""
    print("\n--- AGREGAR NUEVO PAÍS ---")

    # Rango de ejemplo, el mínimo 1 ya lo valida validar_entero
    MAX_POBLACION = 2000000000
    MAX_SUPERFICIE = 200000000

    # 1. Obtención y validación de entradas obligatorias
    nombre = validar_y_obtener_entrada("Nombre (Obligatorio): ", str, False, "El nombre debe ser un texto alfabético y no puede estar vacío.", alfabetico_obligatorio=True)
    
    # Si el nombre es None, la validación interna falló.
    if nombre is None:
        return

    # 2. Verificación de unicidad
    if buscar_pais_por_nombre(lista_paises, nombre, exacto=True):
        print(f"\n Error: El país '{nombre}' ya existe en la base de datos. No se agregó.")
        return

    # 3. Pedir el resto de los datos (la validación de tipo se hace dentro de la función)
    poblacion = validar_y_obtener_entrada("Población (int, ej: 45000000 - Mín 1): ", int, False, "La población debe ser un número entero.", rango=(1, MAX_POBLACION))
    if poblacion is None: return

    superficie = validar_y_obtener_entrada("Superficie (int, km² - Mín 1): ", int, False, "La superficie debe ser un número entero.", rango=(1, MAX_SUPERFICIE))
    if superficie is None: return

    continente = validar_y_obtener_entrada("Continente (Obligatorio, solo letras): ", str, False, "El continente debe ser un texto.", alfabetico_obligatorio=True)
    if continente is None: return

    # 4. Creación y adición del diccionario
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }

    lista_paises.append(nuevo_pais)
    print(f"\n País '{nombre}' agregado exitosamente.")


def actualizar_pais(lista_paises):
    """Actualiza los campos de un país existente."""
    print("\n--- ACTUALIZAR PAÍS ---")

    # 1. Solicitar el nombre del país a actualizar
    nombre_busqueda = validar_y_obtener_entrada("Ingrese el nombre EXACTO del país a actualizar: ", str, False, alfabetico_obligatorio=True)

    # 2. Buscar si existe el país
    resultados = buscar_pais_por_nombre(lista_paises, nombre_busqueda, exacto=True)

    if not resultados:
        print(f"\n Error: País '{nombre_busqueda}' no encontrado. No se puede actualizar.")
        return

    pais_a_actualizar = resultados[0]
    cambios_realizados = False
    log_cambios = [] # Registro para el resumen al final

    print(f"\n Actualizando '{pais_a_actualizar['nombre']}'. Deje el campo vacío para mantener el valor actual.")

    # Rango de ejemplo, el mínimo 1 ya lo valida validar_entero
    MAX_POBLACION = 2000000000
    MAX_SUPERFICIE = 200000000

    # 3. Pedir nuevos datos (permite vacío)

    # Actualizar Población
    nueva_poblacion = validar_y_obtener_entrada(
        f"Población actual ({pais_a_actualizar['poblacion']:,}".replace(",", ".") + "): ",
        int, True, "La población debe ser un número entero.", rango=(1, MAX_POBLACION) # Mínimo 1
    )
    if nueva_poblacion is not None and nueva_poblacion != pais_a_actualizar['poblacion']:
        pais_a_actualizar['poblacion'] = nueva_poblacion
        cambios_realizados = True
        log_cambios.append("Población")

    # Actualizar Superficie
    nueva_superficie = validar_y_obtener_entrada(
        f"Superficie actual ({pais_a_actualizar['superficie']:,}".replace(",", ".") + "): ",
        int, True, "La superficie debe ser un número entero.", rango=(1, MAX_SUPERFICIE) # Mínimo 1
    )
    if nueva_superficie is not None and nueva_superficie != pais_a_actualizar['superficie']:
        pais_a_actualizar['superficie'] = nueva_superficie
        cambios_realizados = True
        log_cambios.append("Superficie")

    # Actualizar Continente
    nuevo_continente = validar_y_obtener_entrada(
        f"Continente actual ({pais_a_actualizar['continente']}): ",
        str, True, "El continente debe ser un texto.", alfabetico_obligatorio=True
    )
    if nuevo_continente is not None and nuevo_continente != pais_a_actualizar['continente']:
        pais_a_actualizar['continente'] = nuevo_continente
        cambios_realizados = True
        log_cambios.append("Continente")

    # 4. Mostrar resultado
    if cambios_realizados:
        print("\n--- Resumen de Actualización ---")
        for campo in log_cambios:
             print(f"   {campo} actualizado.")
        print(f"\n Éxito: El país '{pais_a_actualizar['nombre']}' fue actualizado.")
    else:
        print("\nℹ No se realizaron cambios en el país.")


def eliminar_pais(lista_paises):
    """Elimina un país de la lista si el usuario confirma."""
    print("\n--- ELIMINAR PAÍS ---")

    # 1. Solicitar nombre
    nombre_busqueda = validar_y_obtener_entrada("Ingrese el nombre EXACTO del país a eliminar: ", str, False, alfabetico_obligatorio=True)

    # 2. Buscar si existe el país
    for i, pais in enumerate(lista_paises):
        if pais['nombre'].lower() == nombre_busqueda.lower():
            # 3. Mostrar detalles
            print(f"\nSe encontró el siguiente país:")
            mostrar_pais(pais)

            # --- 2. Lógica de Confirmación Simplificada ---
            # Delegamos la validación de 'si' o 'no' a validar_y_obtener_entrada
            confirmacion = validar_y_obtener_entrada(
                "¿Está seguro que desea eliminar este país? (si/no): ",
                str,
                mensaje_error="Respuesta no válida.",
                opciones_permitidas=['si', 'no'] 
            )

            # Si la validación central retorna un valor (nunca None aquí)
            if confirmacion and confirmacion.lower() == 'si':
                # 4. Eliminar por índice (i)
                lista_paises.pop(i)
                print(f"\n Éxito: País '{pais['nombre']}' eliminado de la lista.")
            else:
                print("\nℹ Eliminación cancelada por el usuario.")
            return

    print(f"\n Error: País '{nombre_busqueda}' no encontrado. No se eliminó.")


def buscar_y_filtrar_paises(lista_paises):
    """Permite buscar países por nombre o filtrarlos por continente, y luego ordenarlos."""
    print("\n--- BUSCAR, FILTRAR y ORDENAR PAÍSES ---")

    # 1. Criterios de Búsqueda/Filtro
    criterio = validar_y_obtener_entrada(
        "Buscar por [N]ombre, [C]ontinente o presione [Enter] para ver todo: ",
        str, True
    )

    resultados_filtrados = lista_paises

    if criterio and criterio.lower() in ('n', 'nombre'):
        # La búsqueda por fragmento no exige que el fragmento sea totalmente alfabético
        nombre_buscar = validar_y_obtener_entrada("Ingrese fragmento del nombre a buscar: ", str, False)
        # Se asegura que la búsqueda se realice solo si se obtuvo un nombre válido
        if nombre_buscar:
            temp_filtrados = []
            nombre_buscar_lower = nombre_buscar.lower()
            for p in lista_paises:
                if nombre_buscar_lower in p['nombre'].lower():
                    temp_filtrados.append(p)
            resultados_filtrados = temp_filtrados

    elif criterio and criterio.lower() in ('c', 'continente'):
        # Aquí sí exigimos que el continente sea alfabético 
        continente_filtrar = validar_y_obtener_entrada("Ingrese el continente exacto a filtrar: ", str, False, alfabetico_obligatorio=True)
        # Se asegura que la búsqueda se realice solo si se obtuvo un continente válido
        if continente_filtrar:
            temp_filtrados = []
            continente_filtrar_lower = continente_filtrar.lower()
            for p in lista_paises:
                if p['continente'].lower() == continente_filtrar_lower:
                    temp_filtrados.append(p)
            resultados_filtrados = temp_filtrados

    # 2. Criterios de Ordenación
    ordenar_por = validar_y_obtener_entrada(
        "\nOrdenar por: [N]ombre, [P]oblación, [S]uperficie o presione [Enter] para no ordenar: ",
        str, True
    )

    if ordenar_por:
        key = None
        if ordenar_por.lower() in ('n', 'nombre'):
            key = 'nombre'
        elif ordenar_por.lower() in ('p', 'poblacion'):
            key = 'poblacion'
        elif ordenar_por.lower() in ('s', 'superficie'):
            key = 'superficie'

        if key:
            orden = validar_y_obtener_entrada("Orden [A]scendente o [D]escendente: ", str, False, "Opción no válida. Ingrese A o D.").lower()
            reverso = (orden in ('d', 'descendente'))

            # --- USO DE FUNCIÓN INTERNA PARA ORDENAR ---
            def obtener_clave_ordenacion(pais):
                """
                Función auxiliar que toma un diccionario 'pais' y devuelve el valor
                asociado a la variable 'key' (nombre, poblacion o superficie) definida en el ámbito superior.
                """
                return pais[key]
            
            # Usamos la función con nombre 'obtener_clave_ordenacion'
            resultados_filtrados.sort(key=obtener_clave_ordenacion, reverse=reverso)
            
            print(f"\n Resultados ordenados por {key} en orden {'descendente' if reverso else 'ascendente'}.")


    # 3. Mostrar los resultados finales
    mostrar_lista_paises(resultados_filtrados)


# --- 4. Flujo Principal del Programa ---

def menu_principal():
    """Función principal que gestiona el menú interactivo y el flujo del programa."""

    limpiar_pantalla()
    # 1. Cargar datos al inicio. La lista de países se pasa entre las funciones.
    lista_paises = cargar_paises_desde_csv(ARCHIVO_PAISES)

    while True:
        print("\n==============================================")
        print("         🌎 GESTOR DE PAÍSES 🌎")
        print("==============================================")
        print("1. ➕ Agregar nuevo país")
        print("2. ✏️ Actualizar país existente")
        print("3. 🗑️ Eliminar país")
        print("4. 🔍 Buscar/Filtrar/Ordenar países")
        print("5. 📜 Mostrar todos los países")
        print("6. 💾 Guardar cambios a CSV")
        print("7. 🚪 Salir")
        print("==============================================")

        opcion = validar_y_obtener_entrada("Seleccione una opción (1-7): ", int, False, "Opción no válida.", rango=(1, 7))

        # La validación asegura que opcion no es None y está entre 1 y 7
        if opcion is not None:
             limpiar_pantalla()

             if opcion == 1:
                 agregar_pais(lista_paises)
             elif opcion == 2:
                 actualizar_pais(lista_paises)
             elif opcion == 3:
                 eliminar_pais(lista_paises)
             elif opcion == 4:
                 buscar_y_filtrar_paises(lista_paises)
             elif opcion == 5:
                 mostrar_lista_paises(lista_paises)
             elif opcion == 6:
                 guardar_paises_a_csv(lista_paises)
             elif opcion == 7:
                 print("\n ¡Gracias por usar el Gestor de Países! Saliendo del programa...")
                 break


# Punto de entrada principal
if __name__ == "__main__":
    menu_principal()