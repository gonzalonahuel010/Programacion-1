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