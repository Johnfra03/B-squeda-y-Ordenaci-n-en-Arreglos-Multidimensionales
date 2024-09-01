# Matriz bidimensional 3x3
matriz = [
    [25, 17, 31],
    [44, 20, 15],
    [18, 30, 27]
]

# Función de QuickSort para ordenar una fila específica
def quicksort_fila(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quicksort_fila(menores) + [pivote] + quicksort_fila(mayores)

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definir la fila a ordenar (por ejemplo, la fila 2 que es la tercera fila)
fila_a_ordenar = 2

# Ordenar la fila especificada utilizando QuickSort
matriz[fila_a_ordenar] = quicksort_fila(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
