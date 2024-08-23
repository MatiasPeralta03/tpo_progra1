# En comercio de electrodomésticos necesita para su línea de cajas un programa que le 
# indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos 
# números enteros, correspondientes al total de la compra y al dinero recibido. 
# Informar cuántos billetes de cada denominación deben ser entregados como vuelto, de 
# tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
# de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el dinero 
# recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta de 
# billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se abona 
# con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 billete 
# de $200, 1 billete de $100 y 3 billetes de $10.

def calcularVuelto(total, recibido):
    vuelto = recibido - total
    lstBilletes = [5000, 1000, 500, 200, 100, 50, 10]
    lstVuelto = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(lstBilletes)):
        while vuelto >= lstBilletes[i]:
            vuelto = vuelto - lstBilletes[i]
            lstVuelto[i] = lstVuelto[i] + 1

    return lstVuelto
    
total = int(input("Ingrese el total de la compra: "))

while total <= 0:
    total = int(input("Ingrese un total de la compra valido mayor a 0: "))

recibido = int(input("Ingrese el dinero recibido: "))

while recibido < total:
    recibido = int(input("Se debe recibir el dinero justo o mas que el total de la compra : "))

listaVuelto = calcularVuelto(total, recibido)

print("--- Vuelto ---")
print("Cant. de billetes de 5000:", listaVuelto[0])
print("Cant. de billetes de 1000:", listaVuelto[1])
print("Cant. de billetes de 500:", listaVuelto[2])
print("Cant. de billetes de 200:", listaVuelto[3])
print("Cant. de billetes de 100:", listaVuelto[4])
print("Cant. de billetes de 50:", listaVuelto[5])
print("Cant. de billetes de 10:", listaVuelto[6])




