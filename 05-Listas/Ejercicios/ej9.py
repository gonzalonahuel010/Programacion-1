""" 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada """

tablero = [["-" for _ in range(3)] for _ in range(3)]

for turno in range(6):
    jugador = 'x' if turno % 2 == 0 else 'o'
    for fila in tablero:
        print(" ".join(fila))
    print()
    fila = int(input(f"{jugador} ingrese la fila (0-2): "))
    columna = int(input(f"{jugador} ingrese la columna (0-2): "))

    if tablero [fila][columna] == '-':
        tablero [fila][columna] = jugador
    else: 
        ocupado = True
        print("casilla ocupada, vuelve a probar otra")
        while ocupado:
            fila = int(input(f"{jugador} ingrese la fila (0-2): "))
            columna = int(input(f"{jugador} ingrese la columna (0-2): "))
            if tablero [fila][columna] == '-':
                tablero [fila][columna] = jugador
                ocupado = False
            else:   
                print("esta casilla tambien esta ocupada, vuelve a probar otra")
print("Estado final del tablero:")
for i, fila in enumerate(tablero):
    print(f"{i} | " + " ".join(fila))
print("   0 1 2")
print("¡Fin del juego!")


