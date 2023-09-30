def encontrar_maximo_y_minimo(lista):
    if len(lista) == 0:
        return None, None  
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = [5, 2, 8, 1, 9, 3, 7]
maximo, minimo = encontrar_maximo_y_minimo(numeros)

print("Número más grande:", maximo)
print("Número más pequeño:", minimo)