class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía. No se puede desapilar.")

class PilaLimitada(Pila):
    def __init__(self, limite):
        super().__init__()
        self.limite = limite

    def esta_llena(self):
        return len(self.items) == self.limite

# Ejemplo de uso de la clase PilaLimitada
pila_limitada = PilaLimitada(5)  # Crear una pila limitada con límite de 5 elementos

print("¿La pila está vacía?", pila_limitada.esta_vacia())

pila_limitada.apilar(1)
pila_limitada.apilar(2)
pila_limitada.apilar(3)
pila_limitada.apilar(4)
pila_limitada.apilar(5)

print("¿La pila está llena?", pila_limitada.esta_llena())

pila_limitada.apilar(6)  # Intentar apilar un elemento cuando la pila está llena
pila_limitada.desapilar()  # Desapilar un elemento

print("¿La pila está llena?", pila_limitada.esta_llena())
