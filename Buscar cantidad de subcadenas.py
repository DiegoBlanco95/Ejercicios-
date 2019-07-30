"""Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que
los caracteres de la subcadena no necesariamente deben estar en forma consecutiva
dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
Cadena:
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.
Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Sub-cadena: UADE
Cantidad encontrada: 4 """


def contar_subcadena(cadena, subcadena):
    largo = len(cadena)
    sub = len(subcadena)
    contador = 0
    cantidad = 0
    for caracter in range(largo-1):
        if cadena[caracter] == subcadena[contador]:
            contador = contador + 1
            
            if contador == sub:
                contador = 0
                cantidad = cantidad + 1
    return cantidad

cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.\
Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
subcadena = "uade"
cantidad = contar_subcadena(cadena, subcadena)
print("Se encontraron", cantidad, "repeticiones")
