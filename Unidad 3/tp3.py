"Trabajo Practico unidad 3"
""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

age = int(input("Ingrese su edad: "))
if age > 18:
    print("Es mayor de edad")
else:
    print ('No es mayor de edad')



""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”. """
nota = float(input("Ingrese su nota: "))
intentos = 3
if nota >= 6 and nota < 11:
    print("Aprobado!!")
elif (nota <= 0 or nota >= 11) and intentos != 0:
    while (intentos != 0):
        print("Numero de nota invalido, vuelva a ingresar su nota")
        nota = float(input("Ingrese su nota: "))
        intentos -= 1
    if intentos == 0:
        print("Demasiados intentos incorrectos, vuelva a intentar mas tarde")
else:
    print("Desaprobado")



""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. """
numero = int(input("Ingrese un numero par: "))
intentos = 3
if numero%2==0 and numero != 0 and numero > 0:
    print("Ha ingresado un numero par")
else:
    while (intentos != 0):
        print("Por favor, ingrese un número par")
        numero = int(input("Ingrese un numero par: "))
        intentos-=1



""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años. """

age = int(input("Ingrese su edad: "))
intentos = 3
if age < 12 and age != 0 :
    print("Es Ninio/a")
elif age >= 12 and age < 18:
    print ("Es Adoloscente")
elif age >= 18 and age < 30:
    print("Es Adulto joven")
elif age >= 30:
    print("Es Adulto")
else:
    while intentos != 0:
        print("Ingrese un numero mayor a 0.")
        age = int(input("Ingrese su edad: "))
        intentos -=1
    if intentos == 0:
        print("Vuelva a intentarlo mas tarde")
         
        

""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string. """

password = input("Ingrese su contrasenia: ")
intentos = 3
if len(password) >= 8 and len(password) <=14:
    print("Ha ingresado una contraseña correcta")
elif len(password) < 8 or len(password) > 14:
    while intentos != 0:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
        password = input("Ingrese su contrasenia: ")
        intentos -=1
    if intentos == 0:
        print("Demasiados intentos incorrectos, vuelva a intentarlo mas tarde")



""" 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria. """

import random, statistics
numeros_aleatorios = [random.randint(1, 100) for i in range(10)]
sesgo_positivo = False
sesgo_negativo = False
sin_sesgo = False
media= statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    sesgo_positivo = True
    if sesgo_positivo:
        print("Sesgo positivo: ",media)
elif media <  mediana and mediana < moda:
    sesgo_negativo = True
    if sesgo_negativo:
        print("Sesgo negativo: ", mediana)
else:
    sin_sesgo = True
    if(sin_sesgo):
        print("Sin sesgo: ",moda)



""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla. """
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in ('a', 'e', 'i', 'o', 'u'):
    frase += '!'  
print (frase)



""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese la opcion que desea: \n1. Si quiere su nombre en mayúsculas.\n2. Si quiere su nombre en minúsculas.\n3. Si quiere su nombre con la primera letra mayúscula."))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print (nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion incorrecta. Vuelva a intentarlo")
    opcion = int(input("Ingrese la opcion que desea: \n1. Si quiere su nombre en mayúsculas.\n2. Si quiere su nombre en minúsculas.\n3. Si quiere su nombre con la primera letra mayúscula."))



""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

escala = int(input("Ingrese la magnitud del terremoto: "))
if escala < 0:
    print("La magnitud no puede ser menor a 0.")
    escala = int(input("Ingrese la magnitud del terremoto: "))
elif escala < 3 :
    print("Muy leve")
elif escala >= 3 and escala < 4:
    print("Leve")
elif escala >= 4 and escala < 5:
    print("Moderado")
elif escala >= 5 and escala < 6:
    print("Fuerte")
elif escala >= 6 and escala < 7:
    print("Muy fuerte")
else:
    print("Extremo")



""" 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
Desde el 21 de diciembre hasta el 20 de marzo (incluidos)       HN Invierno HS Verano
Desde el 21 de marzo hasta el 20 de junio(incluidos)            HN Primavera HS Otonio
Desde el 21 de junio hasta el 20 de septiembre (incluidos)      HN Verano HS Invierno
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)  HN Otonio HS Primavera
"""
hemisferio = input("Ingrese si se encuentra en el Hemisferio Sur o Norte: ")
mes = int(input("Ingrese mes actual(1-12): "))
dia = int(input("Ingrese que dia es(1-31): "))
estacion = ""
if hemisferio.lower() not in ("sur", "norte"):
    hemisferio = input("Ingrese si se encuentra en el Hemisferio Sur o Norte")
if dia not in range(1,32):
    dia = int(input("Ingrese que dia es: "))
if mes not in range(1,13):
    mes = int(input("Ingrese mes actual: "))

fecha = (mes,dia)

if fecha >= (12,21) or fecha <= (3,20):
    estacion = "Invierno" if hemisferio.capitalize() == "Norte" else "Verano"
elif fecha >= (3,21) and fecha <= (6,20):
    estacion = "Primavera" if hemisferio.capitalize() == "Norte" else "Otonio"
elif fecha >= (6,21) and fecha <= (9,20):
    estacion = "Verano" if hemisferio.capitalize() == "Norte" else  "Invierno"
elif fecha >= (9,21) and fecha <= (12,20):
    estacion = "Otonio" if hemisferio.capitalize() == "Norte" else "Primavera"

print(f"Segun la fecha ingresada: {fecha}, estas en {estacion}")
