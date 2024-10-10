import csv

#Abre el archivo CSV en modo lectura
def doc_to_matrix(doc_name):
    with open(doc_name) as file:
        #Se crea el lector CSV
        reader = csv.reader(file)

        #Creamos una lista para almacenar las filas no vacias
        matrix = []
        
        # Iteramos sobre cada fila en el archivo
        for row in reader:
            matrix.append(row)

    return matrix

def mtx_empty_spaces(mtx):
    for lst in mtx:
        if not lst:
            mtx.remove(lst)
    return mtx

def mtx_remove_duplicates(mtx):
    i = 0
    while i < len(mtx):
        j = i + 1
        while j < len(mtx):
            # Compare rows i and j
            if mtx[i] == mtx[j]:
                # Remove the duplicate row
                mtx.pop(j) #mtx.remove(mtx[j])
            else:
                j += 1
        i += 1
    return mtx

def mtx_id_restructure(mtx):
    for i in range(len(mtx)):
        mtx[i][0] = i + 1
    return mtx

def mtx_id_check(mtx):
    i = 0
    estructured = True
    while i < len(mtx) and estructured:
        if mtx[i][0] != (mtx[i+1][0] - 1):
            estructured = False
            mtx = mtx_id_restructure(mtx)
        i += 1
    return mtx

#id	producto	                id_categoria	id_marca	stock	precio_unitario
#1	Televisor Smart 50"	        2	            2	        466     $962,453
#2	Taladro Percutor	        3	            3	        716     $476,375
#4	Sofá 3 Plazas	            4	            4	        2	    $833,928
#5	Lavabo Minimalista	        5	            5           475     $624,611
#6	Refrigerador Doble Puerta	1	            6	        826	    $317,508

            
#Matriz sin vacios: [[1, 2, 3], [2, 1, 3], [3, 3, 1], [1, 2, 2], [1, 2, 3]]

