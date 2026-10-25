import statistics

print("=== CALCULADORA DE ESTATÍSTICAS ===")

entrada = input("Digite os números separados por espaço: ")

numeros = [float(numero) for numero in entrada.split()]

media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)
minimo = min(numeros)
maximo = max(numeros)
desvio = statistics.pstdev(numeros)

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Valor mínimo: {minimo:.2f}")
print(f"Valor máximo: {maximo:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
