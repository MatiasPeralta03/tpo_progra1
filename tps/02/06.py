# Escribir una función que reciba una lista de números enteros como parámetro 
# y la normalice, es decir que todos sus elementos deben sumar 1.0, respetando 
# las proporciones relativas que cada elemento tiene en la lista original. 
# Desarrollar también un programa que permita verificar el comportamiento de 
# la función. Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].

def normalizar_lista(lst):
    total = sum(lst)
    for i in range(len(lst)): 
        lst[i] = (lst[i] / total)
    return lst

lista = [1,1,2]

print("Lista normalizada:",normalizar_lista(lista)) # [0.25, 0.25, 0.5]