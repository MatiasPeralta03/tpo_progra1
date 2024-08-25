# Describir una función diasiguiente(dia, mes año) que reciba como 
# parámetro una fecha cualquiera expresada por tres enteros y calcule 
# y devuelva otros tres enteros correspondientes el día siguiente al 
# dado. Utilizando esta función sin modificaciones ni agregados, 
# desarrollar programas que permitan:
# a.Sumar N días a una fecha.
# b.Calcular la cantidad de días existentes entre dos fechas cualesquiera.

def validarFecha(day, month, year):
    valid_date = False

    if 1582 < year:
        if month in [1,3,5,7,8,10,12]:
            if 0 < day and day <= 31:
                valid_date = True
        elif month in [4,6,9,11]:
            if 0 < day and day <= 30:
                valid_date = True
        elif month == 2:

        #Checkea si el anio es biciesto
            leap_year = False
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        leap_year = True
                else:
                    leap_year = True
            
            if leap_year:
                if 0 < day and day <= 29:
                    valid_date = True
            else:
                if 0 < day and day <= 28:
                    valid_date = True
    
    return valid_date

def unDiaMas(day, month, year):
    if month in [1,3,5,7,8,10,12]:
        if day == 31:
            day = 1
            if month == 12:
                month = 1
                year = year + 1
            else:
                month = month + 1
        else:
            day = day + 1
    elif month in [4,6,9,11]:
        if day == 30:
            day = 1
            month = month + 1
        else:
            day = day + 1
        
    elif month == 2:
        leap_year = False
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap_year = True
            else:
                leap_year = True
        
        if leap_year:
            if day == 29:
                day = 1
                month = month + 1
            else:
                day = day + 1
        else:
            if day == 28:
                day = 1
                month = month + 1
            else:
                day = day + 1
    
    return day, month, year

dia = int(input("Ingrese el dia de su fecha: "))

mes = int(input("Ingrese el mes de su fecha: "))

anio = int(input("Ingrese el anio de su fecha: "))

if validarFecha(dia, mes, anio):
    print("La fecha es valida.")
    listaDiaNuevo = unDiaMas(dia, mes, anio)
    print(f"El proximo dia luego de la fecha ingresada es {listaDiaNuevo[0]}/{listaDiaNuevo[1]}/{listaDiaNuevo[2]}.")
else:
    print("La fecha no es valida.")