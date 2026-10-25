print("=== TIPOS DE DADOS NA PRÁTICA ===")

# Tipos básicos
idade = 30
altura = 1.60
nome = "Tamiles"
estudando_python = True

print("Idade:", idade, "- Tipo:", type(idade))
print("Altura:", altura, "- Tipo:", type(altura))
print("Nome:", nome, "- Tipo:", type(nome))
print("Estudando Python:", estudando_python, "- Tipo:", type(estudando_python))

# Conversão explícita
numero_texto = "10"
numero = int(numero_texto)

print("Texto:", numero_texto, "- Tipo:", type(numero_texto))
print("Convertido:", numero, "- Tipo:", type(numero))

# Conversão de inteiro para decimal
valor_inteiro = 20
valor_decimal = float(valor_inteiro)

print("Inteiro:", valor_inteiro)
print("Convertido para float:", valor_decimal)

# Conversão implícita
resultado = 10 + 2.5

print("Resultado:", resultado)
print("Tipo do resultado:", type(resultado))
