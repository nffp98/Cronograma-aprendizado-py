"""
Introdução aos tipos de dados

Tipo de tipagem = dinâmica/Forte
 Tipos de dados primitivos
 int, float, bool, str

"""

print(123) #ele detecta que é um inteiro
print(12.3) #ele detecta que é um float
print(True) #ele detecta que é um booleano
print("Olá, mundo!") #ele detecta que é uma string


"""
Para strings, podemos usar aspas simples ou duplas"""
print('Olá, mundo!') #aspas simples
print("Olá, mundo!") #aspas duplas    

# Escape = \
print('Ele disse: "Olá, mundo!"') #aspas duplas dentro de aspas simples
print("Ele disse: \"Olá, mundo!\"") #aspas duplas com escape 
print('Ele disse: \'Olá, mundo!\'') #aspas simples com escape

# r

print(r'Ele disse: "Olá, mundo!"') #raw string, não interpreta escape
print(r"Ele disse: \"Olá, mundo!\"") #raw string, não interpreta escape

# Escape e r geralmente não são muito usados juntos, pois o r já ignora os escapes. 
# Pra facilitar pode se usar aspas duplas dentro de aspas simples ou vice-versa.

print("Ele disse: 'Olá, mundo!'") #aspas simples dentro de aspas duplas
print('Ele disse: "Olá, mundo!"') #aspas duplas dentro de aspas simples


#Tipos de int e float

# Inteiros
numero_inteiro = 9
print("Número inteiro:", numero_inteiro) 


# Float
numero_float = 10.5
print("Número float:", numero_float)

#Na programação se usa o ponto para separar a parte inteira da parte decimal.

# A funcão type() retorna o tipo de dado de uma variável. 
print("Tipo de dado de numero_inteiro:", type(numero_inteiro))  

#Tudo em python é um objeto, inclusive os tipos de dados primitivos. 

print('a entrada é',type(1))
print('a entrada é',type('-1.1'))
print('a entrada é',type(2.5)) 

# Booleanos

#True e False são escritos em inglês, com a primeira letra maiúscula.
verdadeiro = True
falso = False
print("Verdadeiro:", verdadeiro)
print("Falso:", falso)
# A função type() também pode ser usada para verificar o tipo de um booleano
print("Tipo de dado de verdadeiro:", type(verdadeiro))


print(10==10) # True, pois 10 é igual a 10 
print(10==20) # False, pois 10 não é igual a 20

#conversão de tipos de dados, coerção, typecasting = é o ato de converter um tipo de dado em outro.
numero_inteiro = 10
numero_float = float(numero_inteiro)  # converte int para float
print("Número float convertido:", numero_float)
numero_float = 10.5
numero_inteiro = int(numero_float)  # converte float para int
print("Número inteiro convertido:", numero_inteiro)
# Conversão de string para int e float
numero_string = "123"

print(1+1) #soma inteiros
print('a'+'b') #concatenação de strings

#coerção 

print(int('1'), type(int('1')))  # converte string para int

print(int('1') + 1)  # soma int com int 

print(str(9)+'Twice') # converte int para string e concatena