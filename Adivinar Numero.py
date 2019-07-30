"""Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número
que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más."""


import random


def adivina_numero(n):
    contador = 0
    while True:
        try:
            valor = int(input("Ingrese el valor a adivinar: "))
            if valor < n:
                print("El numero buscado debe ser mayor a: ", valor)
                contador = contador + 1
            elif valor > n:
                print("El numero buscado debe ser menor a: ", valor)
                contador = contador + 1
            else:
                print("Usted ha ganado el juego, el numero buscado era:",n, "y le ha llevado", contador, "intentos")
                break
        except ValueError:
            print("El dato ingresado no es un valor numerico")
            contador = contador + 1


numero = random.randint(0,30)
adivinanza = adivina_numero(numero)

