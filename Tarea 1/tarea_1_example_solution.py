# Metodo potencia manual
def potencia_manual(base, potencia):
    # Validar que ambos parámetros sean enteros
    if not isinstance(base, int) or not isinstance(potencia, int):
        return -400, None  # Código de error para tipo de datos inválido

    resultado = 1
    for _ in range(potencia):
        resultado *= base

    return 0, resultado  # Código de éxito y resultado de la potencia


# Método separa_letras
def separa_letras(cadena):

    # Verificar que el parámetro sea un string
    if not isinstance(cadena, str):
        return -100, None, None
    # Verificar que el string no esté vacío
    if cadena == "":
        return -300, None, None
    # Verificar que la cadena solo contenga letras del abecedario
    # isalpha() regresa True si todos los caracteres son letras del abecedario
    # Se toma Not True si hay algún dato distinto de una letra del abecedario
    if not cadena.isalpha():
        return -200, None, None

    # Separar en mayúsculas y minúsculas
    # Se recorre cada carácter c en la cadena

    # Solo agrega c a la lista si c.isupper() es True (es una mayuscula)
    mayusculas = "".join([c for c in cadena if c.isupper()])

    # Solo agrega c a la lista si c.islower() es True (es una minuscula)
    minusculas = "".join([c for c in cadena if c.islower()])
    return 0, mayusculas, minusculas
