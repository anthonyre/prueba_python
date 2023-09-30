class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

persona1 = Persona("Juan", 30)

persona1.imprimir_detalles()