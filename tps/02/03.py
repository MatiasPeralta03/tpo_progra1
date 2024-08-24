# Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
# donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 
# 10 valores de la lista.

def generar_cuadrados(lenght):
    lst = []
    for i in range(1, lenght + 1):
        lst.append(i*i)
    return lst

num = int(input("Ingrese el valor hasta donde quiera calcular el cuadrado del mismo: "))

lista = generar_cuadrados(num)
print("Ultimos 10 valor de la lista: ", lista[-10:]) #Preguntar si es valido


