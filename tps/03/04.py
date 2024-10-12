#Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
#en cada una de sus plantas durante una semana. De este modo, cada columna re-
#presenta el día de la semana y cada fila a una de sus fábricas. Ejemplo:

#             |(Lunes) (Martes) (Miércoles) (Jueves) (Viernes) (Sábado)
#             |   0        1         2          3        4         5
#(Fábrica 1)0 |   23       150       20        120       25       150
#(Fábrica 2)1 |   40       75        80         0        80       35
#( . . . )    |   . . . . . . . . . . . . . . . . . . . . . . . . . . .
#(Fábrica n)3 |   80       80        80         80       80       80

#Se solicita:
#a. Crear una matriz con datos generados al azar para N fábricas durante una 
#semana,  considerando  que  la  capacidad  máxima  de  fabricación  es  de  150 
#unidades  por  día  y  puede  suceder  que  en  ciertos  días  no  se  fabrique ninguna. 
#b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
#c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
#d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
#e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
#por cada fábrica.

import random

num = int(input("Ingrese el valor para N tal que representa la cantidad de fabricas: "))

while num < 1:
    num = int(input("Ingrese un valor valido positivo mayor o igual que 1: "))

matriz = [[0]*6 for i in range(num)]
print(matriz)

for i in range(num):
    for j in range(6):
        matriz[i][j] = random_num = random.randint(0, 150)

print("Matriz de produccion de bicicletas ")
for fila in matriz:
    for elem in fila:
        print("%3d" %elem, end="  ")
    print()

maximo = 0
for i in range(len(matriz)):
    if maximo < max(matriz[i]):
        maximo = max(matriz[i])
        fabrica = i
        dia = matriz[i].index(maximo)

print(f"El maximo fue de {maximo} el dia {dia + 1} en la fabrica {fabrica + 1}.")

cont = 0
lst_prod = []
for i in range(len(matriz)):
    for j in range(6):
        cont += matriz[i][j]
    lst_prod.append(cont)
    cont = 0

print(f"El dia mas productivo fue el {lst_prod.index(max(lst_prod)) + 1} con una cantidad de {max(lst_prod)} bicicletas fabricadas.")   
    
# e. Lista por comprensión con la menor cantidad fabricada por cada fábrica
menores_por_fabrica = [min(fabrica) for fabrica in matriz]

print("Menor cantidad fabricada por cada fábrica:")
for i, menor in enumerate(menores_por_fabrica):
    print(f"Fábrica {i + 1}: {menor} unidades")
