#Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
#ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun-
#ción:
#a. Cargar  números  enteros  en  una  matriz  de  N  x  N,  ingresando  los  datos  
# desde teclado. 
#b. Ordenar en forma ascendente cada una de las filas de la matriz.
#c. Intercambiar dos filas, cuyos números se reciben como parámetro.
#d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
#e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
#f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
#parámetro.
#g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-
#mero se recibe como parámetro.
#h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
#i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
#j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
#una lista con los números de las mismas.
#NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
#sea el valor ingresado.

#a. Cargar  números  enteros  en  una  matriz  de  N  x  N,  ingresando  los  datos  
# desde teclado. 

n = int(input("Ingrese el valor de n tal que la matriz a formarse sea N x N: "))

while n < 1:
    n = int(input("Ingrese el valor mayor igual a 1 para n tal que la matriz a formarse sea N x N: "))

matriz = []
lst_aux = []

for i in range(n):
    for j in range(n):
        lst_aux.append(int(input(f"Ingrese el valor para la posicion {i} {j}: ")))
    matriz.append(lst_aux)
    lst_aux = []

print("Matriz:")
for fila in matriz:
    print(fila)

#b. Ordenar en forma ascendente cada una de las filas de la matriz.

#Burbujeo ascendente
def ord_bubble_asc(lst):
    for _ in range(0, len(lst)):
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                aux = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = aux

    return lst

for i in range(len(matriz)):
    matriz[i] = ord_bubble_asc(matriz[i])

print("Matriz con filas ordenadas:")
for fila in matriz:
    print(fila)

#c. Intercambiar dos filas, cuyos números se reciben como parámetro.

num1 = int(input("Ingrese el indice de la primera row a intercambiar: "))

while num1 < 0 or len(matriz) < num1:
    num1 = int(input("Ingrese un valor mayor igual a 0 y en el rango de la matriz: "))


num2 = int(input("Ingrese el indice de la segunda row a intercambiar: "))

while num2 < 0 or len(matriz) < num2:
    num2 = int(input("Ingrese un valor mayor igual a 0 y en el rango de la matriz: "))

matriz[num1],matriz[num2] = matriz[num2],matriz[num1]

print("Matriz con filas cambiadas:")
for fila in matriz:
    print(fila)

#d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.

num1 = int(input("Ingrese el indice de la primera columna a intercambiar: "))

while num1 < 0 or len(matriz) < num1:
    num1 = int(input("Ingrese un valor mayor igual a 0 y en el rango de la matriz: "))


num2 = int(input("Ingrese el indice de la segunda columna a intercambiar: "))

while num2 < 0 or len(matriz) < num2:
    num2 = int(input("Ingrese un valor mayor igual a 0 y en el rango de la matriz: "))

for i in range(len(matriz)):
    matriz[i][num1],matriz[i][num2] = matriz[i][num2],matriz[i][num1]

print("Matriz con columnas cambiadas:")
for fila in matriz:
    print(fila)

#e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)

def transponer_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

print("Matriz original:")
for fila in matriz:
    print(fila)

transponer_matriz(matriz)

print("\nMatriz transpuesta:")
for fila in matriz:
    print(fila)

#f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
#parámetro.

def promedio_lista_en_matriz(matriz, fila):
    prom = 0
    for value in matriz[fila]:
        prom += value
    return prom / len(matriz[fila])

num = int(input("Ingrese el indice de fila para calcular su promedio: "))

while num < 0 or len(matriz) < num:
    num = int(input("Ingrese un valor mayor igual a 0 y en el rango de las filas de la matriz: "))

print(f"El promedio de la fila {num} es de {promedio_lista_en_matriz(matriz, num)}.")

#g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.

num = int(input("Ingrese el indice de columna para calcular su promedio de valores impares: "))

while num < 0 or len(matriz) < num:
    num = int(input("Ingrese un valor mayor igual a 0 y en el rango de las filas de la matriz: "))

def promedio_columna_impar_en_matriz(matriz, columna):
    prom = 0
    for i in range(len(matriz)):
        if matriz[i][columna] % 2 != 0:
            prom += matriz[i][columna]
    return prom / len(matriz[i])

print(f"El promedio de la columna {num} es de {promedio_columna_impar_en_matriz(matriz, num)}.")
