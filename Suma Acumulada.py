import random

def carga_elementos(valor):
    lista = []
    while len(lista) < valor:
        lista.append(random.randint(0,20))
    return lista


def lista_acumulada(lista):
    acumulada = []
    for i in range(len(lista)-1):
        acumulada.append(lista[i] + lista[i+1])
    return acumulada


lista = carga_elementos(6)
print(lista)
acumulada = lista_acumulada(lista)
print(acumulada)
