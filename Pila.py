class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class RequestStack:
    def __init__(self):
        self.top = None  # La pila comienza vacía

    def push_request(self, request):
        """Agregar una nueva solicitud a la pila."""
        new_node = Node(request)
        new_node.next = self.top  # El nuevo nodo apunta al anterior "top"
        self.top = new_node  # Ahora el nuevo nodo es el "top"
        print(f"Solicitud '{request}' agregada a la pila.")

    def process_request(self):
        """Procesar la solicitud en la parte superior de la pila (LIFO)."""
        if self.top:
            print(f"Procesando la solicitud: {self.top.data}")
            self.top = self.top.next  # El nuevo "top" es el siguiente nodo
        else:
            print("No hay más solicitudes para procesar.")

    def show_requests(self):
        """Mostrar las solicitudes pendientes en la pila."""
        if self.top:
            print("Solicitudes pendientes en la pila:")
            current = self.top
            while current:
                print(f"- {current.data}")
                current = current.next
        else:
            print("No hay solicitudes pendientes.")

