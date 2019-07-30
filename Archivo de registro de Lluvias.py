"""Escribir un programa que permita grabar un archivo los datos de lluvia caída durante
un año. Cada línea del archivo se grabará con el siguiente formato:
<dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
Los datos se generarán mediante números al azar, asegurándose que las fechas
sean válidas. La cantidad de registros también será un número al azar entre 50 y
200. Por último se solicita mostrar un informe en formato matricial donde cada columna
represente a un mes y cada fila corresponda a los días del mes. Imprimir
además el total de lluvia caída en todo el año."""


import random


def validar_dia(mes, dia, año,registros):    
    if mes in[4,6,9,11]:
        if dia > 30:
            dia = random.randint(0,30)            
    elif mes == 2:
        if(año%4 == 0 and año%100!=0) or (año%400 == 0):
            if dia > 29:
                dia = random.randint(0,29)
            elif dia> 28:
                dia = random.randint(0,28)
    return dia,mes,registros


def imprime_matriz(matriz):
    filas = len(matriz)
    columna = len(matriz[0])
    for f in range(filas):
        for c in range(columna):
            (print("%6d" %matriz[f][c], end= ""))
        print()


try:
    arch = open(r"C:\Users\Diego\Desktop\lluvia.txt","wt")
    carga = input("Desea cargar los datos?\nIngrese s para continuar, n para finalizar: ")
    matriz = []
    filas = 31
    columnas = 12
    suma = 0
    año = random.randint(1995, 2018)
    for fila in range(filas):
        matriz.append([0]*columnas)
        
    while carga == "s":
        dia = random.randint(1,31)
        mes = random.randint(1,12)
        registros = random.randint(50,200)
        datos = validar_dia(mes,dia,año,registros) 
        datos = str(datos).replace(",",";")
        arch.write(datos + "\n")
        matriz[dia-1][mes-1] = registros 
        carga = input("Desea cargar los datos?\nIngrese s para continuar, s para finalizar: ")
    for fila in range(len(matriz)-1):
        suma = suma + sum(matriz[fila])
        line = "\n" + str(matriz[fila])
        arch.writelines(line)
    imprime = imprime_matriz(matriz)
    
    print(suma)
except IOError:
    print("No se puede grabar el archivo.")

finally:
    arch.close()
    
        




