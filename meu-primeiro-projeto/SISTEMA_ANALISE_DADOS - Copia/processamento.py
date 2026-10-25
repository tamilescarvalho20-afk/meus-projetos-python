"""
processamento.py

Contém as funções responsáveis pelo processamento
e análise dos dados de vendas.
"""

from datetime import datetime


def calcular_total_vendas(vendas: list) -> float:
    """
    Calcula o valor total das vendas.

    Args:
        vendas: Lista contendo os registros de vendas.

    Returns:
        Valor total das vendas.
    """

    total = 0.0

    for venda in vendas:
        total += venda["total"]

    return total


def calcular_quantidade_vendida(vendas: list) -> int:
    """
    Calcula a quantidade total de produtos vendidos.

    Args:
        vendas: Lista contendo os registros de vendas.

    Returns:
        Quantidade total de produtos vendidos.
    """

    quantidade_total = 0

    for venda in vendas:
        quantidade_total += venda["quantidade"]

    return quantidade_total


def calcular_ticket_medio(vendas: list) -> float:
    """
    Calcula o valor médio das vendas.

    Args:
        vendas: Lista contendo os registros de vendas.

    Returns:
        Ticket médio das vendas.
    """

    if not vendas:
        return 0.0

    total = calcular_total_vendas(vendas)

    return total / len(vendas)


def produto_mais_vendido(vendas: list) -> str:
    """
    Identifica o produto com maior quantidade de unidades vendidas.

    Args:
        vendas: Lista contendo os registros de vendas.

    Returns:
        Nome do produto mais vendido.
    """

    if not vendas:
        return "Nenhuma venda registrada."

    quantidade_produtos = {}

    for venda in vendas:
        produto = venda["produto"]
        quantidade = venda["quantidade"]

        if produto in quantidade_produtos:
            quantidade_produtos[produto] += quantidade
        else:
            quantidade_produtos[produto] = quantidade

    produto_maior = max(
        quantidade_produtos,
        key=quantidade_produtos.get
    )

    return produto_maior


def filtrar_por_periodo(
    vendas: list,
    data_inicial: str,
    data_final: str
) -> list:
    """
    Filtra as vendas realizadas dentro de um período.

    Args:
        vendas: Lista contendo os registros de vendas.
        data_inicial: Data inicial no formato DD/MM/AAAA.
        data_final: Data final no formato DD/MM/AAAA.

    Returns:
        Lista contendo somente as vendas do período informado.

    Raises:
        ValueError: Caso as datas sejam inválidas ou a data inicial
        seja posterior à data final.
    """

    inicio = datetime.strptime(data_inicial, "%d/%m/%Y")
    fim = datetime.strptime(data_final, "%d/%m/%Y")

    if inicio > fim:
        raise ValueError(
            "A data inicial não pode ser posterior à data final."
        )

    vendas_filtradas = []

    for venda in vendas:
        data_venda = datetime.strptime(
            venda["data"],
            "%d/%m/%Y"
        )

        if inicio <= data_venda <= fim:
            vendas_filtradas.append(venda)

    return vendas_filtradas
