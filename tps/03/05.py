#Desarrollar  un  programa  que  permita  realizar  reservas  en  una  sala  de  cine  de  N 
#filas con M butacas  por  cada fila. Desarrollar   las  siguientes  funciones  y utilizarlas 
#en un mismo programa:
#mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas 
#del cine. Esta función deberá ser invocada antes de que se realice la reserva, y 
#se volverá a invocar luego de la misma con los estados actualizados.
#reservar:  Deberá  recibir  una  matriz  y  la  butaca  seleccionada,  y  actualizará  la 
#sala en caso de estar disponible dicha butaca. La función devolverá True/False 
#si logró o no reservar la butaca.
#cargar_sala: Recibirá una matriz como parámetro y la cargará con valores 
#aleatorios para simular una sala con butacas ya reservadas.
#butacas_libres: Recibirá como parámetro la matriz y  retornará cuántas buta-
#cas desocupadas hay en la sala.
#butacas_contiguas:  Buscará  la  secuencia  más  larga  de  butacas  libres  conti-
#guas en una misma fila y devolverá las coordenadas de inicio de la misma.
import random

n = int(input("Ingrese el valor para N tal que representa la cantidad de filas: "))

while n < 1:
    n = int(input("Ingrese un valor valido positivo mayor o igual que 1: "))

m = int(input("Ingrese el valor para M tal que representa la cantidad de butacas por fila: "))

while m < 1:
    m = int(input("Ingrese un valor valido positivo mayor o igual que 1: "))

matriz_cine = [["O"]*m for i in range(n)]

def mostrar_butacas(mtx):
    print()
    print(' Pantalla '.center(len(mtx[0])*2 - 1, '*'))
    print()
    for fila in mtx:
        for elem in fila:
            print(elem, end=" ")
        print()
    print()

def reservar(but,mtx):
    occupied = True
    if mtx[but[0]][but[1]] == "O":
        mtx[but[0]][but[1]] = "X"
        occupied = False
    return occupied

def cargar_sala(mtx):
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            mtx[i][j] = random.choice(["X", "O"])

def butacas_libres(mtx):
    cont = 0
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            if mtx[i][j] == "O":
                cont += 1
    return cont

#def butacas_contiguas(mtx):
#pensar

def menu():
    num = 0
    flag = False
    while not flag:
        num  = int(input("1.Mostrar butacas\n2.Reservar\n3.Cargar sala\n4.Ver butacas libres\n5.Salir\n\nSeleccione una opcion: "))
        if num == 1:
            mostrar_butacas(matriz_cine)
        elif num == 2:
            fila = int(input(f"Ingrese el valor de la fila a reservar (1 - {len(matriz_cine)}): "))

            while fila < 1 or len(matriz_cine) < fila:
                fila = int(input(f"Ingrese un valor valido entre 1 y {len(matriz_cine)}: "))

            but = int(input(f"Ingrese el valor de la butaca a reservar (1 - {len(matriz_cine[0])}): "))

            while but < 1 or len(matriz_cine[0]) < but:
                but = int(input(f"Ingrese un valor valido entre 1 y {len(matriz_cine[0])}: "))
            if reservar([fila - 1,but - 1], matriz_cine):
                print("Butaca ocupada.")
            else:
                print("Butaca reservada satisfactoriamente.")
        elif num == 3:
            cargar_sala(matriz_cine)
        elif num == 4:
            print(f"Butaca libre: {butacas_libres(matriz_cine)}.")
        elif num == 5:
            flag = True
        else:
            print('')
            print("-" * 80)
            print("--ERROR--".center(80))
            print("Vuelva a ingresar un número dentro del rango o 15 para salir".center(80))
            print("-" * 80)
            print('')
        
print('')
print("-" * 80)
print(("Bienvenido al cine").center(80))
print("-" * 80)

menu()

print('')
print("-" * 80)
print("Saliendo...".center(80))
print("Gracias por usar nuestro sistema.".center(80))
print("-" * 80)
print('')
