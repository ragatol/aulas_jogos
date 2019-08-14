# exercício - aula 01

# 1 - Dê um valor para as variáveis abaixo de acordo com o comentário.

# número
idade = 
# string
nome = 
# string
comida_favorita = 
# booleano
sou_menina = 

# 2 - Crie expressões usando um operador de acordo com cada comentário:

# Uma mensagem usando a variável nome (string):
mensagem = 

# Uma mensagem usando a variável comida_favorita (string):
sobre_comida = 

# Metade de sua idade (número)
meia_idade = 

# Conferindo se sua idade é maior que 12
# (expressão usa números mas o valor resultante é booleano)
maior_que_doze = 

# Conferindo se você é menina E se é maior que 12 (apenas booleano)
menina_maior_que_doze = 

# 3 - Escreva o valor resultante de cada expressão abaixo e atribua
# o valor à variável.

# 2 + 3
a = 

# a > 3
b = 

# "este texto" + " é " + "emendado"
c = 

# "bonito" == "feio"
d = 

### EXECUTE O PROGRAMA COM F5! ###

print("""Parte 1:
Sua idade é: {}
Seu nome é: {}
Sua comida favorita é: {}
Você é: {}
""".format(idade,nome,comida_favorita,"menina" if sou_menina else "menino"))

print("""Parte 2:
A mensagem é:
{}
Sobre sua comida favoria:
{}
Metade da sua idade é:
{}
Você tem mais que 12 anos:
{}
Você é menina e tem mais de 12 anos:
{}
""".format(mensagem,sobre_comida,meia_idade,maior_que_doze,menina_maior_que_doze))

print("""Parte 3:
a = {}
b = {}
c = {}
d = {}
""".format(a,b,c,d))


