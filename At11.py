class FilaDePrioridade:
    def __init__(self):
        self.fila = []

    def enqueue(self, dado, prioridade):
        # Insere o item na fila com base na prioridade
        self.fila.append((dado, prioridade))
        self.fila.sort(key=lambda x: x[1])  # Ordena pela prioridade

    def dequeue(self):
        # Remove e retorna o item com a maior prioridade
        if self.fila:
            return self.fila.pop(0)[0]
        return None

    def is_empty(self):
        # Verifica se a fila está vazia
        return len(self.fila) == 0
    def peek(self):
        # Retorna o item com a maior prioridade sem removê-lo
        if self.fila:
            return self.fila[0][0]
        return None
    def size(self):
        # Retorna o número de itens na fila
        return len(self.fila)
    def __str__(self):
        # Retorna uma representação da fila
        return ', '.join(f"{dado} (Prioridade: {prioridade})" for dado, prioridade in self.fila)
    
# Exemplo de uso da classe FilaDePrioridade
if __name__ == "__main__":
    fila = FilaDePrioridade()
    fila.enqueue("Relatório Urgente", 1)
    fila.enqueue("Documento Normal", 5)
    fila.enqueue("E-mail Rápido", 2)

    print(fila)  # Exibe a fila com prioridades
    print(fila.dequeue())  # Deve retornar "Relatório Urgente"
    print(fila)  # Exibe a fila após o dequeue
    print(fila.peek())  # Deve retornar "E-mail Rápido"
    print(fila.size())  # Deve retornar o tamanho da fila
    print(fila.is_empty())  # Deve retornar False
    fila.dequeue()  # Remove "E-mail Rápido"
    print(fila)  # Exibe a fila após o segundo dequeue
    fila.dequeue()  # Remove "Documento Normal"
    print(fila.is_empty())  # Deve retornar True após remover todos os itens
    print(fila)  # Exibe a fila vazia
    fila.dequeue()  # Deve retornar None, pois a fila está vazia
    print(fila.peek())  # Deve retornar None, pois a fila está vazia
    print(fila.size())  # Deve retornar 0, pois a fila está vazia
    
    
