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

sublista_invertida = lista[::-1]

lista[2:2] = [3,2]
print(lista) #Inserta 3,2 en la posicion 2

[2,3] > [1,4] #True
[2,3] > [2,4] #False
[2,4,6] > [1,4] #True

id(lista) #Indica el lugar en memoria

#Copiar listas en varios metodos
lista1 = [1,2,3]
lista2 = lista1[:]
lista2.append(4)

lista1 = [1,2,3]
lista2 = list(lista1)
lista2.append(4)

lista1 = [1,2,3]
lista2 = lista1 + []
lista2.append(4)

lista1 = [1,2,3]
lista2 = lista1.copy()
lista2.append(4)

#For
for value in lista1:
    print(value) # 1 2 3

for value in lista1[0:2]:
    print(value) # 1 2

#Enumerate()
#for i, letra in enumerate(lista):

numeros = [1,2,3,4]
lista_raices = list(map(lambda x:x**(1/2),numeros))
print(lista_raices) # 1.0, 1.4142135623730951, 1.7320508075688772, 2.0

#Filter acepta funciones True or False
lista_raices = list(filter(lambda x:x%2!=0,numeros))
print(lista_raices) #Solo valores impares

#Map devuelve una lista del mismo largo que la original pero con valores modificados
#Filter devuelve una lista con el mismo largo o mas corta pero con valores originales

#Conjuntos por extension
#Dias de la semana: Se debe definir cada valor o posibilidades dentro del conjunto

#Conjuntos por comprension
#X tal que X

cuadrados = [x**2 for x in range(6)] 

cubospares = [i**3 for i in range(11) if i**3 % 2 == 0] #Cubos pares desde el 0 hasta el 5to

#Creacion de matrices estatica. Cuando ya sabemos cuantas filas y columnas vamos a usar
matriz = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

#Creacion de matrices dinamica
#Alternativa A
filas = 3
columnas = 4
matriz = []
for f in range(filas):
    fila = []
    for c in range(columnas):
        fila.append(0)
    matriz.append(fila)

#Alternativa B
filas = 3
columnas = 4
matriz = []
for f in range(filas):
    matriz.append([0] * columnas)

#Alternativa C
filas = 3
columnas = 4
matriz = [[0] * columnas for i in range(filas)]

#Alternativa D
filas = 3
columnas = 4
matriz = [[0 for c in range(columnas)] for f in range(filas)]


#Grafico de barras
votos = [ ]
n = int(input("Votos del candidato? (-1 para terminar): "))
while n != -1:
votos = votos + [n] # votos.append(n) sería similar
n = int(input("Votos del candidato? (-1 para terminar) "))
print( )
# Calcular porcentajes e imprimir listado final
total = sum(votos)
for i in range(len(votos)):
porcentaje = votos[i] * 100 / total
print("▪ Candidato %d: %d votos (%.2f%%)"
%(i, votos[i], porcentaje), end=" ")
# Imprimir el gráfico de barras
for j in range(int(porcentaje/10)):
print("*", end="")
print( )

##Clase 7 Tuplas

#Usamos tuples para valores que no se busca que cambien

#Conjuntos

#No se les pueden agregar datos MUTABLES












