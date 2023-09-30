class Matriz:
    def __init__(self, filas, columnas, elementos=None):
        self.filas = filas
        self.columnas = columnas
        if elementos is None:
            self.elementos = [[0] * columnas for _ in range(filas)]
        else:
            self.elementos = elementos

    def mostrar(self):
        for fila in self.elementos:
            print(fila)

    def sumar(self, otra_matriz):
        if self.filas == otra_matriz.filas and self.columnas == otra_matriz.columnas:
            resultado = [[0] * self.columnas for _ in range(self.filas)]
            for i in range(self.filas):
                for j in range(self.columnas):
                    resultado[i][j] = self.elementos[i][j] + otra_matriz.elementos[i][j]
            return Matriz(self.filas, self.columnas, resultado)
        else:
            print("No se pueden sumar las matrices. Las dimensiones son diferentes.")
            return None

    def multiplicar_por_escalar(self, escalar):
        resultado = [[0] * self.columnas for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado[i][j] = self.elementos[i][j] * escalar
        return Matriz(self.filas, self.columnas, resultado)

# Ejemplo de uso de la clase Matriz
matriz1 = Matriz(2, 2, [[1, 2], [3, 4]])
matriz2 = Matriz(2, 2, [[5, 6], [7, 8]])

print("Matriz 1:")
matriz1.mostrar()

print("Matriz 2:")
matriz2.mostrar()

resultado_suma = matriz1.sumar(matriz2)
print("Resultado de la suma:")
resultado_suma.mostrar()

escalar = 2
resultado_multiplicacion = matriz1.multiplicar_por_escalar(escalar)
print(f"Resultado de la multiplicación por {escalar}:")
resultado_multiplicacion.mostrar()
