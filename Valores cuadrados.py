"""Para un número entero N menor de 100 recibido como parámetro, escribir un programa
que utilice una función para devolver la suma de los cuadrados de aquellos
números entre 1 y N que están separados entre si por cuatro unidades. (1 2 + 52 +
92 + 132 + …)"""

def suma_cuadrados(valor):

    contador = 1
    total = 0
    while contador <= valor:
        total = contador**2 + total
        print(contador)
        contador = contador + 4
        print(total)

    return total

valor = int(input("Ingrese un valor"))
suma = suma_cuadrados(valor)
print (suma)
        
