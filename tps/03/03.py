#Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
#azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
#Imprimir la matriz por pantalla.
import random

def get_random_not_in_list(num, exclude_list):
    random_num = random.randint(0, num**2 - 1)  # Adjust the range to [0, num^2)

    while random_num in exclude_list:
        random_num = random.randint(0, num**2 - 1)
    
    return random_num


num = int(input("Ingrese el valor para N tal que N x N forme una matriz con valores al azar sin repetir entre [0,N^2): "))

while num < 1:
    num = int(input("Ingrese un valor valido positivo mayor o igual que 1: "))

matriz = [[0]*num for i in range(num)]

exclude_list = []

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = get_random_not_in_list(num,exclude_list)
        exclude_list.append(matriz[i][j])
        print(exclude_list)

print("Matriz con numeros random: ")
for fila in matriz:
    for elem in fila:
        print("%3d" %elem, end="")
    print()