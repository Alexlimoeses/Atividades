numero = input("Diga um número: ")
def tabuada(numero):
    for i in range(1, 10):
        print(f"{numero} x {i} = {int(numero) * i}")
tabuada(numero)
