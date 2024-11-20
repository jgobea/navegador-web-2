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

# Ejemplo de uso
avl_fs = AVLFileSystem()
avl_fs.insertar_archivo("archivo1.txt", "Este es el contenido del archivo 1")
avl_fs.insertar_archivo("archivo2.txt", "Este es el contenido del archivo 2")
avl_fs.insertar_archivo("archivo3.txt", "Este es el contenido del archivo 3")

avl_fs.in_order(avl_fs.raiz)
