""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno. """

# Inicializamos un diccionario vacío para guardar los datos
alumnos_notas = {}
numero_alumnos = 3
numero_notas = 3

# 1. Solicitamos los datos de los alumnos
for i in range(numero_alumnos):
    print(f"\n--- Alumno {i + 1} de {numero_alumnos} ---")
    
    # Solicitamos el nombre
    nombre = input("Ingresá el nombre del alumno: ")
    
    # Solicitamos y almacenammos las 3 notas en una tupla
    notas_lista = []
    for j in range(numero_notas):
        # Solicitamos la nota y la convertimos directamente a float 
        nota = float(input(f"Ingresá la nota {j + 1}: "))
        notas_lista.append(nota)
                
    # Convertimos la lista de notas a una tupla y la guardamos en el diccionario
    alumnos_notas[nombre] = tuple(notas_lista)

# 2. Calculamos y mostramos el promedio de cada alumno
print("\n" + "="*30)
print("Promedios de los Alumnos")
print("="*30)

# Iteramos sobre el diccionario (clave=nombre, valor=notas_tupla)
for nombre, notas_tupla in alumnos_notas.items():
    # Calculamos la suma de las notas y el promedio
    suma_notas = sum(notas_tupla)
    promedio = suma_notas / len(notas_tupla)
    
    # Mostramos el resultado
    print(f"El promedio de **{nombre}** es: **{promedio:.2f}** (Notas: {notas_tupla})")