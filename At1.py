import unicodedata
def remover_acentos(frase):
    # Normaliza a string e remove acentuação
    frase = unicodedata.normalize('NFD', frase)
    frase = frase.encode('ascii', 'ignore').decode('utf-8')
    return frase

def eh_palindromo(frase):
    # Remove espaços e converte para minúsculas
    frase = frase.replace(" ", "").lower()
    
    # Verifica se a frase é igual à sua inversa
    if frase == frase[::-1]:
        return True
    else:
        return False
    
# Solicita ao usuário para digitar uma palavra ou frase
frase = input("Digite uma palavra ou frase: ")

# Remove acentuação
frase_sem_acentos = remover_acentos(frase)

# Verifica se é um palíndromo
if eh_palindromo(frase_sem_acentos):
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")
