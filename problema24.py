class Empleado:
    def __init__(self, nombre, salario, aumento):
        self.nombre = nombre
        self.salario = salario
        self.aumento = aumento

    def calcular_salario_actualizado(self):
        salario_actualizado = self.salario + (self.salario * (self.aumento / 100))
        return salario_actualizado

# Ejemplo de uso de la clase Empleado
empleado1 = Empleado("Juan", 30000, 10)  # Nombre, salario inicial y aumento del 10%

salario_actualizado = empleado1.calcular_salario_actualizado()
print(f"El salario actualizado de {empleado1.nombre} es ${salario_actualizado:.2f}")
