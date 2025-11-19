""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
algoritmo general. """

def calcular_potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.
    Fórmula utilizada: n^m = n * n^(m-1)
    """
    # Manejar exponentes negativos (Conversión a 1 / n^(-m))
    if exponente < 0:
        # Usa el recíproco y convierte el exponente a positivo.
        return 1 / calcular_potencia_recursiva(base, -exponente)
    
    # 1. Caso Base: n^0 = 1
    if exponente == 0:
        return 1
    
    # 2. Paso Recursivo: n^m = n * n^(m-1)
    else:
        return base * calcular_potencia_recursiva(base, exponente - 1)

def probar_potencia_recursiva():
    """
    Algoritmo general para pedir la base y el exponente al usuario y probar la función.
    """
    print("\nCalculadora de Potencia Recursiva Simple")
    base = float(input("Ingrese el número base (n): "))
    exponente = int(input("Ingrese el exponente (m): "))
    
    # Excluir el caso especial 0^-n que resulta en una división por cero (si base es 0)
    if base == 0 and exponente < 0:
        print("Error: No se puede calcular 0 elevado a un exponente negativo.")
        return

    # Llama a la función recursiva
    resultado = calcular_potencia_recursiva(base, exponente)
    
    # Muestra el resultado
    print(f"\n✅ Resultado: {base} elevado a la {exponente} es **{resultado}**")
        
# Ejecución del Algoritmo
probar_potencia_recursiva()