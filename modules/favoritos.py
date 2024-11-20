from Arbolavl import AVLFileSystem
import csv
from datetime import datetime

class FavoritesManager:
    def __init__(self):
        self.avl_tree = AVLFileSystem()
        self._load_favorites()

    def add_favorite(self, url, title=""):
        """Añade un sitio a favoritos"""
        try:
            self.avl_tree.insertar_archivo(url, title)
            self._save_favorite(url, title)
            print(f"Favorito agregado: {url} - {title}")
        except Exception as e:
            print(f"Error al agregar favorito: {e}")

    def remove_favorite(self, url):
        """Elimina un sitio de favoritos"""
        try:
            if self.avl_tree.eliminar(url):
                self._update_favorites_csv()  # Actualiza el CSV después de eliminar
                print(f"Favorito eliminado: {url}")
                return True
            else:
                print(f"No se pudo eliminar el favorito: {url}")
                return False
        except Exception as e:
            print(f"Error al eliminar el favorito: {e}")
            return False

    def search_favorite(self, url):
        """Busca un favorito en el árbol (preorden)"""
        result = self.avl_tree.consultar(url)
        if result:
            print(f"Favorito encontrado: {url}")
            return True
        print("Favorito no encontrado")
        return False

    def show_favorites(self):
        """Muestra todos los favoritos (postorden)"""
        print("\nLista de favoritos:")
        self.avl_tree.mostrar_postorden()

    def _save_favorite(self, url, title):
        """Guarda el favorito en el archivo CSV"""
        try:
            with open('data/favoritos.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([url, title, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        except Exception as e:
            print(f"Error al guardar favorito: {e}")

    def _load_favorites(self):
        """Carga los favoritos desde el archivo CSV"""
        try:
            with open('data/favoritos.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 2:
                        self.avl_tree.insertar_archivo(row[0], row[1])
        except FileNotFoundError:
            # El archivo se creará cuando se agregue el primer favorito
            pass

    def _update_favorites_csv(self):
        """Actualiza el archivo CSV con los favoritos actuales"""
        try:
            with open('data/favoritos.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                self._write_favorites_to_csv(writer, self.avl_tree.raiz)
        except Exception as e:
            print(f"Error al actualizar el archivo de favoritos: {e}")

    def _write_favorites_to_csv(self, writer, nodo):
        """Escribe los favoritos en el archivo CSV desde el árbol"""
        if nodo:
            self._write_favorites_to_csv(writer, nodo.izquierda)
            writer.writerow([nodo.nombre, nodo.contenido, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
            self._write_favorites_to_csv(writer, nodo.derecha)