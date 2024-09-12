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
    [50,"Aspiradora",2,88870,7,1]
]

nombres = []

for ventas in productos:
    if ventas[1] not in nombres:
        nombres.append(ventas[1])

print(nombres)

nombres_with_id = []

for i in range(len(nombres) - 1):
    nombres_with_id.append([i + 1, nombres[i]])

print(nombres_with_id)