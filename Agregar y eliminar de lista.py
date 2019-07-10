"""Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
ta verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar un vector con números al azar de cuatro dígitos. La cantidad de ele-
mentos también será un número al azar de dos dígitos.

b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.

c. Eliminar todas las repeticiones de un valor en la lista anterior. El valor a elimi-
nar se recibe como parámetro."""

import random


def carga_elementos(cantidad,lista):
    contador = 0
    while contador < cantidad:
        n = random.randint(1000,10000)
        #n = int(input("Ingrese un valor:"))
        lista.append(n)
        contador = contador +1
    return lista


def suma(lista_cargada):
    suma_total = sum(lista_cargada)
    return suma_total


def elimina_elemento(lista_cargada):
    busqueda = int(input("Ingrese un valor"))
    buscar = lista_cargada.count(busqueda)
    while buscar > 0:
        posicion = lista_cargada.index(busqueda)
        lista_cargada.pop(posicion)
        buscar = buscar - 1
    return lista_cargada


lista = []
cantidad_elementos = random.randint(10,100)
lista_cargada = carga_elementos(cantidad_elementos, lista)
sumar_elementos = suma(lista_cargada)

print(lista_cargada)
print(suma)
eliminar = elimina_elemento(lista_cargada)
print(eliminar)


