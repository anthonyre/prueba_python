def sumar_positivos_y_negativos(lista):
    suma_positivos = 0
    suma_negativos = 0

    for numero in lista:
        if numero > 0:
            suma_positivos += numero
        elif numero < 0:
            suma_negativos += numero

    return suma_positivos, suma_negativos

# Ejemplo de uso de la función
numeros = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
suma_positivos, suma_negativos = sumar_positivos_y_negativos(numeros)

print("Suma de números positivos:", suma_positivos)
print("Suma de números negativos:", suma_negativos)