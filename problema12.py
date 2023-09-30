def longitud_de_palabras(lista):
    diccionario = {}
    for palabra in lista:
        diccionario[palabra] = len(palabra)
    return diccionario

palabras = ["manzana", "banana", "pera", "uva", "sandía", "fresa", "kiwi"]
resultado = longitud_de_palabras(palabras)
print("Diccionario de palabras y sus longitudes:")
print(resultado)