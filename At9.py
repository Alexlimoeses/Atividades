class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Fila:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_data

    def is_empty(self):
        return self.front is None

def novo_cliente(fila, nome_cliente):
    fila.enqueue(nome_cliente)
    print(f"Cliente {nome_cliente} adicionado à fila. Estado atual da fila: {fila_status(fila)}")

def atender_cliente(fila):
    cliente = fila.dequeue()
    if cliente:
        print(f"Atendendo cliente: {cliente}. Estado atual da fila: {fila_status(fila)}")
    else:
        print("Nenhum cliente na fila para atender.")

def fila_status(fila):
    clientes = []
    current = fila.front
    while current:
        clientes.append(current.data)
        current = current.next
    return clientes
# Simulação da fila de atendimento
if __name__ == "__main__":
    fila = Fila()

    # Adicionando clientes à fila
    novo_cliente(fila, "Alice")
    novo_cliente(fila, "Bob")
    novo_cliente(fila, "Charlie")
    novo_cliente(fila, "Diana")

    # Atendendo um cliente
    atender_cliente(fila)

    # Adicionando mais um cliente
    novo_cliente(fila, "Eve")

    # Atendendo todos os clientes restantes
    while not fila.is_empty():
        atender_cliente(fila)
    print("Todos os clientes foram atendidos. A fila está vazia.")
    print(fila_status(fila))
