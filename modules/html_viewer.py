from bs4 import BeautifulSoup

class HTMLViewer:
    def __init__(self, hosts_file='data/hosts.txt'):
        self.hosts = self._load_hosts(hosts_file)
        self.current_mode = "basico"

    def _load_hosts(self, hosts_file):
        hosts = {}
        try:
            with open(hosts_file, 'r') as file:
                next(file)
                for line in file:
                    ruta, ip, dominio = line.strip().split()
                    hosts[ip] = {'ruta': ruta, 'dominio': dominio}
                    hosts[dominio] = {'ruta': ruta, 'ip': ip}
        except FileNotFoundError:
            print(f"Archivo {hosts_file} no encontrado")
        return hosts

    def show_content(self, url_or_ip, mode=None):
        if url_or_ip not in self.hosts:
            print(f"URL o IP no encontrada: {url_or_ip}")
            return

        ruta = self.hosts[url_or_ip]['ruta']
        print(ruta)
        self._display_content(ruta, mode or self.current_mode)

    def _display_content(self, ruta, mode):
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                content = file.read()
                if mode == "basico":
                    print(content)
                elif mode == "texto_plano":
                    soup = BeautifulSoup(content, 'html.parser')
                    print(soup.get_text())
        except FileNotFoundError:
            print(f"Archivo no encontrado: {ruta}")

    def list_pages(self):
        print("Páginas disponibles:")
        for host, info in self.hosts.items():
            if '.' in host:
                print(f"- {host} ({info['ruta']})")
