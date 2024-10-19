import lytics

matriz = [
    [1,	"María", "Pér4ez", "MM", 71],
    [2,	"Luis", "García", "F", 19],
    [],
    [2,	"", "Rodríguez","M", 81],
    [4,	"Carlos", "Martínez","H", 25],
    [4,	"Carlos", "Martínez","H", 25],
    [5,	"Laura", "Fernández","M", 68],
    [1,	"María", "Pér4ez", "MM", 71],
    []
]

print(f"La matriz sin vacios es: ")
for value in lytics.mtx_empty_spaces(matriz):
    print(value)

print(f"La matriz sin duplicados es: ")
for value in lytics.mtx_remove_duplicates(matriz):
    print(value)

print(f"La matriz reestructurada es: ")
for value in lytics.mtx_id_check(matriz):
    print(value)
