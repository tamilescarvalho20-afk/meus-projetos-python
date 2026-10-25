print("=== CONVERSOR DE TEMPERATURA ===")

print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")

opcao = input("Escolha uma opção de 1 a 6: ")

if opcao == "1":
	celsius = float(input("Digite a temperatura em Celsius: "))
	fahrenheit = (celsius * 9 / 5) + 32
	print(f"Resultado: {fahrenheit:.2f} °F")

elif opcao == "2":
	celsius = float(input("Digite a temperatura em Celsius: "))
	kelvin = celsius + 273.15
	print(f"Resultado: {kelvin:.2f} K")

elif opcao == "3":
	fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
	celsius = (fahrenheit - 32) * 5 / 9
	print(f"Resultado: {celsius:.2f} °C")

elif opcao == "4":
	fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
	celsius = (fahrenheit - 32) * 5 / 9
	kelvin = celsius + 273.15
	print(f"Resultado: {kelvin:.2f} K")

elif opcao == "5":
	kelvin = float(input("Digite a temperatura em Kelvin: "))
	celsius = kelvin - 273.15
	print(f"Resultado: {celsius:.2f} °C")

elif opcao == "6":
	kelvin = float(input("Digite a temperatura em Kelvin: "))
	celsius = kelvin - 273.15
	fahrenheit = (celsius * 9 / 5) + 32
	print(f"Resultado: {fahrenheit:.2f} °F")

else:
	print("Opção inválida.")
