class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)

    def recorrer_en_orden(self):
        elementos = []
        self._recorrer_en_orden_recursivo(self.raiz, elementos)
        return elementos

    def _recorrer_en_orden_recursivo(self, nodo, elementos):
        if nodo:
            self._recorrer_en_orden_recursivo(nodo.izquierda, elementos)
            elementos.append(nodo.valor)
            self._recorrer_en_orden_recursivo(nodo.derecha, elementos)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, valor)

# Ejemplo de uso de la clase ÁrbolBinario
arbol = ArbolBinario()

arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)

print("Recorrido en orden del árbol:", arbol.recorrer_en_orden())

valor_buscado = 7
encontrado = arbol.buscar(valor_buscado)

if encontrado:
    print(f"El valor {valor_buscado} está en el árbol.")
else:
    print(f"El valor {valor_buscado} no está en el árbol.")
