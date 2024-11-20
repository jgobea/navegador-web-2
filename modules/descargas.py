from Cola import RequestQueue
import csv
from datetime import datetime

class DownloadManager:
    def __init__(self):
        self.download_queue = RequestQueue()
        self.completed_downloads = []

    def add_download(self, url, size="1MB"):
        """Añade una nueva descarga a la cola"""
        download = {
            'url': url,
            'size': size,
            'date': datetime.now(),
            'status': 'pending'
        }
        self.download_queue.enqueue_request(url)
        self._save_download(download)
        print(f"\nDescarga añadida a la cola: {url}")
        print(f"Tamaño: {size}")
        print("Estado: Pendiente")

    def cancel_download(self, index):
        """Cancela una descarga específica por su índice"""
        if self.download_queue.cancel_request(index):
            print(f"\nDescarga {index} cancelada exitosamente")
            self._save_download({
                'url': f'descarga_{index}',
                'size': 'N/A',
                'date': datetime.now(),
                'status': 'cancelled'
            })
            return True
        print(f"\nNo se pudo cancelar la descarga {index}")
        return False

    def show_downloads(self):
        """Muestra todas las descargas pendientes y su estado"""
        print("\n=== Cola de Descargas ===")
        if self.download_queue.is_empty():
            print("No hay descargas pendientes")
        else:
            self.download_queue.show_requests()
        
        print("\n=== Historial de Descargas ===")
        self._show_download_history()

    def _show_download_history(self):
        """Muestra el historial de descargas desde el archivo CSV"""
        try:
            with open('data/descargas.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 4:
                        url, size, date, status = row
                        print(f"URL: {url}")
                        print(f"Tamaño: {size}")
                        print(f"Fecha: {date}")
                        print(f"Estado: {status}")
                        print("-" * 30)
        except FileNotFoundError:
            print("No hay historial de descargas")

    def _save_download(self, download):
        """Guarda la información de la descarga en el archivo CSV"""
        try:
            with open('data/descargas.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    download['url'],
                    download.get('size', 'Unknown'),
                    download['date'].strftime("%Y-%m-%d %H:%M:%S"),
                    download['status']
                ])
        except Exception as e:
            print(f"Error al guardar la descarga: {e}")

    def process_next_download(self):
        """Procesa la siguiente descarga en la cola"""
        if not self.download_queue.is_empty():
            url = self.download_queue.process_request()
            download = {
                'url': url,
                'date': datetime.now(),
                'status': 'completed',
                'size': '1MB'  # Tamaño simulado
            }
            self.completed_downloads.append(download)
            self._save_download(download)
            print(f"\nDescarga completada: {url}")
            return True
        return False
