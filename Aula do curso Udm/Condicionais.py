#Aprendendo if, else e elif
# se (if) a condição for verdadeira, faça isso
# se não (else) faça isso
# se (elif) outra condição for verdadeira, faça isso // meio que o Else if do C, C++, Java, JavaScript...

entrada = input('Você quer "entrar" ou "sair"? ') 

if entrada == 'entrar':
    print('Você entrou no sistema!')    
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Comando inválido! Por favor, digite "entrar" ou "sair".')

#Nesse caso usamos o tab para indicar o bloco de código que pertence ao if, elif e else
#Em Python, a indentação é obrigatória para definir blocos de código
# O tab equivale a 4 espaços
#O elif é opcional mas pode ser usado quantas vezes forem necessárias
#O else também é opcional e só pode ser usado uma vez, no final
#Podemos usar operadores lógicos (and, or, not) para combinar condições
#Exemplo:
idade = int(input('Digite sua idade: '))
if idade < 0:
    print('Idade inválida!')
elif idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 65:
    print('Adulto')
else:
    print('Idoso')
#Podemos usar ifs aninhados, mas é recomendado evitar para manter o código legível


#Trabalhando com condições 

condição = 10 == 10  # True

if condição:
    print('A condição é verdadeira! Vamos imprimir isso.')
else:
    print('A condição é falsa! Não vamos imprimir isso.')

#Operadores de comparação
# == igual
# != diferente  
# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
#Podemos usar qualquer expressão que retorne um valor booleano (True ou False) em uma condição if

condição1 = False

if condição1:
    print('A condição1 é verdadeira!')  
else:
    print('A condição1 é falsa!')   

#não existe elif e else sem if
#o if pode ser usado sozinho
#o else e o elif só podem ser usados junto com o if

#Da de usar o "pass" para dizer que eu vou escrever depois o código do if, elif ou else
#Exemplo:   
if condição1:
    pass
else:
    pass
#Isso é útil quando estamos escrevendo o código e ainda não sabemos o que fazer em cada condição
#Mas não é recomendado deixar o código assim por muito tempo, pois pode gerar confusão

#Anexo essa aula, estamos vendo o debbugging (depuração)
#Depuração é o processo de encontrar e corrigir erros no código

#No viausl code existem os breakpoints (pontos de interrupção)
#Podemos clicar na margem esquerda do editor para adicionar um breakpoint
#Quando rodamos o código em modo de depuração, a execução para no breakpoint
#Podemos então inspecionar variáveis, ver o fluxo de execução e entender o que
#está acontecendo no código

#ele para antes de executar a linha onde está o breakpoint
#Podemos usar os botões de continuar, passo a passo, sair da função, etc
#Para rodar o código em modo de depuração, podemos clicar com o botão direito no editor
#e selecionar "Iniciar Depuração" ou usar o atalho F5
#Podemos ver o valor das variáveis na aba "Variáveis" do painel lateral


