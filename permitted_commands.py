import random

lst1=[1,2,3,4]

print(lst1) # [1,2,3,4]

print(*lst1) # 1 2 3 4

lst2 = [5,6,7,8]

lst3 = lst1 + lst2

print(lst3) # [1,2,3,4,5,6,7,8]

lst4 = [0] * 5

print(lst4) # [0,0,0,0,0]

print(sum(lst1)) # 10

print("El primer valor de la lst1 es %d y el de la lst2 es %d."%(lst1[0], lst2[0]), end="   ")

print(max(lst1)) # 4
print(min(lst1)) # 1

lst5 = list(range(5)) #[0, 1, 2, 3, 4]

# Uso de in y not in

#Uso de insert(<pos>, <elem>), pop(<pos>), remove(<elem>), index(<elem>), count(<elem>), clear(), reverse(), sort(reverse=<True or False>)

#Sort
lista = [1, 2, 3, 4, 5, 6]
lista.sort(key=lambda x: x%2)
print(lista) # [2, 4, 6, 1, 3, 5]

nombres = ["Andrés", "Ariel", "Juan"]
nombres.sort(key=lambda x: x[-1])
print(nombres) # ["Ariel", "Juan", "Andrés"]

nombres = ["Andrés", "Ariel", "Juan"]
nombres.sort(key=len)
print(nombres) # ["Juan", "Ariel", "Andrés"]

numeros = [3, -2, 4, -1]
numeros.sort(key=abs)
print(numeros) # [-1, -2, 3, 4]

numeros = [9, 6, 7, 8, 1, 5, 4]
numeros.sort(key=lambda x:[x%2, x])
print(numeros)# [4, 6, 8, 1, 5, 7, 9]


#Sorted
numeros = [9, 6, 7, 8, 1, 5, 4]
ordenada = sorted(numeros)
print(ordenada)# [1, 4, 5, 6, 7, 8, 9]

#Random
#random.random(): # Devuelve un número realal azar dentro del intervalo [0, 1)

#random.randint(<min>, <max>)

opciones = ["Piedra", "Papel", "Tijera"]
situacion= random.choice(opciones)

lista = [3, 4, 5, 6]
random.shuffle(lista)
print(lista) # por ejemplo [6, 4, 5, 3]

