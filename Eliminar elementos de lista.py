"""Eliminar de una lista de palabras las palabras que se encuentren en una segunda
lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante."""
import random


def carga_elementos(cantidad):
    lista = []
    contador = 0
    while contador < cantidad:
        n = input("Ingrese una palabra: ")
        lista.append(n)
        contador = contador +1
    return lista


def eliminar(lista_a, lista_b):
    largo_a = len(lista_a)
    for frase in range(largo_a-1):
        if lista_a[frase] in lista_b:
                lista_a.remove(lista_a[frase])
    nueva = lista_a
    return nueva
cantidad = random.randint(3,7)
lista_a = carga_elementos(cantidad)
print(lista_a)
lista_b = carga_elementos(cantidad)
print(lista_b)
nueva = eliminar(lista_a, lista_b)
print(nueva)
