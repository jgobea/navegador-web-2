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
            self._insertar_recursivo(valor, self.raiz)
    def _insertar_recursivo(self, valor, nodo_actual):

        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(valor, self.raiz)
    def _eliminar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return None
        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursivo(valor,nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            else:
                sucesor = self._encontrar_minimo(nodo_actual.derecha)
                nodo_actual.valor = sucesor.valor
                nodo_actual.derecha = self._eliminar_recursivo(sucesor.valor, nodo_actual.derecha)
        return nodo_actual
    def _encontrar_minimo(self, nodo_actual):
        if nodo_actual.izquierda is None:
            return nodo_actual
        return self._encontrar_minimo(nodo_actual.izquierda)
    def modificar(self, valor_viejo, valor_nuevo):
        self.eliminar(valor_viejo)
        self.insertar(valor_nuevo)
    def consultar(self, valor):
        return self._consultar_recursivo(valor, self.raiz)
    def _consultar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._consultar_recursivo(valor, nodo_actual.izquierda)
        return self._consultar_recursivo(valor, nodo_actual.derecha)
    def preorden(self):
        self._preorden_recursivo(self.raiz)
    def _preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end=" ")
            self._preorden_recursivo(nodo_actual.izquierda)
            self._preorden_recursivo(nodo_actual.derecha)
    def inorden(self):
        self._inorden_recursivo(self.raiz)
    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.valor, end=" ")
            self._inorden_recursivo(nodo_actual.derecha)
    def postorden(self):
        self._postorden_recursivo(self.raiz)
    def _postorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden_recursivo(nodo_actual.izquierda)
            self._postorden_recursivo(nodo_actual.derecha)
            print(nodo_actual.valor, end=" ")
# Ejemplo de uso:
arbol = ArbolBinario()
#arbol.insertar(4)
#arbol.insertar(2)
#arbol.insertar(1)
#arbol.insertar(3)
#arbol.insertar(6)
#arbol.insertar(5)
#arbol.insertar(7)

arbol.insertar(15)
arbol.insertar(9)
arbol.insertar(6)
arbol.insertar(14)
arbol.insertar(13)
arbol.insertar(20)
arbol.insertar(17)
arbol.insertar(64)
arbol.insertar(26)
arbol.insertar(72)
print("Recorrido en Preorden:")
arbol.preorden()
print("\nRecorrido en Inorden:")
arbol.inorden()
print("\nRecorrido en Postorden:")
arbol.postorden()
valor_a_eliminar = 2
arbol.eliminar(valor_a_eliminar)
print(f"\nEl valor {valor_a_eliminar} ha sido eliminado.")
print("Recorrido en Inorden después de eliminar:")
arbol.inorden()
valor_a_modificar = 5
valor_nuevo = 8
arbol.modificar(valor_a_modificar, valor_nuevo)
print(f"\nEl valor {valor_a_modificar} ha sido modificado por {valor_nuevo}.")
print("Recorrido en Inorden después de modificar:")
arbol.inorden()
valor_a_consultar = 6
nodo_encontrado = arbol.consultar(valor_a_consultar)
if nodo_encontrado:
    print(f"\nEl valor {valor_a_consultar} está presente en el árbol.")
else:
    print(f"\nEl valor {valor_a_consultar} no está presente en el árbol.")
