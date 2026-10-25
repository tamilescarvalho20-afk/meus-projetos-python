from datetime import datetime

nome = input("Digite seu nome: ")

hora = datetime.now().hour

if hora < 12:
	saudacao = "Bom dia"
elif hora < 18:
	saudacao = "Boa tarde"
else:
	saudacao = "Boa noite"

print(saudacao + ", " + nome + "!")
