import lytics
matriz = [[1, 2, 3], [2, 1, 3], [3, 3, 1], [1, 2, 3], [1, 2, 2]]

print(f"Matriz sin vacios: {lytics.mtx_remove_duplicates(matriz)}")
matriz_res = lytics.mtx_id_check(matriz)

print(f"La matriz reestructurada es: ")
for value in matriz_res:
    print(value)
