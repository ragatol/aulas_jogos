# Funções

Funções são pequenos blocos de código que podem ser utilizados várias vezes dentro do mesmo programa. Usamos funções para simplificar e organizar o programa.

## Usando Funções

Nas aulas passadas, já utilizamos algumas funções: **print** para mostrar uma mensagem na tela, **input** para ler algo que o usuário escreve, e **int** para converter um texto em um número.

```python
print("Olá pessoal!")

nome = input("Qual seu nome?")

numero = int("20")
```

Para usar uma função, seguimos a seguinte forma:

"nome" + "(" + "parâmetros" + ")"

Uma função pode ter qualquer quantidade de parâmetros, inclusive nenhum. Por exemplo, a função **print** pode montar uma mensagem antes de ser mostrada na tela juntando os vários parâmetros informados:

```python
print() # não imprime nada já que nenhum parâmetro foi usado
print("Olá!") # imprime 'Olá'
idade = 11
print("Minha idade é",idade) # imprime 'Minha idade é 11'
print("Meu nome", "é", "Joselito!") # imprime 'Meu nome é Joselito!'
```

Como pode ver, os parâmetros são separados por vírgula.

## Criando Funções

Para criar uma função, devemos usar a seguinte forma:

```python
def nomedafuncao(<lista de parâmetros>):
    <comandos>
    .
    .
    .
```

Veja os exemplos:

```python
# criar uma função que não faz nada
def fazernada():
	pass
	
# criar uma função que apenas mostra 'Oi!'
def dizeroi():
	print("Oi!")

# cria uma função que monta uma mensagem usando o valor de um parâmetro
def mostrarcomidda(comida):
	print("Minha comida favorita é",comida)
	
# 'retorna' o resultado da soma
def fazersoma(a,b):
	return a + b
```

### Lista de Parâmetros

A lista de parâmetros define uma lista de nomes que podem receber valores no momento que a função é usada. Então, os valores podem ser utilizados pela função para fazer o trabalho. No exemplo anterior, a função **mostrarcomida** define um único parâmetro: **comida**. Então, ele usa este nome para mostrar uma mensagem personalizada. Veja os exemplos de uso:

```python
mostrarcomida("lasanha") # mostra 'Minha comida favorita é lasanha'

minhacomida = 'pizza'
mostrarcomida(minhacomida) # mostra 'Minha comida favorita é pizza'
```

No primeiro caso, colocamos um valor para o parâmetro **comida** diretamente.

No segundo caso, o valor dentro da variável *minhacomida* é copiado para o parâmetro **comida**, e então a função é "chamada".

### Retornando Valores

Quando queremos que uma função faça um cálculo, e queremos ter o resultado deste cálculo para usar em outra parte do programa, precisamos "retornar" esse valor de dentro da função. Para isso usamos **return**, como na função **fazersoma** do exemplo acima.

Então, basta utilizar a função como se fosse também uma variável, por exemplo:

```python
# a variável 'valor' receberá 5
valor = fazersoma(2,3)

# a variável 'outraidade' terá 30
idade = 20
outraidade = fazersoma(idade,10)

# usando fazersoma como se fosse uma variável,
# mostrando a mensagem 'A soma de 3 e 5 é 8'
print("A soma de 3 e 5 é",fazersoma(3,5))
```

## Exercícios

```python
# programe as funções abaixo de acordo com o nome de cada função
def fazer_nada():

def mostrar_meu_nome():
    
def dizer_oi(usuario):
    
def mostrar_soma(a,b):
    
# programe as funções a seguir para retornar o valor segundo seu nome
def area_retangulo(altura,largura):
    
def media(a, b, c):
    
def menor_valor(x, y):
    

```

