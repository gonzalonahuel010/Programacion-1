""" 2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.  """
products = []
while len(products) < 5:
    product = input("Ingrese un producto: ")
    products.append(product)
print("Lista original: ", products)
products_alf = sorted(products)
print("Lista ordenada alfabeticamente: ", products_alf)
eliminar = input("¿Que producto desea eliminar? " )
if eliminar in products:
    products_alf.remove(eliminar)
else:
    eliminar = input("¿Que producto desea eliminar? " )

print ("Lista ordenada alfabeticamente: ",products_alf)