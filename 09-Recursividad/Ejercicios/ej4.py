""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto. """

def decimal_a_binario_recursivo(n):
    """
    Convierte un número entero positivo (n) de base decimal a binario (cadena de texto) 
    utilizando recursión.

    La conversión se basa en la división sucesiva por 2.
    """
    # 1. Caso Base: Si el número es 0 o 1, el binario es el número mismo.
    if n <= 1:
        return str(n)
    
    # 2. Paso Recursivo: 
    #   a) Llama recursivamente con el cociente (n // 2).
    #   b) Concatena el resto (n % 2) al final (bit menos significativo).
    else:
        cociente_binario = decimal_a_binario_recursivo(n // 2)
        resto = str(n % 2)
        
        # El orden es importante: Cociente (bits de la izquierda) + Resto (bit de la derecha)
        return cociente_binario + resto

def probar_conversion_binaria():
    """
    Algoritmo general para pedir un número al usuario y probar la función binaria.
    """
    print("\nConversor Decimal a Binario Recursivo Simple")
    
    # Se asume que el usuario ingresa un número entero positivo. 
    num_decimal = int(input("Ingrese un número entero positivo en decimal: "))
    
    if num_decimal < 0:
        print("Error: Se esperaba un número entero positivo. El programa se detiene.")
        return

    # Llama a la función recursiva
    resultado_binario = decimal_a_binario_recursivo(num_decimal)
    
    # Muestra el resultado
    print(f"\nEl número decimal {num_decimal} en binario es: **{resultado_binario}**")

# Ejecución del Algoritmo
probar_conversion_binaria()