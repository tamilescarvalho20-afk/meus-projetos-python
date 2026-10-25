"""Calculadora simples com as quatro operações básicas."""

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)

if numero2 != 0:
    divisao = numero1 / numero2
    print("Divisão:", divisao)
else:
    print("Não é possível dividir por zero.")