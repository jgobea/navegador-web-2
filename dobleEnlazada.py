class Tab:
    def __init__(self, url, title, is_pinned=False, is_incognito=False, load_time=0):
        self.url = url
        self.title = title
        self.is_pinned = is_pinned  # Si la pestaña está "fijada" (no puede cerrarse fácilmente)
        self.is_incognito = is_incognito  # Si la pestaña está en modo incógnito
        self.load_time = load_time  # Tiempo de carga de la página
        self.is_active = False  # Pestaña activa
        self.history = [url]  # Historial de URLs visitadas en la pestaña
        self.next = None  # Siguiente pestaña
        self.prev = None  # Pestaña anterior

    def visit_url(self, new_url):
        """Visitar una nueva URL en esta pestaña, actualizando el historial."""
        self.history.append(new_url)
        self.url = new_url

    def show_info(self):
        """Muestra la información detallada de la pestaña."""
        status = " (Activa)" if self.is_active else ""
        pin_status = "Fijada" if self.is_pinned else "No fijada"
        incognito_status = "Incógnito" if self.is_incognito else "Normal"
        print(f"Pestaña: {self.title} | URL: {self.url} | Estado: {pin_status} | Modo: {incognito_status} | Tiempo de carga: {self.load_time} seg{status}")
        print(f"Historial: {self.history}")

class BrowserTabs:
    def __init__(self):
        self.current_tab = None

    def open_tab(self, url, title, is_pinned=False, is_incognito=False, load_time=0):
        new_tab = Tab(url, title, is_pinned, is_incognito, load_time)
        if not self.current_tab:
            self.current_tab = new_tab
            self.current_tab.is_active = True  # La primera pestaña abierta es la activa
        else:
            temp = self.current_tab
            while temp.next:  # Vamos al final de la lista
                temp = temp.next
            temp.next = new_tab
            new_tab.prev = temp

    def show_tabs(self):
        temp = self.current_tab
        while temp:
            temp.show_info()  # Mostrar información detallada de cada pestaña
            temp = temp.next

    def move_to_next_tab(self):
        if self.current_tab and self.current_tab.next:
            self.current_tab.is_active = False  # Desactivar la pestaña actual
            self.current_tab = self.current_tab.next
            self.current_tab.is_active = True  # Activar la siguiente pestaña
            print(f"Movido a: {self.current_tab.title}")
        else:
            print("No hay más pestañas.")

    def move_to_previous_tab(self):
        if self.current_tab and self.current_tab.prev:
            self.current_tab.is_active = False  # Desactivar la pestaña actual
            self.current_tab = self.current_tab.prev
            self.current_tab.is_active = True  # Activar la pestaña anterior
            print(f"Movido a: {self.current_tab.title}")
        else:
            print("No hay pestaña anterior.")

    def close_current_tab(self):
        if not self.current_tab:
            print("No hay pestañas para cerrar.")
            return

        print(f"Cerrando la pestaña: {self.current_tab.title}")
        
        if self.current_tab.prev:
            self.current_tab.prev.next = self.current_tab.next
        if self.current_tab.next:
            self.current_tab.next.prev = self.current_tab.prev
            self.current_tab = self.current_tab.next
        else:
            self.current_tab = self.current_tab.prev
        
        if self.current_tab:
            self.current_tab.is_active = True
    
    def switch_to_tab(self, tab_number):
        """Cambia a la pestaña especificada por número"""
        if not self.current_tab:
            return False

        # Desactivar la pestaña actual
        self.current_tab.is_active = False
        
        # Encontrar la pestaña solicitada
        temp = self.current_tab
        count = 1
        
        # Ir al inicio de la lista
        while temp.prev:
            temp = temp.prev
        
        # Buscar la pestaña por número
        while temp and count < tab_number:
            temp = temp.next
            count += 1
        
        if temp and count == tab_number:
            self.current_tab = temp
            self.current_tab.is_active = True
            return True
        
        # Si no se encontró la pestaña, reactivar la pestaña actual
        self.current_tab.is_active = True
        return False
