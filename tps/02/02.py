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

num = int(input("Ingrese el valor de numeros que desea en la lista: "))

print("Lista:", generar_lista_random(num))

