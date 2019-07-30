"""Escribir una función filtrar_palabras() que reciba una lista de palabras y un entero
N, y devuelva las palabras que tengan más de n caracteres. Escribir también un
programa para verificar el comportamiento de la misma. Hacer una función para
cada uno de los siguientes casos:
a. Utilizando ciclos
b. Mediante listas por comprensión"""


import random


def cargar_frase():
    contador = 0
    while contador != -1:
        palabra = input("Ingrese una frase: ")
        cad = palabra.split()
        contador = -1
    return cad


def filtrar_palabras(lista_palabras, n):   
    largo = len(lista_palabras) 
    cadena = ""
    for palabra in range(largo):
        if len(lista_palabras[palabra]) > n:
            cadena = cadena + lista_palabras[palabra]
    cadena = str(cadena)
    return cadena

def filtrar_palabras2(lista_palabras, n): 
    cadena = [palabra for palabra in lista_palabras if len(palabra) > n]
    return cadena
    
n = random.randint(0,7)
print(n)
lista_palabras = cargar_frase()
print(lista_palabras)
filtrar = filtrar_palabras2(lista_palabras,n)
print(filtrar)
            
            
        
        
    
