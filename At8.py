class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def vazia(self):
        return len(self.itens) == 0

    def clear(self):
        self.itens.clear()

class Navegador:
    def __init__(self, pagina_inicial):
        self.historico_voltar = Pilha()
        self.historico_avancar = Pilha()
        self.pagina_atual = pagina_inicial
        print(f"Navegador iniciado em: {self.pagina_atual}")

    def visitar_pagina(self, url):
        self.historico_voltar.push(self.pagina_atual)
        self.pagina_atual = url
        self.historico_avancar.clear()
        print(f"Visitando: {self.pagina_atual}")

    def voltar(self):
        if not self.historico_voltar.vazia():
            self.historico_avancar.push(self.pagina_atual)
            self.pagina_atual = self.historico_voltar.pop()
        print(f"Voltando para: {self.pagina_atual}")

    def avancar(self):
        if not self.historico_avancar.vazia():
            self.historico_voltar.push(self.pagina_atual)
            self.pagina_atual = self.historico_avancar.pop()
        print(f"Avançando para: {self.pagina_atual}")

# Exemplo de uso:
if __name__ == "__main__":
    nav = Navegador("inicio.com")
    nav.visitar_pagina("pagina1.com")
    nav.visitar_pagina("pagina2.com")
    nav.voltar()
    nav.voltar()
