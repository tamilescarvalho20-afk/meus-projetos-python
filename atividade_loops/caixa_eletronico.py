saldo = 500.00

while True:
	print("\n=== CAIXA ELETRÔNICO ===")
	print("1 - Verificar saldo")
	print("2 - Realizar saque")
	print("3 - Sair")

	opcao = input("Escolha uma opção: ")

	if opcao == "1":
		print(f"Seu saldo é: R$ {saldo:.2f}")

	elif opcao == "2":
		valor = float(input("Digite o valor do saque: R$ "))

		if valor <= 0:
			print("O valor do saque deve ser maior que zero.")
		elif valor > saldo:
			print("Saldo insuficiente.")
		else:
			saldo -= valor
			print("Saque realizado com sucesso!")
			print(f"Seu novo saldo é: R$ {saldo:.2f}")

	elif opcao == "3":
		print("Sistema encerrado. Obrigado!")
		break

	else:
		print("Opção inválida. Tente novamente.")
