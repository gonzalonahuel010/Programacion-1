""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario """

def calcular_factorial_recursivo(n):
    # Caso Base: n = 0
    if n == 0:
        return 1
    
    # Paso Recursivo: n * factorial(n-1)
    else:
        return n * calcular_factorial_recursivo(n - 1)

def mostrar_factoriales_hasta_n():
    print("\nCalculadora de Factoriales Recursivos Simple")
    
    limite = int(input("Ingrese un número entero positivo (N) para calcular factoriales hasta N: "))
            
    print(f"\nFactoriales desde 1 hasta {limite}")
    
    # Bucle para calcular y mostrar el factorial de cada número
    # Se itera desde 1 hasta 'limite' (incluido)
    for i in range(1, limite + 1):
        resultado = calcular_factorial_recursivo(i)
        print(f"Factorial de {i}! = **{resultado}**")

# Ejecución del Programa 
mostrar_factoriales_hasta_n()

""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. """

def fibonacci_recursivo(pos):
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
    print("\nSerie de Fibonacci Recursiva Simple")
    limite = int(input("Ingrese la posición límite (N) para la serie de Fibonacci: "))
    print(f"\nSerie de Fibonacci hasta la posición {limite}")
    serie = []
    
    # Recorremos desde la posición 0 hasta la posición límite (incluida)
    for i in range(limite + 1):
        # Llama a la función recursiva
        valor = fibonacci_recursivo(i)
        serie.append(valor)
        
    # Mostramos la serie completa
    print("Posición | Valor")
    print("-" * 15)
    for i, valor in enumerate(serie):
        print(f"{i} | {valor}")

    print(f"\n✅ El valor en la posición {limite} es {fibonacci_recursivo(limite)}.")


# Ejecución del Programa
mostrar_serie_fibonacci()

""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
algoritmo general. """

def calcular_potencia_recursiva(base, exponente):
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

""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto. """

def decimal_a_binario_recursivo(n):
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

""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed(). """

def es_palindromo(palabra):
  # Caso Base 1: Si la palabra tiene 0 o 1 carácter, es un palíndromo.
  # Por ejemplo, "", "a"
  if len(palabra) <= 1:
    return True

  # Caso Base 2:
  # Si el primer carácter es diferente del último, NO es un palíndromo.
  if palabra[0] != palabra[-1]:
    return False
  
  # Si los caracteres de los extremos son iguales, hacemos la llamada recursiva
  # con la subcadena que excluye el primer y el último carácter.
  return es_palindromo(palabra[1:-1])

""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5) """

def suma_digitos(n):
  # Caso Base: Si el número es menor a 10, la suma es el número mismo.
  if n < 10:
    return n

  # 1. Obtenemos el ultimo dígito: n % 10 
  ultimo_digito = n % 10

  # 2. Obtenemos el número restante (sin el último dígito)
  resto_del_numero = n // 10

  # 3. La suma es el último dígito + la suma de los dígitos del resto.
  return ultimo_digito + suma_digitos(resto_del_numero)

""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide. """

def contar_bloques(n):
  # Caso Base: Si el nivel inferior es 0, no se necesitan más bloques.
  if n <= 0:
    return 0

  # El total es el número de bloques en el nivel actual (n) más el resultado de contar 
  # los bloques de la pirámide más pequeña que comienza con (n - 1) bloques.
  return n + contar_bloques(n - 1)

""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número. """

def contar_digito(numero, digito):
  # Caso Base: Cuando el 'numero' se ha reducido a 0, significa que 
  # no quedan más dígitos por revisar.
  if numero == 0:
    return 0
  
  # 1. Obtener el último dígito del número
  ultimo_digito = numero % 10

  # 2. Inicializar el contador a 1 si hay una coincidencia, o a 0 si no la hay
  contador_actual = 1 if ultimo_digito == digito else 0

  # 3. Sumar el contador actual al resultado de la llamada recursiva
  return contador_actual + contar_digito(numero // 10, digito)