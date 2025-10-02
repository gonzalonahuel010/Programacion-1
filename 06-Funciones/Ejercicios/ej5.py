""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función. """

def segundos_a_horas(segundos):
    #1hs = 3600s
    return segundos//3600

segundos = int(input("Ingrese la cantidad de segundos: "))
hora = segundos_a_horas(segundos)
print(f"Usted ingreso: {segundos} segundo/s que equivale a: {hora} hora/s")