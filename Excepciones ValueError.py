"""El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con elementos y permita que el usuario busque la posición que ocupa alguno
de ellos utilizando el método index. Si el elemento no pertenece a la lista se
imprimirá un mensaje de error y se solicitará un nuevo elemento para buscar. No
utilizar el operador in."""


import random


def carga_listas(n):
    lista = []
    for i in range(n):
        valor = random.randint(0,10)
        lista.append(valor)
    return lista


def buscar_lista(lista):
    while True:
        try:
            elemento = int(input("Ingrese un valor a buscar: "))
            posicion = lista.index(elemento)
            break
        except ValueError:
            print("El elemento no se encuentra en la lista")
    return posicion 


n = random.randint(1,30)
lista = carga_listas(n)
print(lista)
busqueda = buscar_lista(lista)
print(busqueda)


