def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    
    # Comparar la cadena original con su versión invertida
    return cadena == cadena[::-1]

texto = input("Ingresa una cadena de texto: ")

if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")