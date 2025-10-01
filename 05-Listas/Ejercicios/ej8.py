""" 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia. """
notas = [[10,5,7],[10,10,10],[8,6,7],[10,9,9],[6,5,8]]
estudiantes = ["Juan", "Jose", "Carlos", "Roberto", "Diego"]
materias = ["Lengua", "Fisica", "Biologia"]
# i recorre estudiantes
for i in range(len(notas)):
    suma = 0
    #j recorre cada materia
    for j in range(len(notas[i])):
        #accedemos a la nota i en la materia j
        suma+= notas[i][j]
    promedio = suma / len(notas[i])
    print(f"{estudiantes[i]} -> Promedio: {promedio}")
    