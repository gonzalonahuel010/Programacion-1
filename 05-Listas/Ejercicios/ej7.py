""" 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica. """
suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0
temperaturas = [[5,4,5,6,10,11,12],[20,30,33,31,24,28,29]]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]
promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)
print(f"Promedio de temperaturas minimas: {promedio_min}")
print(f"Promedio de temperaturas maximas: {promedio_max}")

for i in range(len(temperaturas)):
    # calculamos la aplitud maxima y minima del dia
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud :
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i

print("Mayor amplitud térmica:", mayor_amplitud, "°C")
print("Día con mayor amplitud:", dias_semana[dia_mayor_amplitud])