# Aula 02 - Decidindo o que fazer: Expressões de controle de execução do programa.

Vamos usar este programa como exemplo:

```python
# Este programa fala se a pessoa é nova ou não!
nome = "Rafael"
idade = 39

if (idade < 30): print(nome + ", você é uma pessoa nova!")
else: print(nome + ", você é uma pessoa velha!")
```

Execute o programa. O que ele mostra? Experimente mudar os valores das variáveis e execute novamente para ver o que acontece.

## IF

O **if** (*se* em inglês), permite que nós possamos criar programas que decidem o que fazer dependendo das condições que colocamos. Olhando mais de perto, ele deve ser escrito da seguinte maneira:

```python
if (expressão booleana): (lista de expressões)
```

A parte **expressão booleana** deve ser uma expressão que cria um valor **True** ou **False**, como vimos na aula anterior com os operadores **==, != e >** por exemplo.

A parte **lista de expressões** são as linhas do programa que só serão executadas **SE** for **True** o resultado da parte anterior. Vamos ver alguns exemplos. Você pode copiar eles e colar no seu programa de testes para ver o que acontece:

```python
# aqui a expressão booleana é True, então vai aparecer OK!
if (True): print("OK!")

# aqui a expressão booleana é False, então não vai aparecer FALSO!
if (False): print("FALSO!")

# aqui a expressão de comparação tem resultado verdadeiro
if (2 == 2): print("2 == 2 é verdadeiro!")
	
# e aqui a expressão de comparação é falsa
if (2 != 2): print("2 != 2 é falso!")
    
# aqui o valor dentro da variável é True
bonito = True
if (bonito): print("Que beleza!")
```

Agora crie 3 linhas usando o if para ver se acontece o que você espera acontecer!

## ELSE

O **else** (*senão* em inglês) permite que nós possamos escrever o que acontece caso o **if** anterior receba o valor **False**. Veja estes exemplos:

```python
# A)
if (True): print ("OK!")
else: print("FALSO!")

# B)
if (2 != 2): print("2 é diferente de 2!")
else: print("2 é igual a 2!")
    
# C)
bonito = True
if (bonito): print("Que beleza!")
else: print("Credo!")
    
# D)
esperta = True
if (esperta == False): print("OPA!")
else: print("AHA!")
```

Escreva no seu caderno o que você acha que vai ser escrito no computador em cada exemplo. Depois, execute ele no seu computador para conferir as respostas. Acertou tudo?

## Sequência de comparações (elif)

Às vezes, nós precisamos de fazer várias comparações para determinar o que fazer. Imagine que vamos fazer um programa que diga para nós algum ingrediente de uma comida. Como existem várias comidas diferentes, nós podemos verificar qual é linha por linha, usando uma mistura de **else e if** juntos, o **elif**:

```python
comida = ""
if (comida == "omelete"): print("Omelete se faz com ovos!")
elif (comida == "bolo"): print("Bolo precisa de leite!")
elif (comida == "sanduíche"): print("Sanduíche precisa de hamburguer!")
else: print("Não sei fazer essa comida!")
```

Este programa é executado da seguinte maneira:

1. A variável **comida** recebe um valor;
2. **Se** ela tiver o valor "omelete", mostramos a mensagem em frente **e ignoramos todo o resto até o else; senão** vamos para o próximo teste...
3. **Se** ela tiver o valor "bolo", mostramos a mensagem em frente e ignoramos o resto, senão...
4. A mesma coisa de novo, mas testamos o valor "sanduíche"; senão...
5. Só resta fazer o que está no **else**;

Coloque os seguintes valores na variável **comida**: "bolo", "salada", "arroz" e "omelete". Escreva no caderno qual mensagem aparece em cada caso.

## Exercício da Aula:

Agora crie um novo arquivo de código fonte, salve como "aula02-exercicio.py" na sua pasta de estudo e faça o exercício abaixo:

```python
# exercício - aula 02:

# 1 - coloque um valor na váriavel abaixo cada comentário
# para que a mensagem dentro do if seja mostrada no computador

# a
a = 
if (a): print("Certo!")

# b
b = 
if (b != True): print("Certo!")
    
# c
c = 
if (c > 30): print("Certo")
    
# d
d = 
if (d + 3 == 5): print("Certo!")
    
# 2 - Complete o programa abaixo que verifica se a pessoa é menor ou maior de idade.
# Mostre a mensagem "Você é maior de idade!" se a idade for maior ou igual a 18,
# ou mostre a mensagem "Você é menor de idade!" caso contrário.
# A variável 'idade' contém a idade da pessoa.
idade = 
if ( ): print("")
else: print("")

# 3 - Escreva um programa que verifica o nome da cor na variável 'cor'.
# Compare com 5 cores diferentes, e para cada cor mostre uma mensagem de um
# objeto que representa essa cor, por exemplo:
# se "azul" então print("O céu é azul!").
# E mostre uma mensagem caso a cor não seja nenhuma das 5 opções.
# Dica: Lembre-se da sequência de comparações!



# Não se esqueça de salvar com Ctrl+S e executar seu exercício com F5!

```

