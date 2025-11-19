""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. """

def fibonacci_recursivo(pos):
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada (pos) de forma recursiva.
    """
    # 1. Caso Base 1: Posición 0
    if pos == 0:
        return 0
    
    # 2. Caso Base 2: Posición 1
    elif pos == 1:
        return 1
    
    # 3. Paso Recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

def mostrar_serie_fibonacci():
    """
    Pide un límite al usuario y muestra la serie de Fibonacci completa hasta esa posición.
    """
    print("\nSerie de Fibonacci Recursiva Simple")
    limite = int(input("Ingrese la posición límite (N) para la serie de Fibonacci: "))
    print(f"\nSerie de Fibonacci hasta la posición {limite}")
    serie = []
    
    # Recorrer desde la posición 0 hasta la posición límite (incluida)
    for i in range(limite + 1):
        # Llama a la función recursiva
        valor = fibonacci_recursivo(i)
        serie.append(valor)
        
    # Mostrar la serie completa
    print("Posición | Valor")
    print("-" * 15)
    for i, valor in enumerate(serie):
        print(f"{i} | {valor}")

    print(f"\n✅ El valor en la posición {limite} es {fibonacci_recursivo(limite)}.")


# --- Ejecución del Programa ---
mostrar_serie_fibonacci()