"""Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo
números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error."""


import random


def carga_listas(n):    
    lista = []            
    while True:
        try:
            for i in range(n):
                #valor = random.randint(0,10)
                valor = int(input("Ingrese un valor: "))
                lista.append(valor)
            break
        except ValueError:
            n = n - i
            print("Ingrese un valor valido")  
    return lista


def suma_listas(lista_1, lista_2, n):
    for i in range(n):
        result = lista_1[i] + lista_2[i]
        print(result)


n = random.randint(1,5)
print(n)
lista_1 = carga_listas(n)
print(lista_1)
lista_2 = carga_listas(n)
print(lista_2)
result = suma_listas(lista_1, lista_2, n)

    


