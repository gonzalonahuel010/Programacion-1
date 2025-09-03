""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745 """
num = input("Ingrese un numero: ")
num_reves = ""
for i in range(len(num)-1,-1,-1):
    num_reves += num[i]
print(f"Numero original: {num}\nNumero invertido: {num_reves}")