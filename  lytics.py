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
