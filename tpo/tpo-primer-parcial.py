''' En este programa se busca analizar las ventas totales de productos de un distribuidor de tecnología. 
    Para esto se generó una matriz con los 100 productos comercializados en el mes. También generamos 
    2 listas "maestras" de categorias y marcas. Estos dos campos corresponden al índice '''

# Tablas maestras
marcas = [
    [1,"Samsung"], 
    [2,"EcoBrand"], 
    [3,"Electra"],
    [4,"MarcaY"],
    [5,"NovaTech"],
    [6,"LG"],
    [7,"TechPro"],
    [8,"MarcaX"],
    [9,"Drean"],
    [10,"Lenovo"],
    [11,"PrimeCo"],
    [12,"Whirpool"],
    [13,"Hormiga Negra"],
    [14,"Ruttini"],
    [15,"Adata"],
    [16,"Salenstein"],
    [17,"Motorola"],
    [18,"Origen"],
    [19,"La falda"],
    [20,"Perro viejo"],
    [21,"Brandin"],
    [22,"Hitachi"],
    [23,"BGH"],
    [24,"WU"]
]

categorias = [
    [1,"Tecnología"],
    [2,"Electrodomésticos"],
    [3,"Supermercado"],
    [4,"Juegos y Juguetes"]
]

productos = [
    [1, 'Tableta', 1, 1, 300000],   # ID, Nombre, ID Marca, ID Categoría, Precio Unitario
    [2, 'Lavadora', 22, 2, 500000], 
    [3, 'Router', 1, 1, 100000], 
    [4, 'Cafetera', 2, 2, 1500000], 
    [5, 'Cerveza', 4, 3, 2000], 
    [6, 'Cámara', 3, 1, 250000], 
    [7, 'Teclado', 5, 1, 75000], 
    [8, 'Monitor', 6, 1, 200000], 
    [9, 'Microonda', 7, 2, 120000], 
    [10, 'Refrigerador', 8, 2, 600000], 
    [11, 'Ratón', 9, 1, 30000], 
    [12, 'Aspiradora', 10, 2, 180000], 
    [13, 'Cámara web', 11, 1, 70000], 
    [14, 'Dinosaurio', 11, 4, 40000], 
    [15, 'Teléfono inteligente', 1, 1, 800000], 
    [16, 'Auto de juguete', 17, 4, 25000], 
    [17, 'Computadora portátil', 7, 1, 1200000], 
    [18, 'Impresora', 6, 1, 1500000], 
    [19, 'Acondicionador de aire', 5, 2, 700000], 
    [20, 'Vino', 14, 3, 30000], 
    [21, 'Reloj inteligente', 4, 1, 250000], 
    [22, 'Disco duro externo', 3, 1, 100000]
]

ventas = [
    [1, 1, 10],  # ID Venta, ID Producto, Cantidad Vendida
    [2, 5, 90],
    [3, 11, 13],
    [4, 14, 87],
    [5, 10, 4],
    [6, 20, 66]
]

def agregar_categoria():

    nombre_categoria = str(input("Ingrese el nombre de la categoria a agregar: "))

    # Verificar si la categoria ya existe
    existe_categoria = False
    for categoria in categorias:
        if categoria[1] == nombre_categoria:
            existe_categoria = True
            break

    if existe_categoria:
        print(f"La marca '{nombre_categoria}' ya existe.")
    else:
        nuevo_id = len(categorias) + 1
        categorias.append([nuevo_id, nombre_categoria])
        print(f"Marca '{nombre_categoria}' agregada con ID {nuevo_id}.")

def agregar_marca():
    nombre_marca = str(input("Ingrese el nombre de la marca a agregar: "))

    # Verificar si la marca ya existe
    existe_marca = False
    for marca in marcas:
        if marca[1] == nombre_marca:
            existe_marca = True
            break

    if existe_marca:
        print(f"La marca '{nombre_marca}' ya existe.")
    else:
        nuevo_id = len(marcas) + 1
        marcas.append([nuevo_id, nombre_marca])
        print(f"Marca '{nombre_marca}' agregada con ID {nuevo_id}.")

def agregar_producto():
    # Solicitar datos al usuario
    print('')
    nombre_producto = input("Ingrese el nombre del producto: ")

    # Verificar si el producto ya existe
    producto_existe = False
    for producto in productos:
        if producto[1] == nombre_producto:
            producto_existe = True
            break

    if producto_existe:
        print(f"El producto '{nombre_producto}' ya existe.")
        return

    nombre_marca = input("Ingrese el nombre de la marca: ")

    # Buscar ID de la marca
    id_marca = None
    for marca in marcas:
        if marca[1] == nombre_marca:
            id_marca = marca[0]
            break

    if id_marca is None:
        print(f"La marca '{nombre_marca}' no existe. Por favor, añádela primero.")
        print('')
        return

    nombre_categoria = input("Ingrese el nombre de la categoría: ")

    # Buscar ID de la categoría
    id_categoria = None
    for categoria in categorias:
        if categoria[1] == nombre_categoria:
            id_categoria = categoria[0]
            break

    if id_categoria is None:
        print(f"La categoría '{nombre_categoria}' no existe. Por favor, añádela primero.")
        return

    precio_unitario = float(input("Ingrese el precio unitario del producto: "))

    nuevo_id = len(productos) + 1
    productos.append([nuevo_id, nombre_producto, id_marca, id_categoria, precio_unitario])
    print(f"Producto '{nombre_producto}' agregado con ID {nuevo_id} y precio unitario {precio_unitario}.")

def agregar_venta():
    # Verificar si el ID del producto es válido
    print('')
    id_producto = int(input("Ingrese el ID del producto a agregar: "))

    producto_valido = False
    for producto in productos:
        if producto[0] == id_producto:
            producto_valido = True
            break

    if not producto_valido:
        print(f"No se puede agregar la venta. El producto con ID {id_producto} no existe.")
        print('')
        return
        

    cantidad_vendida = int(input("Ingrese la cantidad de unidades vendidas: "))
    print('')
    

    # Agregar la nueva venta
    nuevo_id = len(ventas) + 1
    nueva_venta = [nuevo_id, id_producto, cantidad_vendida]
    ventas.append(nueva_venta)
    print(f"Venta agregada: ID Venta {nuevo_id}, ID Producto {id_producto}, Cantidad Vendida {cantidad_vendida}.")
    print('')

def actualizar_categoria():
    print('')
    id_categoria = int(input("Ingrese el ID de la categoria a actualizar: "))

    categoria_encontrada = False
    for categoria in categorias:
        if categoria[0] == id_categoria:
            print(f"Modificarás la categoría {categoria[1]}")
            categoria[1] = str(input("Ingrese la nueva categoría: "))
            categoria_encontrada = True
            print(f"Categoría con ID {id_categoria} actualizada a '{categoria[1]}'.")
            break
        print('')

    if not categoria_encontrada:
        print(f"No se encontró la categoría con ID {id_categoria}.")
        print('')

def actualizar_marca():

    id_marca = int(input("Ingrese el ID de la marca a actualizar: "))

    marca_encontrada = False
    for marca in marcas:
        if marca[0] == id_marca:
            print(f"Modificarás la marca {marca[1]}")
            marca[1] = str(input("Ingrese la nueva marca: "))
            marca_encontrada = True
            print(f"Marca con ID {id_marca} actualizada a '{marca[1]}'.")
            break

    if not marca_encontrada:
        print(f"No se encontró la marca con ID {id_marca}.")

def actualizar_producto():
    # Solicitar datos al usuario
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))

    producto_valido = False
    for producto in productos:
        if producto[0] == id_producto:
            producto_valido = True
            break

    if not producto_valido:
        print(f"No se puede agregar la venta. El producto con ID {id_producto} no existe.")
        return

    nuevo_nombre_producto = input("Ingrese el nuevo nombre del producto: ")
    nuevo_id_marca = int(input("Ingrese el nuevo ID de la marca: "))

    # Verificar si la marca existe
    marca_existe = False
    for marca in marcas:
        if marca[0] == nuevo_id_marca:
            marca_existe = True
            break

    if not marca_existe:
        print(f"La marca con ID {nuevo_id_marca} no existe.")
        return

    nuevo_id_categoria = int(input("Ingrese el nuevo ID de la categoría: "))

    # Verificar si la categoría existe
    categoria_existe = False
    for categoria in categorias:
        if categoria[0] == nuevo_id_categoria:
            categoria_existe = True
            break

    if not categoria_existe:
        print(f"La categoría con ID {nuevo_id_categoria} no existe.")
        return

    nuevo_precio_unitario = float(input("Ingrese el nuevo precio unitario del producto: "))

    # Actualizar el producto
    producto_encontrado = False
    for producto in productos:
        if producto[0] == id_producto:
            producto[1] = nuevo_nombre_producto
            producto[2] = nuevo_id_marca
            producto[3] = nuevo_id_categoria
            producto[4] = nuevo_precio_unitario
            producto_encontrado = True
            print(f"Producto con ID {id_producto} actualizado.")
            break

    if not producto_encontrado:
        print(f"No se encontró el producto con ID {id_producto}.")

def actualizar_venta():
    # Solicitar datos al usuario
    id_venta = int(input("Ingrese el ID de la venta a actualizar: "))

    # Verificar si la venta existe
    venta_encontrada = False
    for venta in ventas:
        if venta[0] == id_venta:
            venta_encontrada = True
            break

    if not venta_encontrada:
        print(f"No se puede actualizar la venta. La venta con ID {id_venta} no existe.")
        return

    # Solicitar el nuevo ID del producto
    id_producto = int(input("Ingrese el nuevo ID del producto: "))

    # Verificar si el ID del producto es válido
    producto_valido = False
    for producto in productos:
        if producto[0] == id_producto:
            producto_valido = True
            break

    if not producto_valido:
        print(f"No se puede actualizar la venta. El producto con ID {id_producto} no existe.")
        return

    # Solicitar la nueva cantidad vendida
    nueva_cantidad = int(input("Ingrese la nueva cantidad vendida: "))

    # Actualizar la venta
    for venta in ventas:
        if venta[0] == id_venta:
            venta[1] = id_producto
            venta[2] = nueva_cantidad
            print(f"Venta con ID {id_venta} actualizada exitosamente.")
            return

    print(f"No se encontró la venta con ID {id_venta}.")

def eliminar_venta():
    # Solicitar el ID de la venta a eliminar

    id_venta = int(input("Ingresa el ID de la venta a eliminar: "))

    # Buscar la venta con el ID especificado
    venta_a_eliminar = None
    for venta in ventas:
        if venta[0] == id_venta:
            venta_a_eliminar = venta
            break

    if venta_a_eliminar:
        ventas.remove(venta_a_eliminar)
        print(f"Venta con ID {id_venta} eliminada.")
    else:
        print(f"No se encontró venta con ID {id_venta}.")

def ver_categorias():
    print('')
    print("-" * 21)
    print("Categorias".center(21))
    print("-" * 21)
    if categorias:
        print(f"{'ID':<4}{'Categoría':<25}")
        print("-" * 21)
        for categoria in categorias:
            print(f"{categoria[0]:<4}{categoria[1]:<25}")
        print("-" * 21)
    else:
        print("No hay categorías disponibles.")
    print('')

def ver_marcas():
    print('')
    print("-" * 16)
    print("Marcas".center(16))
    print("-" * 16)
    if marcas:
        print(f"{'ID':<4}{'Marca':<25}")
        print("-" * 16)
        for marca in marcas:
            print(f"{marca[0]:<4}{marca[1]:<25}")
        print("-" * 16)
    else:
        print("-" * 40)
        print("--No hay marcas disponibles--")
        print("-" * 40)
    print('')

def ver_productos():
    print('')
    print("-" * 91)
    print("Catalogo de productos".center(91))
    print("-" * 91)
    if productos:
        print(f"{'ID':<4}{'Producto':<25}{'Precio Unitario':<25}{'Marca':<20}{'Categoría':<20}")
        print("-" * 91)
        for producto in productos:
            # Encontrar nombre de marca y categoría para mostrar
            marca_nombre = "Desconocida"
            for marca in marcas:
                if marca[0] == producto[2]:
                    marca_nombre = marca[1]
                    break

            categoria_nombre = "Desconocida"
            for categoria in categorias:
                if categoria[0] == producto[3]:
                    categoria_nombre = categoria[1]
                    break

            print(f"{producto[0]:<4}{producto[1]:<25}{producto[4]:<25}{marca_nombre:<20}{categoria_nombre:<20}")       
    else:
        print("No hay productos disponibles.")
    
    print("-" * 91)
    print("")

def ver_ventas():
    if ventas:
        print('')
        print("-" * 105)
        print("Listado de productos detallado".center(105))
        print("-" * 105)
        print(f"{'ID':<5}{'Producto':<20}{'Cantidad':<20}{'Precio Unitario':<20}{'Marca':<23}{'Categoría':<20}")
        print("-" * 105)
        for venta in ventas:
            for producto in productos:
                if producto[0] == venta[1]: #ID producto - ID producto en la venta
                    producto_nombre = producto[1]
                    precio_unitario = producto[4]

                    # Encontrar el nombre de la marca y la categoría del producto
                    for marca in marcas:
                        if marca[0] == producto[2]:
                            marca_nombre = marca[1]
                            break

                    for categoria in categorias:
                        if categoria[0] == producto[3]:
                            categoria_nombre = categoria[1]
                            break
                    break

            print(f"{venta[0]:<5}{producto_nombre:<20}{venta[2]:<20}{precio_unitario:<20}{marca_nombre:<23}{categoria_nombre:<20}")
        print("-" * 105)
        print('')

def generar_informes():

    # Listas para almacenar resultados
    ganancias_por_marca = [0]*len(marcas)
    ventas_por_marca = [0]*len(marcas)
    ganancias_por_categoria = [0]*len(categorias)

    # Calcular las ganancias
    for venta in ventas:
        id_producto = venta[1]
        cantidad_vendida = venta[2]

        # Encontrar el producto correspondiente
        for producto in productos:
            if producto[0] == id_producto:
                precio_unitario = producto[4]
                id_marca = producto[2]
                id_categoria = producto[3]

                # Calcular la ganancia
                ganancia = cantidad_vendida * precio_unitario

                # Calcular ventas por marca
                ventas_por_marca[id_marca - 1] += cantidad_vendida

                # Acumulando la ganancia por marca
                ganancias_por_marca[id_marca - 1] += ganancia

                # Acumulando la ganancia por categoría
                ganancias_por_categoria[id_categoria - 1] += ganancia

    #Inicializamos contadores totales
    total_gan_categ = 0

    # Imprimir los resultados
    print('')
    print("-" * 40)
    print("Las marcas y sus ganancias".center(40))
    print("-" * 40)

    for i in range(len(ganancias_por_marca)):
        if ganancias_por_marca[i] != 0:
            print("-",marcas[i][1],end="") #Nombre de marca
            print(str(ganancias_por_marca[i]).rjust(37 - len(marcas[i][1]),"."),end="")
            print("$")

    # Imprimir los resultados
    print('')
    print("-" * 40)
    print("Las marcas y sus ventas".center(40))
    print("-" * 40)

    for i in range(len(ventas_por_marca)):
        if ventas_por_marca[i] != 0:
            print("-",marcas[i][1],end="") # [[id1, NOMBRE1],[id2, NOMBRE2],[id3, NOMBRE3]]
            print(str(ventas_por_marca[i]).rjust(38 - len(marcas[i][1]),"."))

    print("-" * 40)    
    print('')
    print("-" * 40)
    print("Ganancia total por categoría".center(40))
    print("-" * 40)

    for i in range(len(ganancias_por_categoria)):
        total_gan_categ += ganancias_por_categoria[i]
        print("-",categorias[i][1],end="")
        print(str(ganancias_por_categoria[i]).rjust(37 - len(categorias[i][1]),"."),end="")
        print("$")
    
    print("-" * 40)
    print('')
    # Calcular porcentajes e imprimir listado final
    print("-" * 40)
    print("Ganancia porcentual por categoria".center(40))
    print("-" * 40)
    for i in range(len(ganancias_por_categoria)):
        porcentaje = ganancias_por_categoria[i] * 100 / total_gan_categ
        print("- %s (%.2f%%)" %(categorias[i][1], porcentaje), end=" ")
        # Imprimir el gráfico de barras
        puntos = "*" * int(porcentaje/10)
        print(puntos.rjust(28 - len(categorias[i][1])," "))
    print("-" * 40)
    print('')

def menu():
    num = 0
    while num != 15:
        num  = int(input("1.Ver ventas\n2.Ver productos\n3.Ver marca\n4.ver categorias\n5.Agregar venta\n6.Agregar producto\n7.Agregar marca"
                            "\n8.Agregar categoria\n9.Actualizar venta\n10.Actualizar producto\n11.Actualizar marca\n12.Actualizar categoria"
                            "\n13.Eliminar venta\n14.Generar informe\n15.Salir\n\nSeleccione una opcion: "))
        if num == 1:
            ver_ventas()
        elif num == 2:
            ver_productos()
        elif num == 3:
            ver_marcas()
        elif num == 4:
            ver_categorias()
        elif num == 5:
            agregar_venta()
        elif num == 6:
            agregar_producto()
        elif num == 7:
            agregar_marca()
        elif num == 8:
            agregar_categoria()
        elif num == 9:
            actualizar_venta()
        elif num == 10:
            actualizar_producto()
        elif num == 11:
            actualizar_marca()
        elif num == 12:
            actualizar_categoria()
        elif num == 13:
            eliminar_venta()
        elif num == 14:
            generar_informes()
        else:
            print('')
            print("-" * 80)
            print("--ERROR--".center(80))
            print("Vuelva a ingresar un número dentro del rango o 15 para salir".center(80))
            print("-" * 80)
            print('')
        
print('')
print("-" * 80)
print(("Bienvenido al sistema de analisis de venta").center(80))
print("-" * 80)

menu()

print('')
print("-" * 80)
print("Saliendo...".center(80))
print("Gracias por usar nuestro sistema.".center(80))
print("-" * 80)
print('')







