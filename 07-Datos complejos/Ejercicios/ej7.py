""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

aprobados_parcial_1 = {101, 103, 105, 107, 109, 110}
aprobados_parcial_2 = {103, 104, 105, 106, 110, 111}

print(f"Aprobaron Parcial 1: {aprobados_parcial_1}")
print(f"Aprobaron Parcial 2: {aprobados_parcial_2}")

# 1. Alumnos que aprobaron AMBOS parciales (Intersección)
ambos_parciales = aprobados_parcial_1.intersection(aprobados_parcial_2)

print("\nResultados:")
print(f"Aprobaron ambos parciales (Intersección): {ambos_parciales}")

# --- 2. Alumnos que aprobaron SOLO UNO de los dos (Diferencia Simétrica) ---
solo_uno = aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)

print(f"Aprobaron solo uno de los dos (Diferencia Simétrica): {solo_uno}")
# --- 3. Lista total que aprobó AL MENOS UN parcial (Unión) ---
total_aprobados = aprobados_parcial_1.union(aprobados_parcial_2)

print(f"Total que aprobó al menos uno (Unión): {total_aprobados}")