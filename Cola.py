class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class RequestQueue:
    def __init__(self):
        self.front = None  # Apunta al primer nodo (frente de la cola)
        self.rear = None   # Apunta al último nodo (final de la cola)

    def is_empty(self):
        """Verifica si la cola está vacía"""
        return self.front is None

    def enqueue_request(self, request):
        """Agregar una nueva solicitud a la cola."""
        new_node = Node(request)
        if self.rear:  # Si ya hay elementos en la cola
            self.rear.next = new_node
        self.rear = new_node  # El nuevo nodo es el final de la cola
        if not self.front:  # Si la cola estaba vacía, el frente es también el nuevo nodo
            self.front = new_node
        print(f"Solicitud '{request}' agregada a la cola.")

    def process_request(self):
        """Procesar la primera solicitud en la cola (FIFO)."""
        if self.front:
            data = self.front.data
            print(f"Procesando la solicitud: {data}")
            self.front = self.front.next  # El frente de la cola avanza al siguiente nodo
            if not self.front:  # Si la cola queda vacía, rear también debe ser None
                self.rear = None
            return data
        else:
            print("No hay más solicitudes para procesar.")
            return None

    def show_requests(self):
        """Mostrar las solicitudes pendientes en la cola."""
        if self.front:
            print("Solicitudes pendientes en la cola:")
            current = self.front
            count = 1
            while current:
                print(f"{count}. {current.data}")
                current = current.next
                count += 1
        else:
            print("No hay solicitudes pendientes.")

    def cancel_request(self, index):
        """Cancela una solicitud específica por su índice"""
        if self.is_empty():
            return False
        
        if index == 1:
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return True

        current = self.front
        count = 1
        while current and count < index - 1:
            current = current.next
            count += 1

        if current and current.next:
            current.next = current.next.next
            if not current.next:
                self.rear = current
            return True
        
        return False



