from modules.historial import HistoryManager
from modules.pestanas import TabManager
from modules.descargas import DownloadManager
from modules.html_viewer import HTMLViewer
from modules.favoritos import FavoritesManager
from modules.paginas_locales import LocalPagesManager
from modules.historial_busqueda import SearchHistoryManager
from modules.cache import CacheManager

class WebBrowser:
    def __init__(self):
        self.html_viewer = HTMLViewer()
        self.history = HistoryManager()
        self.tabs = TabManager()
        self.downloads = DownloadManager()
        self.favorites = FavoritesManager()
        self.local_pages = LocalPagesManager()
        self.search_history = SearchHistoryManager()
        self.cache = CacheManager()

    def process_command(self, command):
        parts = command.split()
        if not parts:
            return True

        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        # Módulo 1: Historial de Navegación
        if cmd == "ir" and args:
            self.history.visit_url(args[0])
        elif cmd == "atras":
            self.history.go_back()
        elif cmd == "adelante":
            self.history.go_forward()
        elif cmd == "mostrar_historial":
            self.history.show_history()

        # Módulo 2: Pestañas
        elif cmd == "nueva_pestana" and args:
            self.tabs.new_tab(args[0])
        elif cmd == "cerrar_pestana":
            self.tabs.close_tab()
        elif cmd == "cambiar_pestana" and args:
            try:
                self.tabs.switch_tab(int(args[0]))
            except ValueError:
                print("Número de pestaña inválido")
        elif cmd == "mostrar_pestanas":
            self.tabs.show_tabs()

        # Módulo 3: Descargas
        elif cmd == "descargar" and args:
            self.downloads.add_download(args[0])
        elif cmd == "mostrar_descargas":
            self.downloads.show_downloads()
        elif cmd == "cancelar_descarga" and args:
            try:
                self.downloads.cancel_download(int(args[0]))
            except ValueError:
                print("Número de descarga inválido")

        # Módulo 4: Visualización de Páginas
        elif cmd == "listar_paginas":
            self.html_viewer.list_pages()
        elif cmd == "mostrar_contenido" and len(args) >= 2:
            self.html_viewer.show_content(args[0], args[1])

        # Módulo: Gestión de Favoritos
        elif cmd == "agregar_favorito" and len(args) >= 2:
            self.favorites.add_favorite(args[0], " ".join(args[1:]))
        elif cmd == "eliminar_favorito" and args:
            self.favorites.remove_favorite(args[0])
        elif cmd == "buscar_favorito" and args:
            self.favorites.search_favorite(args[0])
        elif cmd == "mostrar_favoritos":
            self.favorites.show_favorites()

        # Módulo: Páginas Locales
        elif cmd == "listar_paginas2":
            self.local_pages.list_pages()
        elif cmd == "ir2" and args:
            self.local_pages.visit_page(args[0])

        # Módulo: Historial de Búsqueda
        elif cmd == "buscar" and args:
            self.search_history.add_search(" ".join(args))
        elif cmd == "mostrar_historial_busquedas":
            self.search_history.show_history()
        elif cmd == "eliminar_busqueda" and len(args) >= 2:
            if args[0] == "--key" and len(args) > 1:
                self.search_history.delete_search(key=args[1])
            elif args[0] == "--fecha" and len(args) > 1:
                self.search_history.delete_search(date=args[1])

        # Módulo: Gestión de Caché
        elif cmd == "agregar_cache" and len(args) >= 2:
            self.cache.add_to_cache(args[0], " ".join(args[1:]))
        elif cmd == "obtener_cache" and args:
            self.cache.get_from_cache(args[0])
        elif cmd == "vaciar_cache" and len(args) >= 2:
            if args[0] == "--url" and len(args) > 1:
                self.cache.clear_cache(url=args[1])
            elif args[0] == "--fecha" and len(args) > 1:
                self.cache.clear_cache(date=args[1])

        # Comandos generales
        elif cmd == "ayuda":
            self.show_help()
        elif cmd == "salir":
            return False
        else:
            print("Comando no reconocido. Use 'ayuda' para ver los comandos disponibles.")
        
        return True

    def show_help(self):
        print("""
Comandos disponibles:

1. Historial de Navegación:
   - ir <url o ip>: Visitar una página
   - atras: Volver a la página anterior
   - adelante: Avanzar a la página siguiente
   - mostrar_historial: Mostrar todas las páginas visitadas

2. Gestión de Pestañas:
   - nueva_pestana <url>: Abrir una nueva pestaña
   - cerrar_pestana: Cerrar la pestaña actual
   - cambiar_pestana <n>: Cambiar a la pestaña número n
   - mostrar_pestanas: Mostrar todas las pestañas abiertas

3. Gestión de Descargas:
   - descargar <url>: Iniciar la descarga de un archivo
   - mostrar_descargas: Mostrar el estado de la cola de descargas
   - cancelar_descarga <n>: Cancelar la descarga número n

4. Visualización de Páginas:
   - listar_paginas: Mostrar todas las páginas HTML disponibles
   - mostrar_contenido <url> <modo>: Mostrar el contenido de una página
     Modos disponibles: basico, texto_plano

5. Gestión de Favoritos:
   - agregar_favorito <url> <título>: Añade un sitio a favoritos
   - eliminar_favorito <url>: Elimina un sitio de favoritos
   - buscar_favorito <url>: Busca un favorito
   - mostrar_favoritos: Muestra todos los favoritos

6. Páginas Locales:
   - listar_paginas2: Muestra todas las páginas disponibles
   - ir <url>: Visita una página local

7. Historial de Búsqueda:
   - buscar <palabra_clave>: Realiza una búsqueda
   - mostrar_historial_busquedas: Muestra el historial
   - eliminar_busqueda --key <palabra> | --fecha <YYYY-MM-DD>: Elimina búsquedas

8. Gestión de Caché:
   - agregar_cache <url> <contenido>: Agrega contenido a la caché
   - obtener_cache <url>: Recupera contenido de la caché
   - vaciar_cache --url <url> | --fecha <YYYY-MM-DD>: Limpia la caché

Comandos Generales:
   - ayuda: Mostrar esta ayuda
   - salir: Cerrar el navegador
        """)

def main():
    browser = WebBrowser()
    print("Bienvenido al Simulador de Navegador Web en Consola")
    print("Escribe 'ayuda' para ver la lista de comandos disponibles")
    
    while True:
        try:
            command = input("> ")
            if not browser.process_command(command):
                break
        except Exception as e:
            print(f"Error: {e}")
            print("Intente de nuevo o escriba 'ayuda' para ver los comandos disponibles")

    print("¡Hasta pronto!")

if __name__ == "__main__":
    main()
