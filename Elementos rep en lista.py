"""Escribir funciones para:
a. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
b. Generar una lista de 50 números aleatorios del 1 al 100 y comprobar con la
función anterior si existen elementos duplicados. Devolver True o False.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden."""


import random


def carga_elementos(cantidad,lista):
    contador = 0
    while contador < cantidad:
        n = random.randint(1,100)
        lista.append(n)
        contador = contador +1
    return lista


def elemento_rep(lista):
    largo = len(lista)
    dato = 0
    for valor in range(largo):
        cantidad = lista.count(lista[valor])    
        if cantidad > 1:
            dato +=1
            print("El valor: ", lista[valor])
    if dato >= 1:
        return True
    else:
        return False


def elementos_unicos(lista):
    largo = len(lista)
    nuevalista = []
    for valor in range(largo):
        repeticiones = lista.count(lista[valor])
        if repeticiones == 1:
            nuevalista.append(lista[valor])
    return nuevalista


lista = []
cantidad = random.randint(10,99)
lista = carga_elementos(cantidad, lista)
print(lista)
repetidos = elemento_rep(lista)
lista = []
lista2 = carga_elementos(50, lista)
print(lista2)
repetidos = elemento_rep(lista2)
lista2 = elementos_unicos(lista2)
print(lista2)
            
