""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro """
pi = 3.14
radio = float(input("Ingrese el radio de un circulo: "))
area = pi * (radio**2)
perimetro = pi * radio
print(f"Area = {area}cm y Perimetro = {perimetro}cm")