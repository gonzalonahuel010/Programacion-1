""" 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana. """

ventas = [
    [100, 50, 60, 60, 76, 13, 100],  # PC
    [100, 50, 60, 60, 76, 63, 100],  # Notebook
    [100, 10, 60, 40, 56, 43, 100],  # Celular
    [100, 60, 60, 60, 76, 98, 100]   # Bicicleta
]

productos = ["PC", "Notebook", "Celular", "Bicicleta"]

# 1. Mostrar el total vendido por cada producto
print("🔹 Total vendido por cada producto:")
totales_productos = []
for i in range(len(ventas)):
    producto = productos[i]
    lista_ventas = ventas[i]
    total = 0
    for venta in lista_ventas:
        total += venta
    totales_productos.append(total)
    print(f"{producto}: {total} unidades")

# 2. Mostrar el día con mayores ventas totales
mayor_total = 0
dia_mayor = 0
for dia in range(7):
    total_dia = 0
    for producto in range(4):
        total_dia += ventas[producto][dia]
    if total_dia > mayor_total:
        mayor_total = total_dia
        dia_mayor = dia
print(f"\n🔹 El día con mayores ventas totales fue el día {dia_mayor + 1} con {mayor_total} unidades vendidas.")

# 3. Indicar cuál fue el producto más vendido en la semana
indice_max = 0
maximo = totales_productos[0]
for i in range(1, len(totales_productos)):
    if totales_productos[i] > maximo:
        maximo = totales_productos[i]
        indice_max = i
print(f"\n🔹 El producto más vendido en la semana fue {productos[indice_max]} con {maximo} unidades.")
