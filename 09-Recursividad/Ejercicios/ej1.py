""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario """

def calcular_factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.
    """
    # Caso Base: n = 0
    if n == 0:
        return 1
    
    # Paso Recursivo: n * factorial(n-1)
    else:
        return n * calcular_factorial_recursivo(n - 1)

def mostrar_factoriales_hasta_n():
    """
    Pide un número al usuario y muestra el factorial de cada entero desde 1 hasta ese número.
    """
    print("\n=== Calculadora de Factoriales Recursivos Simple ===")
    
    limite = int(input("Ingrese un número entero positivo (N) para calcular factoriales hasta N: "))
            
    print(f"\nFactoriales desde 1 hasta {limite}")
    
    # Bucle para calcular y mostrar el factorial de cada número
    # Se itera desde 1 hasta 'limite' (incluido)
    for i in range(1, limite + 1):
        resultado = calcular_factorial_recursivo(i)
        print(f"Factorial de {i}! = **{resultado}**")

# Ejecución del Programa 
mostrar_factoriales_hasta_n()