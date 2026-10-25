"""
visualizacao.py

Funções responsáveis pela exibição dos resultados
das análises de vendas.
"""


def exibir_produtos(produtos: list) -> None:
	"""
	Exibe os produtos cadastrados no sistema.

	Args:
		produtos: Lista de produtos cadastrados.
	"""

	print("\n===== PRODUTOS CADASTRADOS =====")

	if not produtos:
		print("Nenhum produto cadastrado.")
		return

	for indice, produto in enumerate(produtos, start=1):
		print(
			f"{indice}. {produto['nome']} | "
			f"Preço: R$ {produto['preco']:.2f} | "
			f"Estoque: {produto['estoque']}"
		)


def exibir_vendas(vendas: list) -> None:
	"""
	Exibe as vendas registradas no sistema.

	Args:
		vendas: Lista de vendas registradas.
	"""

	print("\n===== VENDAS REGISTRADAS =====")

	if not vendas:
		print("Nenhuma venda registrada.")
		return

	for indice, venda in enumerate(vendas, start=1):
		print(
			f"{indice}. {venda['data']} | "
			f"Produto: {venda['produto']} | "
			f"Quantidade: {venda['quantidade']} | "
			f"Total: R$ {venda['total']:.2f}"
		)


def exibir_analise(
	total_vendas: float,
	quantidade_vendida: int,
	ticket_medio: float,
	produto_mais_vendido: str
) -> None:
	"""
	Exibe os principais resultados da análise de vendas.

	Args:
		total_vendas: Valor total vendido.
		quantidade_vendida: Quantidade total de produtos vendidos.
		ticket_medio: Valor médio das vendas.
		produto_mais_vendido: Produto com maior quantidade vendida.
	"""

	print("\n===== ANÁLISE DE VENDAS =====")

	print(f"Total de vendas: R$ {total_vendas:.2f}")
	print(f"Quantidade vendida: {quantidade_vendida}")
	print(f"Ticket médio: R$ {ticket_medio:.2f}")
	print(f"Produto mais vendido: {produto_mais_vendido}")
