from Pila import RequestStack
import csv
from datetime import datetime

class HistoryManager:
    def __init__(self):
        self.back_stack = RequestStack()  # Pila para ir hacia atrás
        self.forward_stack = RequestStack()  # Pila para ir hacia adelante
        self.current_page = None

    def visit_url(self, url):
        if self.current_page:
            self.back_stack.push_request(self.current_page)
            self.forward_stack = RequestStack()  # Limpiar pila de adelante
        self.current_page = url
        print(f"\nNavegando a: {url}")
        self._save_to_history(url)

    def go_back(self):
        if self.back_stack.top:
            self.forward_stack.push_request(self.current_page)
            self.current_page = self.back_stack.top.data
            self.back_stack.process_request()  # Hace pop de la pila
            print(f"\nRegresando a: {self.current_page}")
            return True
        print("\nNo hay páginas anteriores")
        return False

    def go_forward(self):
        if self.forward_stack.top:
            self.back_stack.push_request(self.current_page)
            self.current_page = self.forward_stack.top.data
            self.forward_stack.process_request()  # Hace pop de la pila
            print(f"\nAvanzando a: {self.current_page}")
            return True
        print("\nNo hay páginas siguientes")
        return False

    def _save_to_history(self, url):
        with open('data/historial.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([url, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    def show_history(self):
        try:
            with open('data/historial.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(f"{row[0]} - {row[1]}")
        except FileNotFoundError:
            print("No hay historial disponible")
