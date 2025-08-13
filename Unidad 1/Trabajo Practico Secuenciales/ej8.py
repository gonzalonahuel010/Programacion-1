""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. imc = peso en kg/altura en m2"""
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingerese su peso: "))
imc = peso/(altura**2)
print (imc)