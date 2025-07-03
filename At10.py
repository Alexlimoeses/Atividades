from collections import deque

def simular_batata_quente(lista_nomes, num_passes):
    fila = deque(lista_nomes)
    while len(fila) > 1:
        for _ in range(num_passes):
            pessoa = fila.popleft()
            fila.append(pessoa)
        # Remove quem ficou com a batata
        fila.popleft()
    return fila[0]

# Exemplo de uso
if __name__ == "__main__":
    nomes = ["Alice", "Bob", "Charlie", "David", "Eve"]
    num_passes = 3
    vencedor = simular_batata_quente(nomes, num_passes)
    print(f"O vencedor é: {vencedor}")
# Saída esperada: O vencedor é: Charlie (ou outro nome dependendo da ordem inicial
# e do número de passes)
# A ordem dos nomes e o número de passes podem ser ajustados para testar diferentes cenários
# e verificar se a lógica está correta.
