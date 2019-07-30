"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""

def eliminar_subcadena(cadena, posicion, cantidad):
    largo = len(cadena)
    fin = posicion + cantidad
    nueva = ""
    for caracter in range(largo):
        if caracter >= posicion and caracter <= fin:
            pass
        else:
            nueva = nueva + cadena[caracter]
    return nueva

def eliminar_subcadena2(cadena, posicion, cantidad):
    fin = posicion + cantidad
    print(fin)
    nuevo = cadena[0:posicion] + cadena[fin:]
    return nuevo

cadena = "“La victoria de hoy es sobre tu yo de ayer, la de mañana será sobre un hombre inferior”"
posicion = int(input("Ingrese la posicion: "))
cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))
sub = eliminar_subcadena(cadena, posicion, cantidad)
print(sub)
