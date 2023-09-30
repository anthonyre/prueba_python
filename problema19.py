class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamamos al constructor de la clase base "Persona"
        super().__init__(nombre, edad)
        self.carrera = carrera

    def imprimir_detalles(self):
        # Sobrescribimos el método para imprimir los detalles del estudiante
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")

# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Juan", 20, "Ingeniería")

# Imprimir los detalles del estudiante
estudiante1.imprimir_detalles()
