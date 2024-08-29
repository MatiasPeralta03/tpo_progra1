#Generar  e  imprimir  una  lista  por  comprensión  entre  A  y  B  con  los  múltiplos  de  7 
#que no sean múltiplos de 5. A y B se ingresar desde el teclado.
inicio=int(input("Ingrese un valor: \n"))
fin=int(input("Ingrese un valor: \n"))

lista=[n for n in range(inicio, fin+1) if n%7 == 0 and n%5 != 0]
print(lista)