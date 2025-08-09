import datetime
import unittest
import sys
from collections import deque

class Produto:
    def __init__(self, codigo, nome, fabricante, quantidade, preco, dias_manutencao):
        self.codigo = int(codigo)
        self.nome = str(nome)
        self.fabricante = str(fabricante)
        self.quantidade = int(quantidade)
        self.preco = float(preco)
        self.dias_manutencao = int(dias_manutencao)
        self.data_venda = None

    def __repr__(self):
        """Representação em string do objeto, para facilitar a impressão."""
        return f"Cód: {self.codigo} | Nome: {self.nome} | Qtd: {self.quantidade} | Preço: R${self.preco:.2f}"

class No:
    """Nó da Árvore Binária de Busca."""
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class ArvoreProdutos:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = No(produto)
            
        else:
            self._inserir_recursivo(produto, self.raiz)

    def _inserir_recursivo(self, produto, no_atual):
        if produto.codigo < no_atual.produto.codigo:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(produto)
                
            else:
                self._inserir_recursivo(produto, no_atual.esquerda)
                
        elif produto.codigo > no_atual.produto.codigo:
            if no_atual.direita is None:
                no_atual.direita = No(produto)
                
            else:
                self._inserir_recursivo(produto, no_atual.direita)

    def buscar(self, codigo):
        """Busca um produto na árvore pelo código."""
        return self._buscar_recursivo(codigo, self.raiz)

    def _buscar_recursivo(self, codigo, no_atual):
        """Método auxiliar recursivo para a busca."""
        if no_atual is None or no_atual.produto.codigo == codigo:
            return no_atual.produto if no_atual else None
        
        elif codigo < no_atual.produto.codigo:
            return self._buscar_recursivo(codigo, no_atual.esquerda)
        
        else:
            return self._buscar_recursivo(codigo, no_atual.direita)

    def listar_em_ordem(self):
        """Retorna uma lista de produtos em ordem de código (percurso in-order)."""
        if self.raiz:
            return self._listar_em_ordem_recursivo(self.raiz)
        return []

    def _listar_em_ordem_recursivo(self, no_atual):
        """Método auxiliar recursivo que realiza o percurso in-order."""
        res = []
        if no_atual.esquerda:
            res.extend(self._listar_em_ordem_recursivo(no_atual.esquerda))
        res.append(no_atual.produto)
        
        if no_atual.direita:
            res.extend(self._listar_em_ordem_recursivo(no_atual.direita))
            
        return res

class Inventario:
    """
    Classe central que gerencia todo o inventário, utilizando as estruturas
    de dados apropriadas para cada tarefa.
    """
    def __init__(self):
        self.produtos_hash = {}
        self.produtos_arvore = ArvoreProdutos()
        self.historico_operacoes = deque(maxlen=10)
        self.fila_manutencao = deque()

    def adicionar_produto(self, produto):
        if produto.codigo not in self.produtos_hash:
            self.produtos_hash[produto.codigo] = produto
            self.produtos_arvore.inserir(produto)
            self.historico_operacoes.append(('add', produto.codigo))
            print(f"\nProduto '{produto.nome}' adicionado com sucesso!")
            
        else:
            print(f"\nErro: O código {produto.codigo} já está em uso.")

    def buscar_produto_por_codigo(self, codigo):
        return self.produtos_arvore.buscar(codigo)

    def listar_produtos(self, ordenado_por='codigo'):
        produtos_lista = list(self.produtos_hash.values())
        if ordenado_por == 'nome':
            return sorted(produtos_lista, key=lambda p: p.nome)
        
        elif ordenado_por == 'quantidade':
            return sorted(produtos_lista, key=lambda p: p.quantidade)
        
        else:
            return self.produtos_arvore.listar_em_ordem()

    def registrar_venda(self, codigo, quantidade):
        produto = self.produtos_hash.get(codigo)
        if produto and produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            produto.data_venda = datetime.date.today()
            print(f"\n Venda de {quantidade} unidade(s) de '{produto.nome}' registrada.")
            self._agendar_manutencao(produto)
        else:
            print("\n Erro: Produto não encontrado ou quantidade insuficiente em estoque.")

    def _agendar_manutencao(self, produto):
        if produto.data_venda and produto.dias_manutencao > 0:
            data_manutencao = produto.data_venda + datetime.timedelta(days=produto.dias_manutencao)
            # Adiciona na fila (FIFO)
            self.fila_manutencao.append((produto, data_manutencao))
            print(f" Manutenção para '{produto.nome}' agendada para {data_manutencao}.")

    def proxima_manutencao(self):
        """Processa o próximo item da fila de manutenção."""
        if self.fila_manutencao:
            return self.fila_manutencao.popleft()
        return None
    
def exibir_menu():
    """Imprime o menu de opções para o usuário."""
    print("\n--- Sistema de Estoque de Ferramentas Elétricas ---")
    print("1. Adicionar Produto")
    print("2. Listar Produtos (por Código)")
    print("3. Listar Produtos (por Nome)")
    print("4. Buscar Produto por Código")
    print("5. Registrar Venda")
    print("6. Ver Próxima Manutenção Agendada")
    print("7. Sair")
    return input("Escolha uma opção: ")

def loop_principal(inventario):
    """Executa o loop principal da aplicação."""
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            try:
                codigo = int(input("Código: "))
                nome = input("Nome: ")
                fabricante = input("Fabricante: ")
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: "))
                dias_manutencao = int(input("Dias p/ manutenção (0 se não aplicável): "))
                produto = Produto(codigo, nome, fabricante, quantidade, preco, dias_manutencao)
                inventario.adicionar_produto(produto)
                
            except ValueError:
                print("\nErro: Entrada inválida. Por favor, verifique os valores.")

        elif opcao == '2':
            print("\n--- Lista de Produtos (por Código) ---")
            for p in inventario.listar_produtos(ordenado_por='codigo'):
                print(p)

        elif opcao == '3':
            print("\n--- Lista de Produtos (por Nome) ---")
            for p in inventario.listar_produtos(ordenado_por='nome'):
                print(p)

        elif opcao == '4':
            try:
                codigo = int(input("Digite o código do produto: "))
                produto = inventario.buscar_produto_por_codigo(codigo)
                print("\n--- Produto Encontrado ---")
                print(produto) if produto else print("Produto não encontrado.")
            except ValueError:
                print("\n Erro: Código inválido.")

        elif opcao == '5':
            try:
                codigo = int(input("Código do produto vendido: "))
                quantidade = int(input("Quantidade vendida: "))
                inventario.registrar_venda(codigo, quantidade)
            except ValueError:
                print("\ Erro: Entrada inválida.")

        elif opcao == '6':
            print("\n--- Fila de Manutenção ---")
            proxima = inventario.proxima_manutencao()
            if proxima:
                produto, data = proxima
                print(f"Próxima manutenção a ser contatada: '{produto.nome}' (Vendido em {produto.data_venda}) -> Agendar para {data}")
            else:
                print("Nenhuma manutenção na fila.")

        elif opcao == '7':
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

class TestInventario(unittest.TestCase):
    def setUp(self):
        """Configura um ambiente limpo para cada teste."""
        self.inventario = Inventario()
        self.p1 = Produto(101, "Parafusadeira", "Marca X", 10, 150.00, 365)
        self.p2 = Produto(205, "Martelo Rompedor", "Marca Y", 5, 800.00, 180)
        self.p3 = Produto(152, "Lixadeira", "Marca Z", 8, 200.00, 0)
        self.inventario.adicionar_produto(self.p1)
        self.inventario.adicionar_produto(self.p2)
        self.inventario.adicionar_produto(self.p3)

    def test_adicao_e_busca(self):
        """Testa se os produtos são adicionados e podem ser buscados corretamente."""
        self.assertIsNotNone(self.inventario.buscar_produto_por_codigo(101))
        self.assertEqual(self.inventario.buscar_produto_por_codigo(205).nome, "Martelo Rompedor")
        self.assertIsNone(self.inventario.buscar_produto_por_codigo(999))

    def test_registro_de_venda_e_fila_manutencao(self):
        """Testa a baixa no estoque e o agendamento na fila de manutenção."""
        self.inventario.registrar_venda(101, 1)
        self.assertEqual(self.inventario.produtos_hash[101].quantidade, 9)
        self.assertEqual(len(self.inventario.fila_manutencao), 1)
        # Testa venda de produto sem manutenção
        self.inventario.registrar_venda(152, 2)
        self.assertEqual(self.inventario.produtos_hash[152].quantidade, 6)
        self.assertEqual(len(self.inventario.fila_manutencao), 1) # Fila não deve aumentar

    def test_ordenacao_por_nome(self):
        """Testa a funcionalidade de ordenação da lista de produtos."""
        lista_ordenada = self.inventario.listar_produtos(ordenado_por='nome')
        self.assertEqual(lista_ordenada[0].codigo, 152) # Lixadeira
        self.assertEqual(lista_ordenada[1].codigo, 205) # Martelo Rompedor
        self.assertEqual(lista_ordenada[2].codigo, 101) # Parafusadeira

if __name__ == "__main__":
    # Verifica se o script foi chamado com o argumento 'test'
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'test':
        print("Executando suíte de testes...\n")
        # Ignora o argumento 'test' para o unittest e executa os testes
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        # Se não, executa o programa principal
        inventario_principal = Inventario()
        # Populando com alguns dados para demonstração
        inventario_principal.adicionar_produto(Produto(101, "Furadeira de Impacto", "Marca A", 15, 299.90, 180))
        inventario_principal.adicionar_produto(Produto(205, "Serra Circular", "Marca B", 8, 549.50, 365))
        inventario_principal.adicionar_produto(Produto(152, "Lixadeira Orbital", "Marca A", 20, 199.00, 0))
        loop_principal(inventario_principal)
