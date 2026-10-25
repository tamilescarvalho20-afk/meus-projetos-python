"""
modelo.py

Define as estruturas de dados utilizadas pelo sistema
de análise de vendas.
"""

import json


# Lista que armazenará os produtos cadastrados
produtos = []

# Lista que armazenará as vendas realizadas
vendas = []


def adicionar_produto(nome: str, preco: float, estoque: int) -> dict:
	"""
	Cria um novo produto e adiciona à lista de produtos.

	Args:
		nome: Nome do produto.
		preco: Preço unitário do produto.
		estoque: Quantidade disponível em estoque.

	Returns:
		Dicionário contendo os dados do produto.
	"""

	produto = {
		"nome": nome,
		"preco": preco,
		"estoque": estoque
	}

	produtos.append(produto)

	return produto


def registrar_venda(
	produto: str,
	quantidade: int,
	valor_unitario: float,
	data: str
) -> dict:
	"""
	Registra uma nova venda.

	Args:
		produto: Nome do produto vendido.
		quantidade: Quantidade vendida.
		valor_unitario: Preço de cada unidade.
		data: Data da venda.

	Returns:
		Dicionário contendo os dados da venda.
	"""

	venda = {
		"produto": produto,
		"quantidade": quantidade,
		"valor_unitario": valor_unitario,
		"total": quantidade * valor_unitario,
		"data": data
	}

	vendas.append(venda)

	return venda


def salvar_dados() -> None:
	"""
	Salva produtos e vendas em um arquivo JSON.
	"""

	dados = {
		"produtos": produtos,
		"vendas": vendas
	}

	with open("dados.json", "w", encoding="utf-8") as arquivo:
		json.dump(
			dados,
			arquivo,
			ensure_ascii=False,
			indent=4
		)


def carregar_dados() -> None:
	"""
	Carrega produtos e vendas do arquivo JSON.
	"""

	try:
		with open("dados.json", "r", encoding="utf-8") as arquivo:
			dados = json.load(arquivo)

			produtos.clear()
			vendas.clear()

			produtos.extend(dados.get("produtos", []))
			vendas.extend(dados.get("vendas", []))

	except FileNotFoundError:
		pass

	except json.JSONDecodeError:
		print("Aviso: o arquivo dados.json está inválido.")
