def factorial(n):
    if n == 0:
        return 1  # El factorial de 0 es 1 por definición
    else:
        return n * factorial(n - 1)

numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")