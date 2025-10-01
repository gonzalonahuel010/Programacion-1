""" 
La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las 
copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que 
utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar 
vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. 
Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario 
elija salir.
"""
#Este programa es un sistema de gestion de biblioteca, con las respectivas opciones solicitadas; le puse de nombre TUBIBLIOGESTiON.

#Inicializacion de listas para titulos y ejemplares disponibles.
titulos = []
ejemplares = []

#Bucle principal del programa, se mantiene hasta que el usuario elija opcion 8 (Salir).
while True:
    print()
    print("Bienvenido a TUBIBLIOGESTiON, tu sistema de gestion para bibliotecas favorito!")
    print()
    print("\nMENÚ DE GESTIÓN DE BIBLIOTECA")
    print("1. Ingresar títulos iniciales")
    print("2. Ingresar ejemplares para cada título")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad de un título")
    print("5. Listar libros agotados")
    print("6. Agregar nuevo título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    print()
    
    #Validacion de opciones del menu (debe acceder valor entre 1 y 8).
    opcion = int(input("A que opcion desea acceder (1-8)?: "))
    while opcion <1 or opcion >8:
        print("Opcion invalida, intente nuevamente!")
        opcion = int(input("A que opcion desea acceder (1-8)?: "))

    #Estructura match-case para manejo de opciones.
    match opcion:

        #1.Ingresar titulos iniciales.
        case 1:
            es_numero = False
            #Validacion de entrada valida (se verifica que el titulo no este vacio ni repetido antes de agregarlo).
            while not es_numero:
                cantidad = input("Ingrese cuantos titulos desea ingresar: ")
                if cantidad.isdigit():
                    cant_titulos_iniciales = int(cantidad)
                    es_numero = True
                else:
                    print("Entrada inválida. Por favor, ingrese un número entero positivo.")
            #Ingreso de titulos acorde a cantidad ingresada y respetando validaciones (se verifica que sea un numero entero no negativo).
            for i in range (cant_titulos_iniciales):
                es_vacio = False
                while not es_vacio: 
                    titulo = input(f"Ingrese el titulo del libro que desea agregar {i+1} - ") # i + 1 para que el titulo corresponda al primer titulo.
                    if titulo == "":
                        print("Entrada inválida, no puede quedar vacio.") 
                    elif titulo in titulos:
                         print("Titulo repetido. Intente con otro.")
                    else:
                        es_vacio = True
                titulos.append(titulo)

        #2. Ingresar cantidad de ejemplares disponibles de cada titulo.
        case 2:
            for i in range(len(titulos)):
                mayor_0 = False
                #Validaciones de entrada valida.
                while mayor_0 == False:
                    cantidad = int(input(f"Cuantos ejemplares hay de '{titulos[i]}'?: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente nuevamente.")
                    else:
                        ejemplares.append(cantidad)
                        mayor_0 = True
        
        #3. Mostrar el catalogo (incluyendo titulos con ejemplares en 0).
        case 3:
            print("\nCATALOGO DE LIBROS:")
            if len(titulos) == 0:
                print("El catalogo esta vacio aun! Ingrese titulos primeros.")
            for i in range(len(titulos)):
                print(f"'{titulos[i]}' -> {ejemplares[i]} ejemplares")

        #4. Consultar disponibilidad de un titulo en especifico (se verifica si existe el titulo antes de mostrar su disponibilidad).
        case 4:
            if len(titulos) == 0:
                print("El catalogo esta vacio aun! Ingrese titulos primeros.")
            #Validaciones de entrada.
            existe = False
            while not existe:
                nombre_titulo = input("Ingrese el nombre del titulo a consultar: ")
                for i in range(len(titulos)):
                    if nombre_titulo == titulos[i]:
                        print(f"'{titulos[i]}' -> {ejemplares[i]}")
                        existe = True
                        break            
                if not existe:
                    print("Ese título no se encuentra en el catálogo.")

        #5. Listado de libros agotados (se verifica que titulos tienen ejemplares = 0).
        case 5:
            if len(titulos) == 0:
                print("El catalogo esta vacio aun! Ingrese titulos primeros.")
            agotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"Libro '{titulos[i]}' agotado")
                    agotados = True
            if not agotados:
                print("No hay titulos agotados")
        
        #6. Agregar nuevo titulo y sus respectivos ejemplares(se valida que el titulo no sea vacio ni este repetido y que la cantidad de ejemplares sea un numero valido).
        case 6:
            #Validaciones de entrada de titulo.
            es_vacio = False
            while not es_vacio:
                nuevo_titulo = input("Ingrese el titulo del nuevo libro: ")
                if nuevo_titulo == "":
                    print("El titulo del libro debe contener al menos un caracter.")
                elif nuevo_titulo in titulos:
                    print("Titulo repetido. Pruebe con otro.")
                else:
                   es_vacio = True
                   titulos.append(nuevo_titulo)
            es_numero = False
            #Validaciones de entrada de ejemplares.
            while not es_numero:
                cantidad = input("Ingrese la cantidad de ejemplares disponibles: ")
                if cantidad.isdigit():
                    es_numero = True
                    nuevo_ejemplar = int(cantidad)
                    ejemplares.append(nuevo_ejemplar)
                else:
                    print("Entrada inválida. Por favor, ingrese un número entero positivo.") 

        #7. Actualizacion de ejemplares en caso de prestamo o devolucion (se verifica el sock para ver si hay ejemplares disponibles).
        case 7:
            if len(titulos) == 0:
                print("El catalogo esta vacio aun! Ingrese titulos primeros.")
            else:
                print("\nLibros disponibles:")
                for i in range(len(titulos)):
                    print(f"{i}- '{titulos[i]}' -> ({ejemplares[i]} ejemplares)")
                #Validaciones de indice del libro a modificar.
                es_valido = False
                while not es_valido:
                    eleccion = input("Ingrese el indice del libro que desea modificar: ")
                    if eleccion.isdigit():
                        indice = int(eleccion)
                        if 0 <= indice < len(titulos):
                            es_valido = True
                        else:
                            print("No existe ese indice de libro. Intente nuevamente.")
                    else:
                        print("Entrada inválida. Ingrese un número entero.")

                #Menu para opciones de prestamo o devolucion.
                print("\nComo desea proceder?:")
                print("1. Registrar préstamo")
                print("2. Registrar devolución")

                #Validacion de opciones.
                opcion_valida = False
                while not opcion_valida:
                    opcion = input("Ingrese la opcion que desee (1-2): ")
                    if opcion == "1":
                        if ejemplares[indice] > 0:
                            ejemplares[indice] -= 1
                            print(f"Se ha registrado correctamente el prestamo de {titulos[indice]} \nQuedan {ejemplares[indice]} ejemplares disponibles.")
                        else:
                            print("No hay ejemplares disponibles para prestamo.")
                        opcion_valida = True
                    elif opcion == 2:
                        ejemplares[indice] += 1
                        print(f"Se ha registrado correctamente la devolucion de {titulos[indice]} \nQuedan {ejemplares[indice]} ejemplares disponibles.")
                        opcion_valida = True
                    else:
                        print("Opcion invalida. Ingrese 1 o 2 para proceder.")
        
        #Salir del programa (fin del bucle).
        case 8:
            print(f"Gracias por usar TUBIBLIOGESTiON\n¡Hasta pronto! ")
            break



