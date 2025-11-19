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
  """
  Calcula la suma de los dígitos de un número entero positivo 'n'
  utilizando recursión y operaciones matemáticas.
  """
  # Caso Base: Si el número es menor a 10, la suma es el número mismo.
  if n < 10:
    return n

  # 1. Obtenemos el ultimo dígito: n % 10 
  ultimo_digito = n % 10

  # 2. Obtenemos el número restante (sin el último dígito)
  resto_del_numero = n // 10

  # 3. La suma es el último dígito + la suma de los dígitos del resto.
  return ultimo_digito + suma_digitos(resto_del_numero)