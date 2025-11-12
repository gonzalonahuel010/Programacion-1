""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:
contactos = {"Juan": "123456","Ana":"987654"}
Consultar "Juan" muestra "123456" """

contactos = {}
while len(contactos) < 5:
    nombre_invalido = False
    nombre = input("Ingrese el nombre del contacto: ")
    if not nombre.isalpha():
        print("Nombre invalido, vuelve a intentar")
        continue
    else:
        numero = input(f"Ingrese numero de telefono del contacto '{nombre}': ")
        if not numero.isdigit():
            print("Numero invalido, vuelve a intentar")
            continue
        contactos[nombre] = numero
    
print (contactos)