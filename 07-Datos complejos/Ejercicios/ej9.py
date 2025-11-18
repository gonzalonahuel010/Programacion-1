""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora. """

# Diccionario de la agenda: Clave = tupla (día_semana, hora_24h)
agenda = {
    ("lunes", 9): "Gimnasio",
    ("martes", 14): "Crear proyectos laborales",
    ("miércoles", 11): "Presentación de proyectos",
    ("jueves", 17): "Estudiar matematica",
    ("viernes", 14): "Revisión de código"
}

print("Consultar Eventos de la Agenda")
print("Días: Lunes a Viernes. Horas: 0 a 23.")

# 1. Solicitamos la entrada al usuario
dia_input = input("Ingresá el día de la semana (ej: martes): ").lower()

# Solicitamos la hora y la convertimos directamente a entero
hora_input = int(input("Ingresá la hora (ej: 9): "))

# 2. Creamos la clave de búsqueda como una tupla
clave_busqueda = (dia_input, hora_input)

# 3. Consultamos el diccionario
print("\nResultado de la Consulta")

if clave_busqueda in agenda:
    # Si la tupla existe como clave
    evento = agenda[clave_busqueda]
    print(f"Evento programado para el **{dia_input.capitalize()}** a las **{hora_input:02d}:00**:")
    print(f" '{evento}' ")
else:
    # Si la tupla no existe
    print(f"No hay actividad programada para el **{dia_input.capitalize()}** a las **{hora_input:02d}:00**.")