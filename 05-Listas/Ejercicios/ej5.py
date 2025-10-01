""" 5)Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada. """

estudiantes = ['Juan', 'Jose', ' Javier', 'Gonzalo', 'Roberto', 'Carlos', 'Joaquin', ' Tomas']
opcion = int(input("Ingrese una opcion: \n1) Agregar un nuevo estudiante\n2)Eliminar uno existente\n3)Mantener igual"))
if opcion == 1:
    nuevo_estudiante = input("Ingrese nombre del estudiante a agregar: ")
    estudiantes.append(nuevo_estudiante)
    print(estudiantes)
if opcion == 2:
    eliminar_estudiante = input("Ingrese nombre del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if eliminar_estudiante == estudiante:
            estudiantes.remove(estudiante)
    print(estudiantes)
if opcion == 3:
    print(estudiantes)
