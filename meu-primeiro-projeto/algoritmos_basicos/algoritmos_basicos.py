def converter_temperatura(valor, origem, destino):
	"""Converte uma temperatura entre Celsius, Fahrenheit e Kelvin."""
	unidades = {
		"c": "celsius",
		"celsius": "celsius",
		"f": "fahrenheit",
		"fahrenheit": "fahrenheit",
		"k": "kelvin",
		"kelvin": "kelvin",
	}

	try:
		origem = unidades[origem.lower()]
		destino = unidades[destino.lower()]
	except (AttributeError, KeyError) as erro:
		raise ValueError("Unidade deve ser Celsius, Fahrenheit ou Kelvin") from erro

	if origem == "celsius":
		celsius = valor
	elif origem == "fahrenheit":
		celsius = (valor - 32) * 5 / 9
	else:
		celsius = valor - 273.15

	if destino == "celsius":
		return celsius
	if destino == "fahrenheit":
		return celsius * 9 / 5 + 32
	return celsius + 273.15



def verificar_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


def calcular_media(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    return soma / quantidade if quantidade > 0 else 0


def calcular_mediana(numeros):
  numeros_ordenados = sorted(numeros)
  quantidade = len(numeros_ordenados)
  if quantidade % 2 == 1:
   meio = quantidade // 2
   return numeros_ordenados[meio]


  meio = quantidade // 2
  return (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2


def calcular_moda(numeros):
    frequencias = {}

    for numero in numeros:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1
    moda = max(frequencias, key=frequencias.get)
    return moda
def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Converter temperatura")
        print("2 - Verificar número primo")
        print("3 - Calcular estatísticas")
        print("4 - Testar algoritmos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Programa encerrado.")
            break

        elif opcao == "1":
            valor = float(input("Digite o valor da temperatura: "))
            origem = input("Digite a unidade de origem (Celsius, Fahrenheit ou Kelvin): ")
            destino = input("Digite a unidade de destino (Celsius, Fahrenheit ou Kelvin): ")

            resultado = converter_temperatura(valor, origem, destino)
            print("Resultado:", resultado)

        elif opcao == "2":
            numero = int(input("Digite um número inteiro: "))

            if verificar_primo(numero):
                print(f"{numero} é um número primo.")
            else:
                print(f"{numero} não é um número primo.")

        elif opcao == "3":
            entrada = input("Digite os números separados por espaço: ")
            numeros = [float(numero) for numero in entrada.split()]

            print("Média:", calcular_media(numeros))
            print("Mediana:", calcular_mediana(numeros))
            print("Moda:", calcular_moda(numeros))

        elif opcao == "4":
         testar_algoritmos()

        else:
            print("Opção inválida. Tente novamente.")
def testar_algoritmos():
    print("\n===== TESTES AUTOMÁTICOS =====")
    assert abs(converter_temperatura(0, "Celsius", "Fahrenheit") - 32) < 0.001
    assert abs(converter_temperatura(32, "Fahrenheit", "Celsius") - 0) < 0.001
    assert abs(converter_temperatura(0, "Celsius", "Kelvin") - 273.15) < 0.001
    assert verificar_primo(7) is True
    assert verificar_primo(10) is False
    assert calcular_media([1, 2, 3, 4, 5]) == 3
    assert calcular_mediana([2, 4, 6, 8]) == 5
    assert calcular_moda([2, 4, 4, 6, 6, 6, 8]) == 6
    print("Todos os testes passaram com sucesso!")


menu()   