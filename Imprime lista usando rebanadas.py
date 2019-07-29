"""Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores
de la lista, utilizando la técnica de las rebanandas."""

import random
def carga_elementos(valor):
    lista = []
    numero = 1
    while numero < valor:
        lista.append(numero**2)
        numero += 1
    return lista


valor = int(input("Ingrese un valor: "))
lista = carga_elementos(valor, lista)
print(lista)
print(lista[len(lista) - 10:])
