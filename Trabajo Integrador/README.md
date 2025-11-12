# README — Gestor de Países (CLI)

Aplicación de consola en Python para **gestionar un dataset de países**: agregar, actualizar, eliminar, buscar/filtrar/ordenar y persistir en CSV.

> **Esta versión del README está adaptada al código actual**, que:
> - Lee el CSV desde una **ruta absoluta de Windows**.
> - Usa **delimitador `;`** (`delimiter=';'`) y **codificación `utf-8-sig`** al leer.
> - Normaliza **cabeceras** a minúsculas para compararlas de forma **no sensible a mayúsculas**.
> - Permite **superficie = 0** *solo* durante la carga desde CSV (no en altas/actualizaciones interactivas).
>
> Tené en cuenta que, al **guardar**, `csv.DictWriter` usa **coma** por defecto (`,`) como separador, por lo que el archivo guardado **no** tendrá `;` a menos que modifiques el código de guardado. Lee la sección de *Formato de CSV* para mantener la coherencia.

---

## 🚀 Características principales

- **Menú interactivo** para: agregar, actualizar, eliminar, buscar/filtrar/ordenar y mostrar países.
- **Validaciones centralizadas** de entradas (enteros positivos, textos alfabéticos, opciones).
- **Búsqueda** por fragmento de nombre y **filtro** por continente.
- **Ordenación** por nombre, población o superficie (asc/desc).
- **Formateo** de números con puntos como separador de miles **solo al imprimir** (no en el CSV).
- **Mensajes claros** de error/confirmación e informes de filas ignoradas en la carga.

---

## 📦 Requisitos

- Python **3.8+**
- Sin dependencias externas (solo `csv`, `os`, `re` de la librería estándar).

---

## 📁 Ruta y formato de CSV

### Ruta de entrada
El programa intenta leer el archivo en:
```
C:/Users/gonza/OneDrive - TUPAD UTN/UTN/Programacion-1/Trabajo Integrador/dataset_paises.csv
```
Podés cambiar esta ruta editando la constante `ARCHIVO_PAISES` al inicio del script.

### Parámetros de lectura
- **Codificación**: `utf-8-sig`
- **Delimitador**: `;` (punto y coma)
- **Cabeceras obligatorias** (insensibles a mayúsculas): `nombre`, `poblacion`, `superficie`, `continente`

> Si las cabeceras no coinciden con ese conjunto, el archivo se rechaza y se muestran las cabeceras leídas para diagnóstico.

### **Importante sobre el guardado**
La función de guardado usa `csv.DictWriter` sin `delimiter`, por lo que **guardará con coma (`,`)**. Si querés mantener `;` para entrada y salida, cambiá:
```python
escritor = csv.DictWriter(archivo, fieldnames=CABECERAS_ESPERADAS, delimiter=';')
```
y asegurate de abrir también con `newline=''` y `encoding='utf-8'` (o `utf-8-sig` si necesitás BOM).

### Ejemplo de CSV **de entrada** con `;`
```csv
nombre;poblacion;superficie;continente
Argentina;45376763;2780400;América
España;47351567;505990;Europa
Japón;125360000;377975;Asia
```

> **Nota:** Durante la **carga** se acepta `superficie = 0` (por `permite_cero=True`). En el **alta/actualización** interactiva se exige `superficie >= 1`.

---

## 🧭 Uso (menú)

```
==============================================
         🌎 GESTOR DE PAÍSES 🌎
==============================================
1. ➕ Agregar nuevo país
2. ✏️ Actualizar país existente
3. 🗑️ Eliminar país
4. 🔍 Buscar/Filtrar/Ordenar países
5. 📜 Mostrar todos los países
6. 💾 Guardar cambios a CSV
7. 🚪 Salir
==============================================
```

- **1 Agregar**: valida nombre (alfabético), población/superficie (enteros > 0) y continente (alfabético). Evita duplicados por nombre exacto.
- **2 Actualizar**: solicita nombre **exacto**; permite dejar campos en blanco para mantener valores; muestra resumen de cambios.
- **3 Eliminar**: solicita nombre **exacto** y confirmación explícita `si/no`.
- **4 Buscar/Filtrar/Ordenar**:
  - Buscar por **[N]ombre** (fragmento, no sensible a mayúsculas).
  - Filtrar por **[C]ontinente** (igualdad exacta, alfabético).
  - Ordenar por **Nombre/Población/Superficie** y elegir **[A]scendente** o **[D]escendente**.
- **5 Mostrar todos**: imprime una tabla con columnas alineadas.
- **6 Guardar**: persiste el estado actual en `ARCHIVO_PAISES` (ver nota sobre separador).
- **7 Salir**: cierra el programa.

---

## ✅ Reglas de validación (detalle)

- **Enteros** (`poblacion`, `superficie`):
  - Solo dígitos (`.isdigit()`), **≥ 1** en altas/actualizaciones.
  - Rango máximo por defecto: `población <= 2.000.000.000`, `superficie <= 200.000.000`.
  - **Carga desde CSV**: `superficie` acepta **0** (`permite_cero=True`).
- **Cadenas** (`nombre`, `continente`):
  - Solo letras (incluye tildes y `ñ`) y espacios: `^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$`.
- **Opciones validadas**: confirmaciones `si/no` mediante lista de opciones permitidas.
- **Cabeceras CSV**: comparación insensible a mayúsculas (normalizadas a minúsculas).

---

## 🧩 Funciones clave

- `cargar_paises_desde_csv(ruta)`: valida cabeceras, lee con `;` y `utf-8-sig`, limpia/convierte filas; reporta filas ignoradas.
- `guardar_paises_a_csv(lista)`: guarda el CSV (por defecto con **coma**); podés ajustar `delimiter=';'` para coherencia.
- `validar_y_obtener_entrada(...)`: **núcleo** de validación de entradas (enteros, cadenas, opciones, rangos, vacío permitido).
- `buscar_pais_por_nombre(lista, nombre, exacto=False)`: búsqueda exacta o por fragmento (case-insensitive).
- `mostrar_lista_paises(lista)` / `mostrar_pais(pais)`: salida amigable y alineada.

---

## 🧪 Ejemplos de interacción

**Agregar país**
```
Nombre (Obligatorio): Chile
Población (int, ej: 45000000 - Mín 1): 19107216
Superficie (int, km² - Mín 1): 756102
Continente (Obligatorio, solo letras): América
 País 'Chile' agregado exitosamente.
```

**Eliminar país**
```
Ingrese el nombre EXACTO del país a eliminar: Japón
¿Está seguro que desea eliminar este país? (si/no): si
 Éxito: País 'Japón' eliminado de la lista.
```

---

## 🛠️ Solución de problemas

- **“Archivo no encontrado”**  
  Verificá la ruta absoluta en `ARCHIVO_PAISES`. Si usás OneDrive, comprobá que el archivo esté sincronizado localmente.
- **“Error de formato en CSV: cabeceras…”**  
  Confirmá que las cabeceras sean exactamente `nombre;poblacion;superficie;continente` (en cualquier casing, sin espacios extra).
- **Aparecen caracteres raros al inicio del primer encabezado**  
  Usar `encoding='utf-8-sig'` soluciona el BOM en archivos generados por Excel.
- **Separador inconsistente entre leer y guardar**  
  Si leés con `;` y guardás con `,`, luego Excel puede abrirlos distinto. Para coherencia, definí `delimiter=';'` también en el guardado.
- **Superficie = 0**  
  Aceptada solo al **cargar**; en altas/actualizaciones se exige `>= 1`.

---

## 🗺️ Roadmap (ideas de mejora)

- Unificar separador (`;`) en lectura y guardado.
- Lista cerrada de continentes (América, Europa, Asia, África, Oceanía, Antártida).
- Tests unitarios (pytest) de validaciones y flujo.
- Exportación/Importación en JSON.
- Paginación en la vista de resultados largos.


---

## 🧾 Notas finales
- Los separadores de miles con puntos aparecen **solo al imprimir**; en CSV se guardan números **sin** separadores.
- El flujo principal corre en `menu_principal()` dentro del bloque `if __name__ == "__main__":`.
- encoding='utf-8-sig' para eliminar caracteres invisibles.
- Ruta al archivo debe estar completa para correcta lectura del mismo.
