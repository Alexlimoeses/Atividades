# Definindo a lista de tarefas
tarefas = []
# Definindo a função para adicionar uma nova tarefa
def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
# Definindo a função para visualizar todas as tarefas
def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")
# Definindo a função para remover uma tarefa
def remover_tarefa():
    tarefa = input("Digite o nome da tarefa a ser removida: ")
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
    else:
        print(f"Tarefa '{tarefa}' não encontrada na lista.")
# Definindo a função para marcar uma tarefa como concluída
def marcar_concluida():
    tarefa = input("Digite o nome da tarefa a ser marcada como concluída: ")
    if tarefa in tarefas:
        index = tarefas.index(tarefa)
        tarefas[index] = f"{tarefa} (concluída)"
        print(f"Tarefa '{tarefa}' marcada como concluída!")
    else:
        print(f"Tarefa '{tarefa}' não encontrada na lista.")
# Definindo a função para salvar a lista de tarefas em um arquivo
def salvar_tarefas():
    with open("tarefas.txt", "w") as file:
        for tarefa in tarefas:
            file.write(tarefa + "\n")
    print("Lista de tarefas salva em 'tarefas.txt'.")
# Definindo a função para carregar a lista de tarefas de um arquivo
def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as file:
            global tarefas
            tarefas = [line.strip() for line in file]
        print("Lista de tarefas carregada com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'tarefas.txt' não encontrado.")
# Função principal para o menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Marcar tarefa como concluída")
        print("5. Salvar tarefas")
        print("6. Carregar tarefas")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            marcar_concluida()
        elif opcao == "5":
            salvar_tarefas()
        elif opcao == "6":
            carregar_tarefas()
        elif opcao == "7":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")
# Executando o menu
if __name__ == "__main__":
    menu()
