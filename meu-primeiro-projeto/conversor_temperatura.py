print("CONVERSOR DE TEMPERATURA")

print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == "1":
	celsius = float(input("Digite a temperatura em Celsius: "))
	fahrenheit = (celsius * 9 / 5) + 32
	print("Temperatura em Fahrenheit:", fahrenheit)

elif opcao == "2":
	fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
	celsius = (fahrenheit - 32) * 5 / 9
	print("Temperatura em Celsius:", celsius)

else:
	print("Opção inválida.")
