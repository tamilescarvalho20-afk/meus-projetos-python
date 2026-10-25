print("=== REGISTRO DE DESPESAS ===")

categoria = input("Digite a categoria da despesa: ")
descricao = input("Digite a descrição da despesa: ")
valor = float(input("Digite o valor da despesa: R$ "))
data = input("Digite a data da despesa (DD/MM/AAAA): ")

despesa = {
	"categoria": categoria,
	"descricao": descricao,
	"valor": valor,
	"data": data,
}

print("\n=== DESPESA REGISTRADA ===")
print("Categoria:", despesa["categoria"])
print("Descrição:", despesa["descricao"])
print(f'Valor: R$ {despesa["valor"]:.2f}')
print("Data:", despesa["data"])
