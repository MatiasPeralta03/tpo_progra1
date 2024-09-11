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

def calcularCostoSubte(viajes):

    url = "https://www.argentina.gob.ar/redsube/tarifas-de-transporte-publico-amba"

    #response = requests.get(url)

    #if response.status_code == 200:
    #    # Parse the content of the page
    #    soup = BeautifulSoup(response.content, 'html.parser')
    #    
    #    # Extraemos el precio actualizado de la pagina gubernamental de precios del transporte publico
    #    precioSubte = 650 #int(soup.find_all('td')[36].contents[0][2:]) # 650 pesos
    #else:
    #    print("Failed to retrieve the webpage")

    precioSubte = 650

    if 1 <= viajes <= 20:
        return precioSubte*viajes
    elif 21 <= viajes <= 30:
        return precioSubte*20 + precioSubte*0.80
    elif 31 <= viajes <= 40:
        return precioSubte*20 + precioSubte * 0.70
    elif 41 <= viajes:
        return precioSubte*20 + precioSubte * 0.60

viajes = int(input("Ingrese el valor de viajes efectuados: "))

while viajes <= 0:
    viajes = int(input("Ingrese un valor valido de viajes efectuados mayor a 0: "))

print("El precio final con los descuentos aplicados es de:", calcularCostoSubte(viajes))


