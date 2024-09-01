# Matriz bidimensional 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor específico en la matriz
def buscar_en_matriz(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return (fila, columna)
    return None

# Definir el valor a buscar
valor_buscado = 60

# Llamar a la función para buscar el valor
posicion = buscar_en_matriz(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"Valor {valor_buscado} encontrado en la posición: fila {posicion[0]}, columna {posicion[1]}.")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz.")
