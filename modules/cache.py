from BTree import BTree
from datetime import datetime
import json

class CacheManager:
    def __init__(self):
        self.cache = BTree(3)  # Árbol B con grado mínimo 3
        self._load_cache()

    def add_to_cache(self, url, content):
        """Agrega contenido a la caché"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cache.insert(url, content, timestamp)
        self._save_cache()
        print(f"Contenido agregado a la caché: {url}")

    def get_from_cache(self, url):
        """Recupera contenido de la caché"""
        content, timestamp = self.cache.search(url)
        if content:
            print(f"Cache hit para: {url}")
            print(f"Último acceso: {timestamp}")
            print(content)
        print(f"Cache miss para: {url}")
        return None

    def clear_cache(self, url=None, date=None):
        """Limpia la caché según los criterios especificados"""
        if url:
            # Implementar eliminación por URL específica
            print(f"Eliminando caché para: {url}")
        elif date:
            try:
                target_date = datetime.strptime(date, "%Y-%m-%d")
                self.cache.delete_by_date(date)
                print(f"Caché eliminada para entradas posteriores a: {date}")
            except ValueError:
                print("Formato de fecha inválido. Use YYYY-MM-DD")
        self._save_cache()

    def _save_cache(self):
        """Guarda el estado actual de la caché en un archivo"""
        try:
            cache_data = {
                'urls': self.cache.root.keys,
                'contents': self.cache.root.values,
                'timestamps': self.cache.root.timestamps
            }
            with open('data/cache.json', 'w') as f:
                json.dump(cache_data, f)
        except Exception as e:
            print(f"Error al guardar la caché: {e}")

    def _load_cache(self):
        """Carga el estado de la caché desde un archivo"""
        try:
            with open('data/cache.json', 'r') as f:
                cache_data = json.load(f)
                for i in range(len(cache_data['urls'])):
                    self.cache.insert(
                        cache_data['urls'][i],
                        cache_data['contents'][i],
                        cache_data['timestamps'][i]
                    )
        except FileNotFoundError:
            pass 