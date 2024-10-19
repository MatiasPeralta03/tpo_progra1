def read_csv(file_path):
    try:
        arch = open(file_path, "rt")
        
        # Read and discard the header line
        arch.readline()
        
        productos_con_monto = {}
        linea = arch.readline()
        while linea:
            id, fecha, producto, cantidad, cliente, monto, medio_de_pago = linea.split(';')
            if producto not in productos_con_monto.keys():
                productos_con_monto[producto] = 0
            
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

file = "tpo/ventas.csv" #tpo/ventas.csv 

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