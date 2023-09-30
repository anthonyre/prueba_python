class Cola:
    def __init__(self):
        self.items = []  # Inicializamos una lista vacía para representar la cola

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            print("La cola está vacía. No se puede desencolar.")

# Ejemplo de uso de la clase Cola
cola = Cola()

print("¿La cola está vacía?", cola.esta_vacia())  # Verificar si la cola está vacía

cola.encolar(1)  # Encolar elementos
cola.encolar(2)
cola.encolar(3)

print("¿La cola está vacía?", cola.esta_vacia())  # Verificar de nuevo

elemento = cola.desencolar()  # Desencolar un elemento
print("Elemento desencolado:", elemento)

print("¿La cola está vacía?", cola.esta_vacia())  # Verificar una vez más
