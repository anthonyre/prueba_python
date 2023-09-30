class Pila:
    def __init__(self):
        self.items = []  # Inicializamos una lista vacía para representar la pila

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía. No se puede desapilar.")

# Ejemplo de uso de la clase Pila
pila = Pila()

print("¿La pila está vacía?", pila.esta_vacia())  # Verificar si la pila está vacía

pila.apilar(1)  # Apilar elementos
pila.apilar(2)
pila.apilar(3)

print("¿La pila está vacía?", pila.esta_vacia())  # Verificar de nuevo

elemento = pila.desapilar()  # Desapilar un elemento
print("Elemento desapilado:", elemento)

print("¿La pila está vacía?", pila.esta_vacia())  # Verificar una vez más
