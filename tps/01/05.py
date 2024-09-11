# Escribir funciones lambda para:a.Informar si un número es oblongo. Se dice 
# que un número es oblongo cuando se puede obtener multiplicando dos números 
# naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de 
# multiplicar 2 * 3.b.Informar si un número es triangular. Un número se 
# define como triangular si puede expresarse como la suma de un grupo de 
# números naturales consecuti-vos comenzando desde 1. Por ejemplo 10 es un 
# número triangular porque se obtiene sumando 1+2+3+4.Ambas funciones lambda 
# reciben como único parámetro el número a evaluar y de-vuelven True o False. 
# No se permite utilizar ayudas externas a las mismas.

def validarOblongo(num):
    #x = n*(n+1) = n2 + n = x 
    #Si la potencia de n cuadrada
    esOblongo = lambda x:int(x**0.5) * int(x**0,5+1) == x
    #oblongo = False
    #num1 = 1
    #num2 = 2

    #if (num1 * num2) == num:
    #    oblongo = True

    #while (num1 * num2) <= num:
    #    if (num1 * num2) == num:
    #        oblongo = True
    #    num1 = num1 + 1
    #    num2 = num2 + 1
    
    #return oblongo

def validarTriangular(num):
    esTriangular = lambda x:int(x**0.5) * int(x**0,5+1) == x #dividir o multiplicar por 2
    triangular = False
    i = 1
    valor = 0
    while valor <= num:
        if valor == num:
            triangular = True
        valor = valor + i
        i = i + 1
    return esTriangular

num = int(input("Ingrese el numero a evaluar: ")) 

while num <= 0:
    num = int(input("Ingrese un numero valido mayor a 0: "))

if validarOblongo(num):
    print("El numero es oblongo.")
else:
    print("El numero no es oblongo.")

if validarTriangular(num):
    print("El numero es triangular.")
else:
    print("El numero no es triangular.")    

# 6 es ambos

    
