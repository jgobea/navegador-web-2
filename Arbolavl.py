class NodoArchivo:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVLFileSystem:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def insertar(self, nodo, nombre, contenido):
        if not nodo:
            return NodoArchivo(nombre, contenido)

        if nombre < nodo.nombre:
            nodo.izquierda = self.insertar(nodo.izquierda, nombre, contenido)
        elif nombre > nodo.nombre:
            nodo.derecha = self.insertar(nodo.derecha, nombre, contenido)
        else:
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        balance = self.obtener_balance(nodo)

        if balance > 1 and nombre < nodo.izquierda.nombre:
            return self.rotar_derecha(nodo)

        if balance < -1 and nombre > nodo.derecha.nombre:
            return self.rotar_izquierda(nodo)

        if balance > 1 and nombre > nodo.izquierda.nombre:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)

        if balance < -1 and nombre < nodo.derecha.nombre:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def insertar_archivo(self, nombre, contenido):
        self.raiz = self.insertar(self.raiz, nombre, contenido)

    def in_order(self, nodo):
        if nodo:
            self.in_order(nodo.izquierda)
            print(nodo.nombre)
            self.in_order(nodo.derecha)

    def postorden(self, nodo):
        """Recorrido en postorden del árbol"""
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(f"URL: {nodo.nombre}, Contenido: {nodo.contenido}")

    def mostrar_postorden(self):
        """Método público para iniciar el recorrido postorden desde la raíz"""
        self.postorden(self.raiz)

    def eliminar(self, nombre):
        """Elimina un archivo del árbol AVL"""
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        if not nodo:
            return nodo

        if nombre < nodo.nombre:
            nodo.izquierda = self._eliminar(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            nodo.derecha = self._eliminar(nodo.derecha, nombre)
        else:
            # Nodo encontrado
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            else:
                # Nodo con dos hijos: obtener el sucesor (mínimo en el subárbol derecho)
                temp = self._encontrar_minimo(nodo.derecha)
                nodo.nombre = temp.nombre
                nodo.contenido = temp.contenido
                nodo.derecha = self._eliminar(nodo.derecha, temp.nombre)

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        balance = self.obtener_balance(nodo)

        # Rotaciones para balancear el árbol
        if balance > 1 and self.obtener_balance(nodo.izquierda) >= 0:
            return self.rotar_derecha(nodo)
        if balance > 1 and self.obtener_balance(nodo.izquierda) < 0:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        if balance < -1 and self.obtener_balance(nodo.derecha) <= 0:
            return self.rotar_izquierda(nodo)
        if balance < -1 and self.obtener_balance(nodo.derecha) > 0:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def _encontrar_minimo(self, nodo):
        """Encuentra el nodo con el valor mínimo en el árbol"""
        if nodo.izquierda is None:
            return nodo
        return self._encontrar_minimo(nodo.izquierda)

    def consultar(self, nombre):
        """Consulta un archivo en el árbol AVL"""
        return self._consultar(self.raiz, nombre)

    def _consultar(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self._consultar(nodo.izquierda, nombre)
        return self._consultar(nodo.derecha, nombre)

