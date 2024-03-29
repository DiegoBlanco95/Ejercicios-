"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento
de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes
casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""

def extraer_subcadena(cadena, posicion, cantidad):
    fin = posicion + cantidad
    subcadena = cadena[posicion:fin+1]
    return subcadena
    
def extraer_subcadena2(cadena, posicion, cantidad):
    fin = posicion + cantidad
    largo = len(cadena)
    contador = 0
    nueva = ""
    for caracter in range(largo):
        if contador >= posicion and contador <=fin:
            nueva = nueva + cadena[caracter]
        contador = contador + 1
    return nueva
    
cadena = '"El número de teléfono es 4356-7890"'
posicion = int(input("Ingrese la posicion deseada: "))
cantidad = int(input("Ingrese la cantidad de caracteres deseada: "))
subcadena = extraer_subcadena2(cadena, posicion, cantidad)
print(subcadena)
