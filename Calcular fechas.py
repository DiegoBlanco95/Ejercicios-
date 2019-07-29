"""Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera
expresada por tres enteros (correspondientes al día, mes y año) y calcule y
devuelva tres enteros correspondientes el día siguiente al dado.
Utilizando esta función, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera."""

def cant_dias(mes, año):
    if mes in [4, 6, 9, 11]:
        dias = 30
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    elif mes ==2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            dias = 29
        else:
            dias = 28
    else:
        dias = - 1
    return dias


def cargar_fechas():
    mes = int(input("Ingrese un mes: "))
    mes = mes_valido(mes)
    año = int(input("Ingrese un año: "))
    cantidad_dias = cant_dias(mes, año)
    dia = int(input("Ingrese un dia: "))
    if dia > cantidad_dias:
        dia = int(input("Ingrese un dia menor a la cantidad de dias del mes que es: " + str(cantidad_dias) + "\n "))
    return dia, mes, año


def mes_valido(mes):
    if mes > 12 or mes < 1:
        mes = int(input("Ingrese un mes valido entre 1 y 12: "))
    else:
        return mes
    return mes


def dia_siguiente(dia, mes, año):
    dias = cant_dias(mes, año)
    if dia == dias:
        dia_siguiente = 1
        if mes == 12:
            mes = 1
            año = año + 1
        else:
            mes = mes + 1
    else:
        dia_siguiente = dia + 1
    return(dia_siguiente, mes, año)


def fecha_mayor(fecha1, fecha2):
    if fecha1[2] < fecha2[2]:
        mayor = fecha2
    elif fecha1[2] > fecha2[2]:
        mayor = fecha1
    elif fecha1[2] == fecha2[2]:
        if fecha1[1] > fecha2[1]:
            mayor = fecha1
        else:
            mayor = fecha2
    return mayor


def diferencia_dias(fecha1, fecha2):
    contador = 0
    mayor = fecha_mayor(fecha1, fecha2)
    if mayor != fecha2:
        menor = fecha2
    else:
        menor = fecha1
    while menor != mayor:
        menor = dia_siguiente(menor[0], menor[1], menor[2],)
        contador += 1
    return contador

fecha1 = cargar_fechas()
fecha2 = cargar_fechas()
print("La diferencia entre dias es : ",diferencia_dias(fecha1, fecha2))



        
    
