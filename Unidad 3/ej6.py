""" 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria. """

import random, statistics
numeros_aleatorios = [random.randint(1, 100) for i in range(10)]
sesgo_positivo = False
sesgo_negativo = False
sin_sesgo = False
media= statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    sesgo_positivo = True
    if sesgo_positivo:
        print("Sesgo positivo: ",media)
elif media <  mediana and mediana < moda:
    sesgo_negativo = True
    if sesgo_negativo:
        print("Sesgo negativo: ", mediana)
else:
    sin_sesgo = True
    if(sin_sesgo):
        print("Sin sesgo: ",moda)
