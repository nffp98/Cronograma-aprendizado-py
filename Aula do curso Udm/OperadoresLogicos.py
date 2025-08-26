#aprender sobre operadores logicos
#and, or, not, is

#and = e = Todas as condições precisam ser verdadeiras
#or = ou = Apenas uma das condições precisa ser verdadeira
#not = não = Inverte o resultado
#is = é = Compara se um valor é igual ao outro
#in = em = Verifica se um valor está contido em uma sequência (string, lista, etc.)
#not in = não em = Verifica se um valor não está contido em uma sequência (string, lista, etc.)
#0 / 0.0 / '' / "" / [] / () / {} = False ou falsy = vazio = False
#Também existe o tipo None = vazio = False usado pra indicar que uma variável não tem valor

#sitema para aprender a logica dos operadores logicos

entrada = input('[E]ntrar [S]air: ')
senha_da_pessoa = input('Senha: ')

print('Você escolheu a opção: {}'.format(entrada))

#O if só é executado quando todas as condições forem verdadeiras
#O and tem precedência sobre o or, ou seja, o and é executado primeiro
if entrada == 'E' and senha_da_pessoa == '1234':
    print('Você entrou no sistema') 
else:
    print('Você não entrou no sistema')
    print('Até mais!')

#Chamado de avaliação de curto circuito
#print( True and True ) #True
#print( True and False ) #False
#print( False and True ) #False
#print( False and False ) #False

#print(bool('')) #False
#print(bool(' ')) #True
#print(bool([])) #False
#print(bool([1, 2, 3])) #True
#print(bool(())) #False
#print(bool((1, 2, 3))) #True
#print(bool({})) #False
#print(True and 0 and True) #0 #False

#Operador or //  qualquer condição verdadeira, o resultado é verdadeiro
#print( True or True ) #True
#print( True or False ) #True
#print( False or True ) #True
#print( False or False ) #False 

#Entre parenteses, o and é avaliado antes do or 
if (entrada == 'E' or entrada == 'e') and senha_da_pessoa == '1234':
    print('Você entrou no sistema') 
else:
    print('Você não entrou no sistema')
    print('Até mais!')

#exemplo de avaliação de curto circuito com or

senha = input('Senha: ') or 'Sem senha' #se o input for vazio, a variável senha recebe 'Sem senha'

print(senha)

#operador not
#inverte o valor booleano

senha = input('Senha: ')

if not senha: #se a senha for vazia
    print('Você não digitou nada')  
else:
    print('Você digitou a senha: {}'.format(senha))

#print(not True) #False
#print(not False) #True

#Operador in e not in

#Strings são iteráveis ou seja  podem ser percorridas

#0 1 2 3 4 5 6 7 8 9 10
#Julia
#-9 -8 -7 -6 -5 -4 -3 -2 -1

nome = 'Julia'
print('u' in nome) #True
print('z' in nome) #False
print('u' not in nome) #False
print('z' not in nome) #True

#Printar o índice de uma letra na string
print(nome[2]) #imprime a letra na posição 2 que é a letra 'l'
print(nome[10])  #imprime erro pois não existe a posição 10 na string


