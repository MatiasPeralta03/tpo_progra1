# Escribir funciones para:
# a.Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa a través del teclado.

# b.Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función 
# no debe modificar la lista.

# c.Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, 
# sin importar el orden. Combinar estas tres funciones en un mismo programa.

import random as rd

def generar_lista_random(lenght):
    lst=[]
    for _ in range(lenght):
        lst.append(rd.randint(1,100))
    return lst

def elemento_repetido(lst):
    rep = False
#    index = 0
#    while rep == False and index != (len(lst) - 1):
#        if lst.count(lst[index]) >= 2:
#            rep = True
#        index = index + 1

#    Otra forma menos optima
    for value in lst:
        if lst.count(value) > 1:
            rep = True
            break
    return rep
             
def depurar_elementos_unicos(lst):
    for value in lst:
        if lst.count(value) >= 2:
            print("Valor %d repetido %d veces" %(value,lst.count(value)))
            while lst.count(value) != 1:
                lst.remove(value)
    return lst

num = int(input("Ingrese el valor de numeros que desea en la lista: "))

lista = generar_lista_random(num)

print("Lista sin depurar:", lista)

if elemento_repetido(lista):
    print("Lista depurada:", depurar_elementos_unicos(lista))
else:
    print("No posee elementos repetidos.")



