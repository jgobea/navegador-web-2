class NodoDirectorio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subdirectorios = []

    def agregar_subdirectorio(self, subdirectorio):
        self.subdirectorios.append(subdirectorio)

    def encontrar_subdirectorio(self, nombre):
        for subdirectorio in self.subdirectorios:
            if subdirectorio.nombre == nombre:
                return subdirectorio
        return None

    def eliminar_subdirectorio(self, nombre):
        for subdirectorio in self.subdirectorios:
            if subdirectorio.nombre == nombre:
                self.subdirectorios.remove(subdirectorio)
                return True
        return False

    def recorrido_preorden(self):
        print(self.nombre)
        for subdirectorio in self.subdirectorios:
            subdirectorio.recorrido_preorden()

    def recorrido_inorden(self):
        if len(self.subdirectorios) > 0:
            self.subdirectorios[0].recorrido_inorden()
        print(self.nombre)
        for subdirectorio in self.subdirectorios[1:]:
            subdirectorio.recorrido_inorden()

    def recorrido_postorden(self):
        for subdirectorio in self.subdirectorios:
            subdirectorio.recorrido_postorden()
        print(self.nombre)


class FileSystem:
    def __init__(self):
        self.raiz = NodoDirectorio("Raíz")

    def crear_directorio(self, ruta, nombre):
        directorio_actual = self._navegar_ruta(ruta)
        if directorio_actual:
            nuevo_directorio = NodoDirectorio(nombre)
            directorio_actual.agregar_subdirectorio(nuevo_directorio)
            return True
        return False

    def listar_directorio(self, ruta):
        directorio_actual = self._navegar_ruta(ruta)
        if directorio_actual:
            return [subdir.nombre for subdir in directorio_actual.subdirectorios]
        return None

    def eliminar_directorio(self, ruta, nombre):
        directorio_actual = self._navegar_ruta(ruta)
        if directorio_actual:
            return directorio_actual.eliminar_subdirectorio(nombre)
        return False

    def _navegar_ruta(self, ruta):
        if ruta == "/":
            return self.raiz

        partes_ruta = ruta.split("/")
        directorio_actual = self.raiz
        for parte in partes_ruta:
            if parte:
                directorio_actual = directorio_actual.encontrar_subdirectorio(parte)
                if not directorio_actual:
                    return None
        return directorio_actual

