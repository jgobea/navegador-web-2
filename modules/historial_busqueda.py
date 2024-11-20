from ArbolBinarioDemo import ArbolBinario
import csv
from datetime import datetime

class SearchHistoryManager:
    def __init__(self):
        self.search_tree = ArbolBinario()
        self._load_history()

    def add_search(self, keyword):
        """Añade una búsqueda al historial"""
        search_entry = {
            'keyword': keyword,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.search_tree.insertar(keyword)
        self._save_search(search_entry)
        print(f"Búsqueda registrada: {keyword}")

    def show_history(self):
        """Muestra el historial de búsquedas en orden"""
        print("\nHistorial de búsquedas:")
        self.search_tree.inorden()

    def delete_search(self, key=None, date=None):
        """Elimina búsquedas por palabra clave o fecha"""
        if key:
            self.search_tree.eliminar(key)
            print(f"Búsquedas con palabra clave '{key}' eliminadas")
        elif date:
            try:
                target_date = datetime.strptime(date, "%Y-%m-%d")
                # Implementar lógica para eliminar por fecha
                print(f"Búsquedas posteriores a {date} eliminadas")
            except ValueError:
                print("Formato de fecha inválido. Use YYYY-MM-DD")

    def _save_search(self, search_entry):
        """Guarda la búsqueda en el archivo CSV"""
        try:
            with open('data/busquedas.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    search_entry['keyword'],
                    search_entry['timestamp']
                ])
        except Exception as e:
            print(f"Error al guardar búsqueda: {e}")

    def _load_history(self):
        """Carga el historial desde el archivo CSV"""
        try:
            with open('data/busquedas.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        self.search_tree.insertar(row[0])
        except FileNotFoundError:
            pass 