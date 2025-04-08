# Diccionario con las combinaciones posibles de números romanos
# Ordenado de mayor a menor para poder hacer la conversión correctamente
valores_romanos = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]

# Función que convierte un número decimal (entero) a número romano
def decimal_to_roman(numero):
    resultado = ""  # Acumulador del número romano final

    # Recorremos cada valor del diccionario
    for valor, simbolo in valores_romanos:
        # Mientras el número sea mayor o igual al valor actual
        while numero >= valor:
            resultado += simbolo     # Agregamos el símbolo romano
            numero -= valor          # Restamos ese valor al número original

    return resultado  # Devolvemos el número romano final
