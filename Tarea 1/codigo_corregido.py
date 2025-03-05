# definición de funciones

def validarMes(mes):

    if int(mes) < 1 or int(mes) > 12:
        return "invalido"
    else:
        return "valido"


def multiplicar():
    i = 0
    valorA = int(input("Ingrese el primer valor:"))
    valorB = int(input("Ingrese el segundo valor: "))
    valorC = int(input("Ingrese el tercer valor: "))
    while i == 0:
        if valorB < valorC:
            multiplicar = (valorA*valorB)
            i += 1
            print(multiplicar)
        else:
            return "Ingrese un tercer valor que sea mayor al segundo"
    return
