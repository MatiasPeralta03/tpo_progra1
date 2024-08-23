# Desarrollar una función que reciba tres números enteros positivos y devuelva el mayor 
# de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en caso 
# de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar también 
# un programa para ingresar los tres valores, invocar a la función y mostrar el máximo 
# hallado, o un mensaje informativo si éste no existe.

def valorMayor(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
    elif num2 > num3:
        if num2 > num3:
            return num2
    elif num3 > num1:
        if num3 > num2:
            return num3
    return -1 

num1 = int(input("Ingrese el valor para el primer numero positivo: "))

while num1 <= 0:
    num1 = int(input("Ingrese el valor para el primer numero positivo valido mayor a 0: "))

num2 = int(input("Ingrese el valor para el segundo numero positivo: "))

while num2 <= 0:
    num2 = int(input("Ingrese el valor para el segundo numero positivo valido mayor a 0: "))

num3 = int(input("Ingrese el valor para el tercer numero positivo: "))

while num3 <= 0:
    num3 = int(input("Ingrese el valor para el tercer numero positivo valido mayor a 0: "))

mayor = valorMayor(num1, num2, num3)

if mayor != -1:
    print("El mayor valor estricto es:", mayor)
else:
    print("No existe un mayor estricto.")