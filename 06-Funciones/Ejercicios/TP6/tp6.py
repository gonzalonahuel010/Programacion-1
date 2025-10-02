""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal. """

def imprimir_hola_mundo():
    print ("Hola Mundo!")

imprimir_hola_mundo()

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario. """

def saludar_usuario(nombre):
    print (f"Hola {nombre}!")

nombre = input("Cual es su nombre?: ")

saludar_usuario(nombre)

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados. """

def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal()

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

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción. """

def tabla_multiplicar(numero):
    for i in range(1,11):
        print (numero*i)    
num = int(input("Ingrese un numero: "))
tabla_multiplicar(num)

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara. """

def operaciones_basicas(a, b):
    sum = a+b
    res = a-b
    mult = a*b
    div = a/b
    if a < b:
        suma = print(f"\nSuma de {a} y {b}: {sum}\n")
        resta = print(f"Resta de {a} y {b}: {res}\n")
        multiplicacion = print(f"Multipliacion de {a} y {b}: {mult}\n")          
        div=b/a
        division = print(f"Division de {b} y {a}: {div}\nLa divison la dimos vuelta porque {b} es mas grande que {a}\n")
    else:
        suma = print(f"\nSuma de {a} y {b}: {sum}\n")
        resta = print(f"Resta de {a} y {b}: {res}\n")
        multiplicacion = print(f"Multipliacion de {a} y {b}: {mult}\n")          
        division = print(f"Division de {b} y {a}: {div}\n")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operaciones_basicas(num1,num2)

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales. """

def calcular_imc(peso, altura):
    return peso/(altura**2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros y centimetros: "))
print(calcular_imc(peso,altura))

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """

def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

celcius = int(input("Ingrese la tempura Celsius: "))
farenheit = celsius_a_fahrenheit(celcius)
print(f"{celcius} grados Celsius es equivalente a {farenheit} grados Farenheit.")

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """

def calcular_promedio(a, b, c):
    return (a+b+c)/3

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

promedio = calcular_promedio(a,b,c)

print(f"El promedio de {a},{b} y {c} es: {promedio}")