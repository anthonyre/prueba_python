class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo

    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.head:
            self.head = nuevo_nodo
            return
        actual = self.head
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso de la clase LinkedList
mi_lista = LinkedList()

mi_lista.insertar_al_final(1)
mi_lista.insertar_al_final(2)
mi_lista.insertar_al_final(3)

mi_lista.insertar_al_principio(0)

mi_lista.imprimir_lista()
