class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def imprimir_detalles(self):
        print("Detalles del Libro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")

# Crear una instancia de la clase Libro
mi_libro = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 1925)

# Imprimir los detalles del libro
mi_libro.imprimir_detalles()
