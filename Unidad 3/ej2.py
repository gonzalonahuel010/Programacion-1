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
