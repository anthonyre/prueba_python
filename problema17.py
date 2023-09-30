class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def calcular_area(self):
        return self.ancho * self.altura

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.altura)

# Crear una instancia de la clase Rectángulo
mi_rectangulo = Rectangulo(5, 10)

# Calcular y mostrar el área y el perímetro
area = mi_rectangulo.calcular_area()
perimetro = mi_rectangulo.calcular_perimetro()

print(f"Área del rectángulo: {area}")
print(f"Perímetro del rectángulo: {perimetro}")