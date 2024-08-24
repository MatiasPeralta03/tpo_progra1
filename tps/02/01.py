# Desarrollar cada una de las siguientes funciones y escribir un programa 
# que per-mita verificar su funcionamiento imprimiendo la lista luego de 
# invocar a cada fun-ción:
# a.Cargar una lista con números al azar de cuatro dígitos. La cantidad de 
# elemen-tos también será un número al azar de dos dígitos.

# b.Calcular y devolver el producto de todos los elementos de la lista 
# anterior. 

# c.Eliminar todas las apariciones de un valor en la lista anterior. El 
# valor a eliminar se ingresa desde el teclado y la función lo recibe 
# como parámetro. No utilizar listas auxiliares.

# d.Determinar si el contenido de una lista cualquiera es capicúa, sin usar 
# listas auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

import random as rd

def generar_lista_random():
    lst=[]
    for _ in range(rd.randint(10,99)):
        lst.append(rd.randint(1000,9999))
    return lst

def producto_lista(lst):
    aux = 1
    for i in range(len(lst)):
        aux = aux * lst[i]
    return aux

def eliminar_num_en_lista(lst,num):
    while num in lst:
        lst.remove(num)
    return lst

def lista_capicua(lst):
    capicua = False
    count = 0
    index = 0
    inv = -1
    while index != (len(lst) - 1) and lst[index] == lst[inv]:
        index = index + 1
        inv = inv - 1
        count = count + 1
    if count == len(lst) - 1:
        capicua = True
    # Otra manera es trabajar con inverse() ocupando una lista auxiliar
    return capicua
    

lista = generar_lista_random()

print(lista)

print("Producto de lista es: %d" %(producto_lista(lista)))

num = int(input("Ingresar el numero a eliminar de la lista: "))

eliminar_num_en_lista(lista,num)

if lista_capicua(lista):
    print("La lista es capicua.")
else:
    print("La lista no es capicua.")



