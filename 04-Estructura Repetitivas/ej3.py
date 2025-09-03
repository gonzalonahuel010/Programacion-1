""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores. """

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero "))
mayor = 0
menor = 0
suma = 0

if num1 < num2:
    mayor = num2
    menor = num1
else:
    mayor = num1
    menor = num2
for i in range (menor+1,mayor):
    suma += i
    print (suma)
print (suma)

