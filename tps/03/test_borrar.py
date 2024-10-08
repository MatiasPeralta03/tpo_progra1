matriz = [[1, 2, 3], [2, 1, 3], [3, 3, 1]]

def transponer_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

#t_matriz = transponer_matriz(matriz)

t_matriz = [[1, 2, 3], [3, 1, 3], [3, 3, 1]]

print(t_matriz)

def detectar_simetria(mtx_t, mtx):
    flag = True
    i = 0 
    while i < (len(mtx)) and flag:
        j = 0
        while j < (len(mtx)) and flag:
            if mtx[i][j] != mtx_t[i][j]:
                flag = False
            print(mtx_t[i][j])
            j += 1
        i += 1
    return flag

if detectar_simetria(t_matriz, matriz):
    print("SImetricas")