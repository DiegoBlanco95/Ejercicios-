"""Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra". Realizar un programa para obtener ambas claves,
donde la primera se construye con los dígitos impares de la clave maestra y la
segunda con los dígitos pares. Los dígitos se numeran desde la izquierda. Ejemplo:
Si clave maestra = 12345, la clave 1 sería 135 y la clave 2 sería 24."""


import random


def generar_numero_entero():
    clavemaestra = ""
    largo = random.randint(0, 6)
    contador = 0
    while contador <= largo:
        n = random.randint(0, 9)
        n = str(n)
        clavemaestra = clavemaestra + n
        contador = contador + 1
    return clavemaestra


def claves(clavemaestra):
    largo = len(clavemaestra)
    clave_par = []
    clave_impar = []
    for valor in range(largo):
        if int(clavemaestra[valor]) % 2 == 0:
            clave_par.append(clavemaestra[valor])
        else:
            clave_impar.append(clavemaestra[valor])

    return clave_par, clave_impar


clave_maestra = generar_numero_entero()
print(clave_maestra)
clave = claves(clave_maestra)
print(clave)
