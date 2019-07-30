"""Escribir una función que reciba como parámetro un número entero entre 0 y 999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres."""
import random
def numero_romano(valor):
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

    unidad = valor % 10
    decena = (valor//10)%10
    centena = (valor//100)%10

    if valor >= 100:
        valor = centenas[centena] + decenas[decena] + unidades[unidad]
    elif valor >= 10:
        valor = decenas[decena] + unidades[unidad]
    else:
        valor = unidades[unidad]
    return valor

valor = random.randint(0,10000)
print(valor)
#valor = int(input("Ingrese un valor: "))
valor = numero_romano(valor)
print(valor)
