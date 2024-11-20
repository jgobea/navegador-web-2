from dobleEnlazada import BrowserTabs, Tab

class TabManager:
    def __init__(self):
        self.browser_tabs = BrowserTabs()

    def new_tab(self, url):
        self.browser_tabs.open_tab(url, url)
        print(f"Abriste una nueva pestaña con: {url}")

    def close_tab(self):
        self.browser_tabs.close_current_tab()

    def switch_tab(self, tab_number):
        if self.browser_tabs.switch_to_tab(tab_number):
            current_url = self.browser_tabs.current_tab.url
            print(f"Cambiado a pestaña {tab_number}: {current_url}")
        else:
            print(f"No existe la pestaña {tab_number}")

    def show_tabs(self):
        self.browser_tabs.show_tabs()
