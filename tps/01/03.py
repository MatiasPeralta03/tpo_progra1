# Una persona desea llevar el control de los gastos realizados al viajar en el 
# subte-rráneo dentro de un mes. Sabiendo que dicho medio de transporte 
# utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) 
# se solicita desarrollar una función que reciba como parámetro la cantidad de 
# viajes realizados en un determinado mes y devuelva el total gastado en viajes. 
# Realizar también un programa para verificar el comportamiento de la función.
#
# Cantidad de viajes | Valor del pasaje
# 1 a 20             | Averiguar en Internet el valor actualizado
# 21 a 30            | 20% de descuento sobre tarifa máxima
# 31 a 40            | 30% de descuento sobre tarifa máxima
# Más de 40          | 40% de descuento sobre tarifa máxima

import requests
from bs4 import BeautifulSoup

def calcularCostoSubte(num1):

    url = "https://www.argentina.gob.ar/redsube/tarifas-de-transporte-publico-amba"

    response = requests.get(url)

    if response.status_code == 200:
        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraemos el precio actualizado de la pagina gubernamental de precios del transporte publico
        precioSubte = int(soup.find_all('td')[36].contents[0][2:]) # 650 pesos
    else:
        print("Failed to retrieve the webpage")

    precio = 0
    for i in range(1, num1 + 1):
        if 1 <= i <= 20:
            precio = precio + precioSubte
        elif 21 <= i <= 30:
            precio = precio + int(precioSubte * 0.80)
        elif 31 <= i <= 40:
            precio = precio + int(precioSubte * 0.70)
        elif 41 <= i:
            precio = precio + int(precioSubte * 0.60)
        
    print("El precio final con los descuentos aplicados es de:", precio)

num1 = int(input("Ingrese el valor de viajes efectuados: "))

while num1 <= 0:
    num1 = int(input("Ingrese un valor valido de viajes efectuados mayor a 0: "))

calcularCostoSubte(num1)

