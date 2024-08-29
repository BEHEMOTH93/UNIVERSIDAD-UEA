# Matriz 3x3
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de la ordenación
print("\nMatriz después de ordenar la fila 2:")
for fila in matriz:
    print(fila)
