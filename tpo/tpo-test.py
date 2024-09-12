''' En este programa se busca analizar las ventas totales de productos de un distribuidor de tecnología. 
    Para esto se generó una matriz con los 100 productos comercializados en el mes. También generamos 
    2 listas "maestras" de categorias y marcas. Estos dos campos corresponden al índice '''

#Lista de Categorias

categorias = [
    [1,"Tecnología"],
    [2,"Electrodomésticos"],
    [3,"Supermercado"],
    [4,"Juegos y Juguetes"]
]

#Lista de Marcas

marcas= [
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

''' Matriz de productos Nx6, siendo N la cantidad de filas.
    Los campos son id,nombre,marca,precio_unitario,cantidad,categoria '''

productos=[
    [1,"Tableta",3,347610,72,0],
    [2,"Lavadora",5,618650,96,1],
    [3,"Router",1,73760,1,0],
    [4,"Cafetera",2,93530,45,1],
    [5,"Cerveza",3,3500,29,1],
    [6,"Cámara",4,760310,14,0],
    [7,"Tableta",5,479000,40,0],
    [8,"Teclado",6,56840,2,0],
    [9,"Monitor",2,44000,82,0],
    [10,"Microonda",3,2860,22,1],
    [11,"Refrigerador",7,929780,82,1],
    [12,"Ratón",1,65030,85,0],
    [13,"Lavadora",5,827970,11,1],
    [14,"Cámara",4,2038760,10,0],
    [15,"Router",6,86540,43,0],
    [16,"Aspiradora",4,16980,73,1],
    [17,"Microonda",2,112780,82,1],
    [18,"Cámara web",1,65400,2,0],
    [19,"Dinosaurio",2,87450,59,3],
    [20,"Microonda",2,74370,11,1],
    [21,"Cerveza",6,4100,60,2],
    [22,"Teléfono inteligente",10,900110,22,0],
    [23,"Lavadora",8,769020,87,1],
    [24,"Auto de juguete",6,82890,48,3],
    [25,"Tableta",9,228790,77,0],
    [26,"Dinosaurio",1,7280,13,1],
    [27,"Computadora portátil",7,17790,45,0],
    [28,"Impresora",4,60150,49,0],
    [29,"Lavadora",12,618900,96,1],
    [30,"Computadora portátil",10,65730,81,0],
    [31,"Acondicionador de aire",8,1398100,62,0],
    [32,"Refrigerador",4,20180,67,1],
    [33,"Vino",13,98600,10,2],
    [34,"Impresora",14,228660,17,0],
    [35,"Acondicionador de aire",5,1278600,60,1],
    [36,"Teléfono inteligente",10,2700590,54,0],
    [37,"Impresora",1,44100,55,0],
    [38,"Ratón",10,40070,32,0],
    [39,"Computadora portátil",4,85360,44,0],
    [40,"Aspiradora",6,964660,75,1],
    [41,"Reloj inteligente",2,16500,84,0],
    [42,"Cámara",7,6718610,94,0],
    [43,"Teclado",1,220930,66,0],
    [44,"Cafetera",14,237830,30,1],
    [45,"Acondicionador de aire",1,1863000,41,0],
    [46,"Vino",16,22140,81,2],
    [47,"Teléfono inteligente",14,2100910,46,0],
    [48,"Aspiradora",10,26480,81,0],
    [49,"Cámara web",14,45160,22,0],
    [50,"Aspiradora",2,88870,7,1],
    [51,"Dinosaurio",4,62900,30,3],
    [52,"Aspiradora",6,46540,95,1],
    [53,"Auto de juguete",4,98820,85,3],
    [54,"Teléfono inteligente",2,1500090,70,0],
    [55,"Impresora",4,26390,58,0],
    [56,"Dinosaurio",10,97330,44,3],
    [57,"Disco duro externo",15,16120,33,0],
    [58,"Ratón",1,99380,78,0],
    [59,"Cámara web",1,81900,35,0],
    [60,"Cámara",7,5289620,77,0],
    [61,"Monitor",10,28320,30,0],
    [62,"Computadora portátil",1,1570930,53,0],
    [63,"Vino",18,81430,19,2],
    [64,"Reloj inteligente",14,541200,31,0],
    [65,"Refrigerador",3,80460,91,0],
    [66,"Auto de juguete",6,89480,40,3],
    [67,"Auriculares",4,22610,88,0],
    [68,"Tableta",17,382660,32,0],
    [69,"Vino",19,48780,10,2],
    [70,"Cámara",1,94700,98,0],
    [71,"Impresora",2,97160,74,0],
    [72,"Computadora portátil",7,88200,54,0],
    [73,"Vino",20,65920,94,2],
    [74,"Impresora",7,3130,36,0],
    [75,"Cámara web",3,151700,14,0],
    [76,"Cámara web",1,60290,95,0],
    [77,"Monitor",1,25530,98,0],
    [78,"Vino",14,46970,17,2],
    [79,"Monitor",22,74920,87,0],
    [80,"Impresora",2,20140,24,0],
    [81,"Ratón",2,81770,65,0],
    [82,"Acondicionador de aire",12,2609000,91,1],
    [83,"Reloj inteligente",7,44450,17,0],
    [84,"Router",10,116080,90,0],
    [85,"Monitor",7,41170,91,0],
    [86,"Refrigerador",14,207870,17,1],
    [87,"Ratón",6,93150,46,0],
    [88,"Acondicionador de aire",22,1202330,46,0],
    [89,"Impresora",14,81690,2,0],
    [90,"Dinosaurio",7,71890,67,3],
    [91,"Computadora portátil",7,72480,5,0],
    [92,"Cámara web",2,160810,74,0],
    [93,"Router",22,104590,72,0],
    [94,"Auriculares",7,10300,66,0],
    [95,"Cafetera",3,185570,6,1],
    [96,"Ratón",1,91510,81,0],
    [97,"Teléfono inteligente",7,393900,6,0],
    [98,"Teléfono inteligente",4,81670,11,0],
    [99,"Disco duro externo",23,903260,57,0],
    [100,"Acondicionador de aire",24,941390,15,1]
]

#Total de ventas
total_ventas = 0
lista_valores_por_marca = [0]*len(marcas)
lista_top = []
for producto in productos:
    total_ventas += producto[3] * producto[4]
    lista_valores_por_marca[producto[2] - 1] += producto[3] * producto[4]

for i in range(len(lista_valores_por_marca) - 1):
    lista_top.append([marcas[i][1], lista_valores_por_marca[i]])

lista_top_ordenada = sorted(lista_top, key=lambda x: x[1], reverse=True)
print("Top 10 de marcas con mas ventas")
for i in range(10):
    print(f"- {lista_top_ordenada[i][0]} - {lista_top_ordenada[i][1]}$")

print(f"Capital total de ganancia: {total_ventas}$") 

# 1. Determinar las marcas más vendidas
marca_ventas = {}
for producto in productos:
    marca_id = producto[2]
    cantidad = producto[4]
    if marca_id in marca_ventas:
        marca_ventas[marca_id] += cantidad
    else:
        marca_ventas[marca_id] = cantidad

# Encontrar la marca más vendida
max_ventas = -1
marca_mas_vendida = None
for marca_id in marca_ventas:
    if marca_ventas[marca_id] > max_ventas:
        max_ventas = marca_ventas[marca_id]
        marca_mas_vendida = marca_id

# 2. Determinar la mayor venta (precio total = precio unitario * cantidad)
mayor_venta_producto = productos[0]
max_total_venta = productos[0][3] * productos[0][4]

for producto in productos[1:]:
    total_venta = producto[3] * producto[4]
    if total_venta > max_total_venta:
        max_total_venta = total_venta
        mayor_venta_producto = producto

nombre_mayor_venta = mayor_venta_producto[1]
total_mayor_venta = max_total_venta

# 3. Determinar la categoría más consumida
categoria_consumo = {}
for producto in productos:
    categoria_id = producto[5]
    cantidad = producto[4]
    if categoria_id in categoria_consumo:
        categoria_consumo[categoria_id] += cantidad
    else:
        categoria_consumo[categoria_id] = cantidad

# Encontrar la categoría más consumida
max_consumo = -1
categoria_mas_consumida = None
for categoria_id in categoria_consumo:
    if categoria_consumo[categoria_id] > max_consumo:
        max_consumo = categoria_consumo[categoria_id]
        categoria_mas_consumida = categoria_id

# Resultados
print(f"Mayor venta: {nombre_mayor_venta} con un total de ${total_mayor_venta}.")