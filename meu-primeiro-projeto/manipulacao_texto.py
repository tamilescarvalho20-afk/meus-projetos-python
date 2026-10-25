print("=== MANIPULAÇÃO DE TEXTO ===")

frase = input("Digite uma frase: ")

palavras = frase.split()

print("Quantidade de palavras:", len(palavras))
print("Frase invertida:", frase[::-1])
print("Em maiúsculas:", frase.upper())
print("Em minúsculas:", frase.lower())
print("Capitalizada:", frase.title())

busca = input("Digite uma palavra que deseja procurar: ")

if busca.lower() in frase.lower():
	print("A palavra foi encontrada na frase.")
else:
	print("A palavra não foi encontrada na frase.")
