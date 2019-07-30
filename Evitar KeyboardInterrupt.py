"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000 evitando
que pueda ser interrumpido."""


def imprime_numeros():
    contador = 0
    numero = 1        
    while True:
        try:
            while contador < 1000:
                print(numero)
                numero = numero + 1
                contador = contador + 1
            break
        except KeyboardInterrupt:
            pass

numero = imprime_numeros()

        
