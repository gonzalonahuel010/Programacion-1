""" 1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja. """

notas = []
suma = 0
max_nota = 1
min_nota = 10
while len(notas) < 10:
    nota = int(input("Ingrese una nota: "))
    if nota <1 or nota > 10 :
        nota = int(input("Ingrese una nota valida (1-10): "))
    notas.append(nota)
    if nota > max_nota:
        max_nota = nota
    if nota < min_nota :
        min_nota = nota
print(notas)
for nota in range(len(notas)):
    suma += notas[nota]
    print (suma)
promedio = suma / len(notas)
print("promedio: ",promedio)
print("max: ",max_nota)
print("min: ",min_nota)

