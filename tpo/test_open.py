def read_csv(file_path):
    try:
        arch = open(file_path, "rt")
        
        # Read and discard the header line
        arch.readline()
        
        linea = arch.readline()
        while linea:
            id, fecha, nombre_producto, cantidad, cliente, monto, medio_de_pago = linea.split(',')
            medio_de_pago = medio_de_pago.rstrip('\n')
            print(f"ID: {id:>7} - Monto: {monto}")
            linea = arch.readline()
            
        print("Archivo leido correctamente.")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

file = "tpo/generated_data_top.csv"

read_csv(file)

def menu():
    num = 0
    flag = False
    while not flag:
        num  = int(input("1.Ver ventas\n2.Ver productos\n3.Salir\n\nSeleccione una opcion: "))
        if num == 1:
            informes()
        elif num == 2:
            ver_productos()
        elif num == 3:
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