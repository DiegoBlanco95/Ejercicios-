"""La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo."""


import math


def raiz_cuadrada(n):
    while True:
        try:
            raiz =  math.sqrt(n)
            break
        except ValueError:
            n = int(input("Ingrese un numero positivo: "))
    return raiz


n = int(input("Ingrese un numero: "))
cuadrado = raiz_cuadrada(n)
print (cuadrado)
