entrada = input("Ingresa palabras separadas por espacios: ")
lista_de_palabras = entrada.split()
mas_de = int(input("Ingresa el numero limite de palabras "))

palabras_mas_de = [palabra for palabra in lista_de_palabras if len(palabra) > mas_de]

print("Palabras con más de ",mas_de," caracteres:", palabras_mas_de)