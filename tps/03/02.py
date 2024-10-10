#Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio-
#nes que generen cada una de ellas sin intervención humana y escribir un programa 
#que  las  invoque  e  imprima  por  pantalla.  El  tamaño  de  las  matrices  debe  estable-
#cerse como N x N, donde N se ingresa a través del teclado.
#a: 1 0 0 0     b: 0 0 0 27    c: 4 0 0 0
#   0 3 0 0        0 0 9 0        3 3 0 0
#   0 0 5 0        0 3 0 0        2 2 2 0
#   0 0 0 7        1 0 0 0        1 1 1 1

#d: 8 8 8 8     e: 0 1 0 2     f: 0  0 0 1
#   4 4 4 4        3 0 4 0        0  0 3 2
#   2 2 2 2        0 5 0 6        0  6 5 4
#   1 1 1 1        7 0 8 0        10 9 8 7

#g: 1  2  3  4  h: 1  2  4  7  i: 1  2  6  7
#   12 13 14 5     3  5  8  11    3  5  8  13
#   11 16 15 6     6  9  12 14    4  9  12 14
#   10 9  8  7     10 13 15 16    10 11 15 16

def generarPatronA(mat):
    for i in range(len(mat)):
        mat[i][i] = 2*i+1
    return mat

def generarPatronB(mat):
    for i in range(len(mat)-1, -1, -1):
        mat[len(mat)-i-1][i] = 3**i
    return mat

def generarPatronC(mat):
    n=0
    for i in range(len(mat)-1, -1, -1):
        for j in range(len(mat)-n):
            mat[i][j] = len(mat)-i
        n+=1
    return mat

def generarPatronD(mat):
    for i in range(len(mat)-1, -1, -1):
        for j in range(len(mat)):
            mat[i][j] = 2**(len(mat)-i-1)
    return mat

def generarPatronE(mat):
    n=1
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (i + j) % 2 == 1:
                mat[i][j]= n
                n+=1
    return mat

def generarPatronF(mat):
    n=len(mat) - 2
    cont = 1
    for i in range(0, len(mat)):
        for j in range(len(mat)- 1, n, -1):
            print(f"Posicion {i} - {j}")
            if (i + j) % 2 == 1:
                mat[i][j]= cont
                n+=1
        n-=1

#    #ChatGPT version
#    n = len(mat) - 1  # Start with the full width of the matrix
#    cont = 1  # Start counting from 1
#
#    for i in range(len(mat)):
#        for j in range(n, i - 1, -1):  # Start from n, go down to i
#            mat[i][j] = cont
#            cont += 1
#        n -= 1  # Decrease the width for the next row

    return mat

#Programa principal
#matriz = [[0]*4 for i in range(4)]

print("Patron A")
for fila in generarPatronA([[0]*4 for i in range(4)]):
    for elem in fila:
        print("%3d" %elem, end="")
    print()

print("Patron B")
for fila in generarPatronB([[0]*4 for i in range(4)]):
    for elem in fila:
        print("%3d" %elem, end="")
    print()

print("Patron C")
for fila in generarPatronC([[0]*4 for i in range(4)]):
    for elem in fila:
        print("%3d" %elem, end="")
    print()

print("Patron D")
for fila in generarPatronD([[0]*4 for i in range(4)]):
    for elem in fila:
        print("%3d" %elem, end="")
    print()

print("Patron E")
for fila in generarPatronE([[0]*4 for i in range(4)]):
    for elem in fila:
        print("%3d" %elem, end="")
    print()

print("Patron F")
for fila in generarPatronF([[0]*4 for i in range(4)]):
    for elem in fila:
        print("%3d" %elem, end="")
    print()
    



