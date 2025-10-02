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