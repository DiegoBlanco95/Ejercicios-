"""Definir una función superposición() que reciba como parámetros dos listas de cualquier
tipo y devuelva True si tienen al menos un elemento en común, o False en
caso contrario. Desarrollar un programa para verificar su comportamiento."""


import random


def carga_elementos(cantidad):
    lista = []
    contador = 0
    while contador < cantidad:
        n = random.randint(1,15)
        #n = int(input("Ingrese un valor:"))
        lista.append(n)
        contador = contador +1
    return lista


def superposicion(primera, segunda):
    largop = len(primera)
    largos = len(segunda)
    value = 0
    for valor in range(largop):
        for num in range(largos):
            print("Se compara el valor: ", primera[valor], " con el valor: ", segunda[num])
            if primera[valor] == segunda[num]:
                print("El valor ", primera[valor], " esta repetido en ambas listas")
                value = value + 1
    if value >= 1:
        return True
    else:
        return False
    

cantidad = int(input("Ingrese un valor: "))
primera = carga_elementos(cantidad)
cantidad = int(input("Ingrese un valor: "))
segunda = carga_elementos(cantidad)
superposicion = superposicion(primera, segunda)
print(superposicion)
