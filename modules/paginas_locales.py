from nario import FileSystem
import csv
from datetime import datetime

class LocalPagesManager:
    def __init__(self, hosts_file='data/hosts.txt'):
        self.file_system = FileSystem()
        self.hosts = {}
        self._load_hosts(hosts_file)
        self._initialize_file_system()

    def _load_hosts(self, hosts_file):
        """Carga el mapeo de hosts desde el archivo"""
        try:
            with open(hosts_file, 'r') as file:
                next(file)  # Skip header
                for line in file:
                    ruta, ip, dominio = line.strip().split()
                    self.hosts[dominio] = {'ruta': ruta, 'ip': ip}
                    self.hosts[ip] = {'ruta': ruta, 'dominio': dominio}
        except FileNotFoundError:
            print(f"Archivo {hosts_file} no encontrado")

    def _initialize_file_system(self):
        """Inicializa el sistema de archivos con los hosts cargados"""
        for host, info in self.hosts.items():
            if '/' in host:  # Es un dominio con ruta
                parts = host.split('/')
                current_path = "/"
                for part in parts[:-1]:  # Crear estructura de directorios
                    if current_path == "/":
                        current_path = part
                    else:
                        current_path = f"{current_path}/{part}"
                    self.file_system.crear_directorio("/", current_path)

    def list_pages(self):
        """Lista todas las páginas disponibles (inorden)"""
        print("\nPáginas HTML disponibles:")
        for host, info in sorted(self.hosts.items()):
            print(f"- {host} ({info['ruta']})")

    def visit_page(self, url_or_ip):
        """Visita una página por URL o IP"""
        if url_or_ip in self.hosts:
            info = self.hosts[url_or_ip]
            try:
                with open(info['ruta'], 'r', encoding='utf-8') as file:
                    content = file.read()
                    print(f"\nVisitando: {url_or_ip}")
                    print("Contenido (Modo Básico):")
                    print(content)
            except FileNotFoundError:
                print(f"Archivo no encontrado: {info['ruta']}")
        else:
            print(f"URL o IP no encontrada: {url_or_ip}") 