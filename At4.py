# Definindo as vogais
vogais = "aeiouAEIOU"
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# Inicializando contadores
contagem_vogais = 0
contagem_consoantes = 0

# Solicitando ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Iterando sobre cada caractere da frase
for caractere in frase:

    # Verificando se o caractere é uma vogal
    if caractere in vogais:
        contagem_vogais += 1

    # Verificando se o caractere é uma consoante
    elif caractere in consoantes:
        contagem_consoantes += 1

# Exibindo os resultados
print(f"Número de vogais: {contagem_vogais}")
print(f"Número de consoantes: {contagem_consoantes}")

# Desafio Extra: Contar também espaços ou outros tipos de caracteres
contagem_espacos = 0
for caractere in frase:
    if caractere == " ":
        contagem_espacos += 1

print(f"Número de espaços: {contagem_espacos}")

# Desafio Extra: Contar também espaços ou outros tipos de caracteres
contagem_outros = 0

for caractere in frase:
    if caractere not in vogais and caractere not in consoantes and caractere != " ":
        contagem_outros += 1

print(f"Número de outros caracteres: {contagem_outros}")

# Desafio Extra: Contar também espaços ou outros tipos de caracteres
contagem_total = contagem_vogais + contagem_consoantes + contagem_espacos + contagem_outros
print(f"Número total de caracteres: {contagem_total}")
