class Diccionario:
    def __init__(self):
        self.diccionario = {}  # Inicializamos un diccionario vacío

    def agregar(self, clave, valor):
        self.diccionario[clave] = valor

    def buscar(self, clave):
        if clave in self.diccionario:
            return self.diccionario[clave]
        else:
            return f"La clave '{clave}' no existe en el diccionario."

    def eliminar(self, clave):
        if clave in self.diccionario:
            del self.diccionario[clave]
        else:
            print(f"La clave '{clave}' no existe en el diccionario.")

# Ejemplo de uso de la clase Diccionario
mi_diccionario = Diccionario()

mi_diccionario.agregar("nombre", "Juan")
mi_diccionario.agregar("edad", 30)
mi_diccionario.agregar("ciudad", "Madrid")

print("Diccionario completo:")
print(mi_diccionario.diccionario)

valor = mi_diccionario.buscar("edad")
print("Valor de 'edad':", valor)

mi_diccionario.eliminar("ciudad")

print("Diccionario después de eliminar 'ciudad':")
print(mi_diccionario.diccionario)
