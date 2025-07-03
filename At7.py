class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        raise IndexError("Pilha vazia")

    def size(self):
        return len(self.itens)
def inverter_string(texto):
    pilha = Pilha()
    
    # Adiciona cada caractere à pilha
    for char in texto:
        pilha.push(char)
    
    # Constrói a string invertida
    texto_invertido = ""
    while not pilha.is_empty():
        texto_invertido += pilha.pop()
    
    return texto_invertido
# Testando a função
if __name__ == "__main__":
    entrada = "Python"
    saida = inverter_string(entrada)
    print(f"Entrada: {entrada}")
    print(f"Saída: {saida}")  

