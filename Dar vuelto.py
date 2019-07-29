"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados al cliente
como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona
con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
de $20, 1 billete de $10 y 3 billetes de $1."""

def entregar_vuelto(recibido, total):
    vuelto = recibido - total
    billetes = [500, 100, 50, 20, 10, 5, 1]
    dinero = len(billetes)
    cantidad = ""
    contador = 0
    cantidades = []
    for billete in range(dinero):
        contador = 0
        while vuelto >= billetes[billete]:
            vuelto = vuelto - billetes[billete]
            if vuelto >= 0:
                contador = contador + 1            
        if contador != 0:
            cantidad = ("Se entregaron " , str(contador) , " billetes de: " , str(billetes[billete]))
            cantidades.append(cantidad)
    return cantidades

total = int(input("Ingrese el valor total de la compra: "))
recibido = int(input("Ingrese el dinero recibido: "))

compra = entregar_vuelto(recibido, total)
largo = len(compra)
print(largo)
contador  = 0
while contador < largo:
    print(compra[contador])
    contador = contador + 1
                        
            
