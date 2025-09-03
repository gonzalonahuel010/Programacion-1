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
         
        
        
