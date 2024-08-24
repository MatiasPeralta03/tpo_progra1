# Escribir una función que reciba una lista como parámetro y devuelva True si 
# la lista está ordenada en forma ascendente o False en caso contrario. Por 
# ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna 
# False. Desarrollar además un programa para verificar el comportamiento de 
# la función.

def lista_ordenanda_asc(lst):
    asc = True
    index = 0
    while asc == True and index != (len(lst) - 1):
        if lst[index] > lst[index + 1]:
            asc = False
        index = index + 1
    return asc

lista = ['a','b','c'] # True

print(lista_ordenanda_asc(lista))

lista = [1,2,3,4,5] # True