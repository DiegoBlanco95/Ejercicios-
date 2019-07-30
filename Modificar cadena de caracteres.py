"""Escribir un programa que permita ingresar una cadena de caracteres y coloque en
mayúscula la primera letra posterior a un espacio, eliminando todos los espacios
que contenga. Imprimir por pantalla la cadena obtenida."""

def coloca_may(cadena):
    cadena = cadena.title()
    cadena = cadena.replace(" ", "")     
    return cadena

cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.\
Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
print(cadena)
cadena = coloca_may(cadena)
print (cadena)
