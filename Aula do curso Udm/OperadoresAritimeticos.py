#Operadores matemáticos

adicao = 10 + 5
print("Adição:", adicao)

subtracao = 10 - 5
print("Subtração:", subtracao)

multiplicacao = 10 * 5
print("Multiplicação:", multiplicacao)

divisao = 10 / 3 #vai sempre retornar um float, mesmo que o resultado seja inteiro
print("Divisão:", divisao)

divisao_inteira = 10 // 3 #retorna o inteiro da divisão, ou seja, o resultado da divisão sem a parte decimal
print("Divisão inteira:", divisao_inteira)

exponenciacao = 2 ** 3 #2 elevado a 3, ou seja, 2 * 2 * 2
print("Exponenciação:", exponenciacao)  

modulo = 10 % 3 #retorna o resto da divisão, ou seja, o que sobra quando 10 é dividido por 3, 10 dividido por 3 é 3, com resto 1, então o resultado é 1
print("Módulo:", modulo) #Serve para definir numeros pares e ímpares. 


print(10 % 3 == 0) #verifica se 10 é divisível por 3, o resultado é False, pois 10 não é divisível por 3

print(10 % 2 == 0) #verifica se 10 é divisível por 2, o resultado é True, pois 10 é divisível por 2 


concatenacao = "10" + "5" #concatena duas strings, o resultado é "105"
print("Concatenação:", concatenacao) 

a_vezes_b = 10 * "a" #repete a string "a" 10 vezes, o resultado é "aaaaaaaaaa"
print("Repetição:", a_vezes_b)

vezes_nome = 9 * "Fernanda " #repete a string "Fernanda" 9 vezes, o resultado é "FernandaFernandaFernandaFernandaFernandaFernandaFernandaFernandaFernanda"
print("Repetição do nome:", vezes_nome)

#Precedencia dos operadores
#1 - Parênteses 
#2 - Exponenciação
#3 - Multiplicação, Divisão, Divisão inteira e Módulo
#4 - Adição e Subtração

print('Achar o resultado: 1024 ')

conta = 1 + 1 ** 5 + 5  #A exponenciação é resolvida primeiro, depois a adição, o resultado é 1 + 1 + 5 = 7
print("Resultado da conta:", conta) #a exponenciação é resolvida primeiro, então 1 ** 5 = 1, depois a adição é feita, então o resultado final é 7 

conta2 = (1 + 1) ** 5 + 5 #Aqui, a adição dentro dos parênteses é resolvida primeiro, então 1 + 1 = 2, depois a exponenciação é feita, então 2 ** 5 = 32, e por fim a adição com 5 é feita, resultando em 32 + 5 = 37
print("Resultado da conta 2:", conta2)  # A exponenciação é resolvida depois da adição dentro dos parênteses, então o resultado final é 37

conta3 = (1 + 1) ** (5 + 5) #Aqui, a adição dentro dos parênteses é resolvida primeiro, então 1 + 1 = 2, depois a adição dentro dos parênteses da exponenciação é resolvida, então 5 + 5 = 10, e por fim a exponenciação é feita, então 2 ** 10 = 1024
print("Resultado da conta 3:", conta3) #O resultado final é 1024 