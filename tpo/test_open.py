def read_csv(file_path):
    try:
        arch = open(file_path, "rt")
        
        # Read and discard the header line
        arch.readline()
        
       
        
        productos_con_monto = {}
        linea = arch.readline()
        while linea:
            descuento_cliente = 1
            porcentaje_pago = 1
            id, fecha, producto, cantidad, cliente, monto, medio_de_pago = linea.split(';')
            medio_de_pago = medio_de_pago.rstrip('\n')
            monto = int(monto)
            if producto not in productos_con_monto.keys():
                productos_con_monto[producto] = 0
            
            # Descuento por cliente recurrente
            if cliente == "Y":
                descuento_cliente -= 0.10  # 10% de descuento si es cliente recurrente
            
            # Ajuste por método de pago
            if medio_de_pago == "Efectivo":
                porcentaje_pago -= 0.05  # 5% de descuento si paga en efectivo
            elif medio_de_pago == "Transferencia":
                porcentaje_pago -= 0.05  # 5% de descuento si paga por transferencia
            elif medio_de_pago == "Tarjeta":
                porcentaje_pago += 0.10  # 10% de aumento si paga con tarjeta
            
            
            # Calcular el monto final aplicando primero el descuento por cliente y luego el ajuste por método de pago
            monto_final = monto * ((descuento_cliente + porcentaje_pago)-1)
            
            # Mostrar información del cliente y su monto ajustado
            print(f"Cliente: {cliente}, Producto: {producto}, Monto original: {monto:.2f}$, Monto ajustado: {monto_final:.2f}$ (Descuento por cliente: {descuento_cliente*100-100:.2f}%, Ajuste por pago: {porcentaje_pago*100-100:.2f}%)")
            
            
            productos_con_monto[producto] += int(monto)
            medio_de_pago = medio_de_pago.rstrip('\n')
            linea = arch.readline()

        for key, value in sorted(productos_con_monto.items(), key=lambda item: item[1], reverse=True): #item es la dupla y item[1] es el segundo valor de esta dupla traida desde el diccionario
            print(f"{key}: {value}$")

                

        print("Archivo leido correctamente.") 
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    except ValueError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

file = "tpo/ventas - copia.csv" #tpo/ventas.csv 



def menu():
    flag = False
    while not flag:
        num = int(input("1.Ver informes\n2.Salir\n\nSeleccione una opcion: "))
        if num == 1:
            print(f"Monto por producto")
            read_csv(file)
        elif num == 2:
            flag = True
        else:
            print('')
            print("-" * 80)
            print("--ERROR--".center(80))
            print("Vuelva a ingresar un número dentro del rango o 15 para salir".center(80))
            print("-" * 80)
            print('')
        
print('')
print("-" * 80)
print(("Bienvenido al sistema de analisis de ventas").center(80))
print("-" * 80)
print('')

menu()

print('')
print("-" * 80)
print("Saliendo...".center(80))
print("Gracias por usar nuestro sistema.".center(80))
print("-" * 80)
print('')

#id;fecha;producto;cantidad;cliente;monto;medio_de_pago
#1;21/02/2023;Producto H;13;Y;390000;Efectivo
#2;26/03/2023;Producto O;13;N;169000;Tarjeta
#3;09/01/2023;Producto I;4;N;100000;Transferencia
#4;28/11/2023;Producto S;12;Y;192000;Tarjeta
#5;24/04/2023;Producto N;17;N;238000;Tarjeta