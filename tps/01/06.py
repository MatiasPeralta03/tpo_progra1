# Desarrollar una función que reciba como parámetros dos números enteros positivos 
# y devuelva como valor de retorno el número que resulte de concatenar ambos 
# parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite 
# utilizar facilidades de Python no vistas en clase.

def concatenarNumeros(num1, num2):
    # Determinar el número de dígitos de num2
    num_digitos = 0
    temp = num2
    while temp > 0:
        temp //= 10
        num_digitos += 1
    
    # Desplazar num1 a la izquierda el número de dígitos de num2
    resultado = num1 * (10 ** num_digitos) + num2
    return resultado

num1 = int(input("Ingrese el primer numero: ")) 

while num1 <= 0:
    num1 = int(input("Ingrese un numero valido mayor a 0: "))

num2 = int(input("Ingrese el segundo numero: ")) 

while num2 <= 0:
    num2 = int(input("Ingrese un numero valido mayor a 0: "))

print(concatenarNumeros(num1, num2))

