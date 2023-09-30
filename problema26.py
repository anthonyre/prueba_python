import math

class Circulo:
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    def calcular_area(self):
        area = math.pi * self.radio**2
        return area

# Ejemplo de uso de la clase Circulo
mi_circulo = Circulo(5, "rojo")

print(f"Círculo de radio {mi_circulo.radio} y color {mi_circulo.color}")
area_del_circulo = mi_circulo.calcular_area()
print(f"Área del círculo: {area_del_circulo:.2f}")
