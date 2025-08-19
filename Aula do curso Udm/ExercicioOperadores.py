#Exercicio de calculo de IMC

nome = "Fernanda"
altura = 1.73
peso = 75.2
#imc = ... (os 3 pontos indicam que você deve completar a linha, são chamados de "placeholders")
imc = peso / (altura ** 2)

print(nome, "tem", altura, "de altura, pesa", peso, "kg e seu IMC é", imc)

#formatação de strings

#f-strings significa "formatted string literals"
#f-strings são strings que permitem incluir expressões dentro de chaves {}


linha1 = f"Nome: {nome} tem {altura:.2f} de altura,"
linha2 = f"pesa {peso} kg e seu IMC é"
linha3 = f"{imc:.2f}"

print(linha1, linha2, linha3)