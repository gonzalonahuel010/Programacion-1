""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """

def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

celcius = int(input("Ingrese la tempura Celsius: "))
farenheit = celsius_a_fahrenheit(celcius)
print(f"{celcius} grados Celsius es equivalente a {farenheit} grados Farenheit.")