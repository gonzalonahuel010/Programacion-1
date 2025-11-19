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