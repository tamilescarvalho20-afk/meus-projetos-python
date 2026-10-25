def converter_temperatura(valor, origem, destino):
	origem = origem.upper()
	destino = destino.upper()

	# Primeiro converte a temperatura para Celsius
	if origem == "C":
		celsius = valor
	elif origem == "F":
		celsius = (valor - 32) * 5 / 9
	elif origem == "K":
		celsius = valor - 273.15
	else:
		raise ValueError("Unidade de origem inválida.")

	# Depois converte de Celsius para a unidade desejada
	if destino == "C":
		return celsius
	elif destino == "F":
		return (celsius * 9 / 5) + 32
	elif destino == "K":
		return celsius + 273.15
	else:
		raise ValueError("Unidade de destino inválida.")
