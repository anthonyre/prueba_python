def es_primo(numero):
    if numero <= 1:
        return False  
    elif numero <= 3:
        return True  
    elif numero % 2 == 0 or numero % 3 == 0:
        return False 
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True

# Ejemplo de uso de la función
numero = int(input("Ingresa un número entero: "))
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")