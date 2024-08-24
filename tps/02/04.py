# Eliminar de una lista de números enteros aquellos valores que se encuentren 
# en una segunda lista. Imprimir la lista original, la lista de valores a 
# eliminar y la lista resultante. La función debe modificar la lista original
# sin crear una copia modificada.
import random as rd

def generar_lista_random(lenght):
    lst=[]
    for _ in range(lenght):
        lst.append(rd.randint(1,100))
    return lst

def eliminar_valores_en_lista(lst_ori,lst_val):
    for i in lst_val:
        while i in lst_ori:
            lst_ori.remove(i)
    return lst_ori
            
lista_original = generar_lista_random(10)

print("Lista de 10 valores generada:", lista_original)

lista_valores_elim = [10,20,30,40,50,60,70,80,90]

print("Lista con valores a eliminar:", lista_valores_elim)

print("Lista resultante:", eliminar_valores_en_lista(lista_original,lista_valores_elim))


