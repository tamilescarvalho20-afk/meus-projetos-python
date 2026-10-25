"""
main.py

Programa principal do sistema de análise de dados de vendas.
"""

from datetime import datetime

from modelo import (
	produtos,
	vendas,
	adicionar_produto,
	registrar_venda,
	salvar_dados,
	carregar_dados,
)

from processamento import (
	calcular_total_vendas,
	calcular_quantidade_vendida,
	calcular_ticket_medio,
	produto_mais_vendido,
	filtrar_por_periodo,
)

from visualizacao import (
	exibir_produtos,
	exibir_vendas,
	exibir_analise,
)


def cadastrar_produto() -> None:
	"""Solicita os dados de um produto e realiza seu cadastro."""
	print("\n===== CADASTRO DE PRODUTO =====")
	try:
		nome = input("Nome do produto: ").strip()
		if not nome:
			print("\nErro: o nome do produto não pode ficar vazio.")
			return
		preco = float(input("Preço do produto: R$ ").replace(",", "."))
		if preco <= 0:
			print("\nErro: o preço deve ser maior que zero.")
			return
		estoque = int(input("Quantidade em estoque: "))
		if estoque < 0:
			print("\nErro: o estoque não pode ser negativo.")
			return
		adicionar_produto(nome, preco, estoque)
		salvar_dados()
		print("\nProduto cadastrado com sucesso!")
	except ValueError:
		print("\nErro: digite valores válidos.")


def cadastrar_venda() -> None:
	"""Solicita os dados e registra uma nova venda."""
	print("\n===== REGISTRO DE VENDA =====")
	try:
		produto = input("Nome do produto: ").strip()
		if not produto:
			print("\nErro: informe o nome do produto.")
			return
		produto_encontrado = next(
			(item for item in produtos if item["nome"].lower() == produto.lower()),
			None,
		)
		if produto_encontrado is None:
			print("\nErro: produto não encontrado.")
			return
		quantidade = int(input("Quantidade vendida: "))
		if quantidade <= 0:
			print("\nErro: a quantidade deve ser maior que zero.")
			return
		if quantidade > produto_encontrado["estoque"]:
			print("\nErro: quantidade maior que o estoque disponível.")
			return
		valor_unitario = float(input("Valor unitário: R$ ").replace(",", "."))
		if valor_unitario <= 0:
			print("\nErro: o valor deve ser maior que zero.")
			return
		data = input("Data da venda (DD/MM/AAAA): ").strip()
		datetime.strptime(data, "%d/%m/%Y")
		registrar_venda(produto_encontrado["nome"], quantidade, valor_unitario, data)
		produto_encontrado["estoque"] -= quantidade
		salvar_dados()
		print("\nVenda registrada com sucesso!")
	except ValueError:
		print("\nErro: informe valores válidos e uma data no formato DD/MM/AAAA.")


def mostrar_analise() -> None:
	"""Calcula e exibe os principais indicadores de vendas."""
	exibir_analise(
		calcular_total_vendas(vendas),
		calcular_quantidade_vendida(vendas),
		calcular_ticket_medio(vendas),
		produto_mais_vendido(vendas),
	)


def mostrar_analise_periodo() -> None:
	"""Exibe a análise das vendas de um período específico."""
	print("\n===== ANÁLISE POR PERÍODO =====")
	data_inicial = input("Data inicial (DD/MM/AAAA): ").strip()
	data_final = input("Data final (DD/MM/AAAA): ").strip()
	try:
		vendas_periodo = filtrar_por_periodo(vendas, data_inicial, data_final)
		if not vendas_periodo:
			print("\nNenhuma venda encontrada nesse período.")
			return
		exibir_analise(
			calcular_total_vendas(vendas_periodo),
			calcular_quantidade_vendida(vendas_periodo),
			calcular_ticket_medio(vendas_periodo),
			produto_mais_vendido(vendas_periodo),
		)
	except ValueError:
		print("\nErro: informe datas válidas no formato DD/MM/AAAA.")


def menu() -> None:
	"""Exibe o menu principal do sistema."""
	carregar_dados()
	while True:
		print("\n==============================")
		print(" SISTEMA DE ANÁLISE DE DADOS")
		print("==============================")
		print("1 - Cadastrar produto")
		print("2 - Registrar venda")
		print("3 - Exibir produtos")
		print("4 - Exibir vendas")
		print("5 - Exibir análise")
		print("6 - Análise por período")
		print("0 - Sair")
		print("==============================")
		opcao = input("Escolha uma opção: ")
		if opcao == "1":
			cadastrar_produto()
		elif opcao == "2":
			cadastrar_venda()
		elif opcao == "3":
			exibir_produtos(produtos)
		elif opcao == "4":
			exibir_vendas(vendas)
		elif opcao == "5":
			mostrar_analise()
		elif opcao == "6":
			mostrar_analise_periodo()
		elif opcao == "0":
			salvar_dados()
			print("\nDados salvos com sucesso.")
			print("Programa encerrado.")
			break
		else:
			print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
	menu()
