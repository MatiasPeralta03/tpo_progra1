# Desarrollar una función que reciba tres números enteros positivos correspondientes al día, 
# mes, año de una fecha y verifique si corresponden a una fecha válida. Debe tenerse en cuenta 
# la cantidad de días de cada mes, incluyendo los años bisiestos. Devolver True o False 
# según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento 
# de la función.

def validarFecha(day, month, year):
    valid_date = False

    if 1582 < year:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if 0 < day and day <= 31:
                valid_date = True
        elif month == 4 or month == 6 or month == 9 or month == 11:
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

dia = int(input("Ingrese el dia de su fecha: "))

mes = int(input("Ingrese el mes de su fecha: "))

anio = int(input("Ingrese el anio de su fecha: "))

if validarFecha(dia, mes, anio):
    print("Fecha valida.")
else:
    print("Fecha invalida.")

