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