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