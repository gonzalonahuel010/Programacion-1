""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados. """

def calcular_area_circulo(radio):
    pi = 3.1416
    return pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    pi = 3.1416
    return 2 * pi * radio

radio = int(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print (f"El area del circulo es: {radio}\n El perimetro del circulo es: {perimetro}")
