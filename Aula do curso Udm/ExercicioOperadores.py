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

#formatação de strings com o método format()

a = 'Azao'

b = 'Bzao'

c = 1.1

#a b e c são argumentos passados para o método format
formato = 'a={} b= {} e c= {:2f}'.format(a, b, c) 

print(formato)

#posso usar índices para referenciar os argumentos
formatodois = 'a={0} b= {1} e c= {2:2f}'.format(a, b, c)

print(formatodois)

#parametro nomeado é quando passo o nome do argumento
formatotres = 'a={nome} b= {sobrenome} e c= {valor:2f}'.format(nome=a, sobrenome=b, valor=c)

print(formatotres)

#quando uma funcionalidade é muito usada, ela vira um método
#o método é uma função que "pertence" a um objeto
#o método é chamado usando o operador ponto (.)
#exemplos de métodos: .format(), .upper(), .lower(), .replace(), .find()
#exemplos de objetos: strings, listas, dicionários, tuplas
#exemplos de funções: print(), len(), type(), int(), float(), str()
