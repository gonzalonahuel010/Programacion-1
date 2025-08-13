# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla. """
nombre = input("Ingrese su nombre: ")
saludo = "Hola " + nombre
print(saludo)

""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla. """
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")

""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro """
pi = 3.14
radio = float(input("Ingrese el radio de un circulo: "))
area = pi * (radio**2)
perimetro = pi * radio
print(f"Area = {area}cm y Perimetro = {perimetro}cm")

""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale. """
segundos = int(input("Ingrese cantidad de segundos para pasar a horas: "))
hora = segundos/3600
print(f"{segundos} segundos equivale a {hora} horas")

""" 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número. """
n = int(input("Ingrese un numero: "))
for i in range(1,11):
    print (f"{n}x{i} = {n*i}")

""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el esultado de sumarlos, dividirlos, multiplicarlos y restarlos. """
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
print(f"{n1}+{n2} = {n1+n2}")
print(f"{n1}-{n2} = {n1-n2}")
print(f"{n1}x{n2} = {n1*n2}")
print(f"{n1}/{n2} = {n1/n2}")

""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. imc = peso en kg/altura en m2"""
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingerese su peso: "))
imc = peso/(altura**2)
print (imc)

""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32 """
temp = float(input("Ingrese temperatura en Celsius: "))
farenheit = 9/5 * temp + 32
print(farenheit)

""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un segundo numero: "))
n3 = int(input("Ingrese un tercero numero: "))
promedio = (n1+n2+n3)/3
print (promedio)

