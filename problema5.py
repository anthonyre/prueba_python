def fibonacci_hasta_limite(limite):
    a, b = 0, 1
    fibonacci = []
    while a <= limite:
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci

limite = int(input("Ingresa un número límite para la secuencia de Fibonacci: "))

secuencia_fibonacci = fibonacci_hasta_limite(limite)

print("Secuencia de Fibonacci hasta", limite, ":")
print(secuencia_fibonacci)