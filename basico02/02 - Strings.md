# Básico 02 - Strings

Em nossos programas, também vamos precisar de usar texto para mensagens ou mostrar resultados para o usuário.

**String** é o tipo que guarda um texto qualquer. Ele deve ser escrito usando aspas duplas ou simples no começo e no final:

```python
'um texto entre aspas simples'
"um texto entre aspas duplas"

'esse texto aqui está errado!"
```

## Expressões

Existe apenas duas expressões que podemos fazer com texto: concatenar e comparar.

Concatenar é juntar duas sequências. Para o computador, um texto é apenas uma sequência de letras.

Usamos **+** para concatenar strings:

```python
'olá ' + 'mundo!'
"Meu nome é" + ' Joselito!'
```

Usamos a comparação com **==** para ver se uma string é **igual** a outra:

```python
'Joselito' == "Joselito"
'Maria' == 'José'
```

E usamos a comparação com **!=** para ver se uma string é **diferente** da outra:

```python
'Joselito' != 'Joseltio'
"Maria" != "José"
```

E claro, podemos colocar strings dentro de variáveis:

```python
nome = "Joselito"
casal = "Maria" + ' e ' + "José"
mensagem = "Meu amigo é " + nome
```

## Mostrando um texto para o usuário

Para mostrar um texto qualquer, usamos a função **print()**. Com print, podemos mostrar várias informações em uma linha usando várias partes, separadas por vírgula. Exemplos:

```python
meu_nome = "Joselito"
minha_idade = 33
print("Meu nome é",meu_nome)
print("Minha idade é",minha_idade)
amigo = "Ricardo"
print("Meu nome é", meu_nome,"e meu amigo é",amigo)
```

## Exercício

```python
## 1 - Crie variáveis com os dados pedidos:

# a) Seu Nome:

# b) Nome da sua mãe:

# c) Sua idade:

# d) Ano de nascimento:

# e) Nome de uma amizade:

## 2 - Use expressões para criar as seguintes variáveis:

# a) Uma mensagem de apresentação usando seu nome:

# b) Quantos anos você terá em 2030:

# c) Uma string dizendo a quanto tempo você conhece sua amizade, e o nome dela

## 3 - Mostre o que se pede usando print():

# a) A mensagem de apresentação que você criou antes:

# b) Usando format, uma mensagem dizendo que ano você nasceu, sua idade atual
# e quandos anos você terá em 2030 que você calculou antes:

# c) Uma mensagem com o nome da sua mãe, e qual a fruta você acha que ela gosta:


##### Agora EXECUTE O PROGRAMA COM F5 #####

```

Pronto!

