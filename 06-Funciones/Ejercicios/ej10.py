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