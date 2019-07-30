"""Desarrollar un programa para eliminar todos los comentarios de un programa escrito
en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo "#" (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
y que también se considera comentario a las cadenas de documentación
(docstrings)."""



try:
    entrada = open(r"C:\Users\Diego\Desktop\ejercicio.txt","rt")
    salida = open(r"C:\Users\Diego\Desktop\ejercicio2.txt","wt")
    for linea in entrada:
        print(linea)
        lista = list(linea)
        if "#" in lista:
            if True:
                if  "'#'" in lista:
                    salida.write(linea)
                else:
                    pass
        else:
            salida.write(linea)
except IOError:
    print("No se puede grabar el archivo.")

finally:
    entrada.close()
    salida.close()            

try:
    salida = open(r"C:\Users\Diego\Desktop\ejercicio2.txt","rt")
    for line in salida:
        print(line)

except IOError:
    print("No se puede grabar el archivo.")

finally:
    salida.close()            

