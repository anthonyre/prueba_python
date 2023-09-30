def contar(cadena, letra):
    contador = 0

    for caracter in cadena:
        if caracter == letra:
            contador += 1

    return contador

texto = input("Ingresa un texto: ")
letra_a_contar = input("Ingresa una letra límite para contar la letra repetida: ")

resultado = contar(texto, letra_a_contar)
print(f"La letra '{letra_a_contar}' aparece {resultado} veces en la cadena.")
