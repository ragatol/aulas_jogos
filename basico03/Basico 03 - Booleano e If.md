# Básico 03 - Comparações

Até agora, só criamos programas que executam as expressões uma depois da outra, sem qualquer opção para mudar esta ordem de execução.

Vamos ver como podemos escolher o que fazer em um programa usando o **IF**.

## IF (se)

O **if** é um *bloco de controle* que permite a execução condicional de expressões.

Com ele, podemos escolher entre executar ou não expressões baseadas em um teste.

Veja um exemplo:

```python
idade = 20
if (idade > 18): print("Você é maior de idade!")
```

Neste exemplo, usamos um operador de comparação. Operadores de comparação criam valores do tipo **BOOLEANO**. Existe apenas duas opções para este tipo de valor: **True** para *verdadeiro* e **False** para falso.

A expressão logo depois da palavra **if** deve ser uma que tenha um resultado booleano, portanto devemos usar os operadores de comparação.

## Operações Booleanas

### Comparando Números

Nesta tabela temos os operadores booleanos mais comuns para números.

| Operador | Operação         | Exemplos                          |
| -------- | ---------------- | --------------------------------- |
| ==       | Igual à          | 2 == 2 → True<br />2 == 3 → False |
| !=       | Diferente de     | 2 != 2 → False<br />2 != 3 → True |
| >        | maior que        | 2 > 2 → False<br />2 > 1 → True   |
| >=       | maior ou igual à | 2 >= 2 → True<br />2 >= 1 → True  |
| <        | menor que        | 2 < 1 → False<br />1 < 2 → True   |
| <=       | menor ou igual à | 2 <= 2 → True<br />2 <= 1 → True  |

### Comparando Strings

Para strings, geralmente usamos apenas os operadores de comparação **==** e **!=**. A comparação é feita letra por letra, e diferencia maiúsculas de minúsculas:

```python
# Estas strings são iguais
"Joselito" == "Joselito"

# Estas são diferentes
"Joselito" != "joselito"
```

#### Comparando Strings com Números

Para comparar um texto com um número, precisamos ou transformar o número em texto, ou tentar transformar o texto em número:

```python
# Aqui transformamos o número 5 em uma string:
str(5)

# Aqui transformamos uma string em um número:
int("5")

# transformando o número em string e comparando com um texto:
str(22) == "22"

# transformando um texto em número e comparando números:
int("15") < 16
```

### Comparando Booleanos

Além de comparar como fizemos com strings, usando *igual à* e *diferente de*, existem duas operações exclusivas para booleanos: **and** e **or**.

#### AND (e)

Usamos o **and** para verificar se os dois valores são verdadeiros. Ele resulta em **True** apenas nesse caso.

```python
# Apenas aqui o resultado é verdadeiro (True):
True and True

# Todos os casos aqui resultam em falso (False):
True and False
False and True
False and False
```

#### OR (ou)

Usamos o **or** para verificar se algum dos valores é verdadeiro.

```python
# Todos os casos aqui resultam em verdadeiro (True):
True or False
False or True
True or True

# Apenas neste caso o resultado é falso (False):
False or False
```

### Expressões Booleanas

Podemos criar expressões usando os comparadores com várias operações de uma vez, misturando valores com variáveis, e até mesmo usando parênteses. Verifique qual resultado cada linha aqui dá no IDLE:

```python
# definindo variáveis para usar nas expressões abaixo:
idade = 15
nome = "Joselito"

# comparando valores com variáveis:
idade < 18
nome != "Ricardo"

# fazendo comparações mais complicadas:

# conferindo se a comparação de 2 igual a 2 é falsa:
(2 == 2) == False

# verificando se a idade é maior que 10, e se o nome é igual a "Roberto":
idade > 10 and nome == "Roberto"
```

## Usando IF para criar um programa

Agora vamos criar um programa usando o que aprendemos até hoje, mas antes vamos ver como escrevemos um programa que usa o **if**.

Lembrando que para usar um **if** simples, escrevemos da seguinte maneira:

```python
if (expressão-booleana): operação se verdadeiro
```

* expressão-booleana é um valor True ou False, ou uma operação de comparação;
* operação se verdadeiro é o que vai ser executado apenas e a expressão for verdadeira;

Exemplos:

```python
nome = "Joselito"
if (nome != "Ricardo"): print("Você não é o Ricardo!")

idade = 15
if (idade > 18): print("Você é maior de idade")
if (idade < 30): print("Você não está velho!")
```

### Lendo algo que o usuário digita

Além do IF, vamos fazer algumas perguntas para usar em nosso programa usando **input**. **Input** mostra uma mensagem e espera que o usuário digite algo com ENTER e coloca o que foi digitado na variável:

```python
nome_digitado = input("Qual seu nome? ")
idade_digitada = input("Qual sua idade? ")
```

### Criando um programa que usa o nome e a idade

Crie um novo arquivo no IDLE (File -> New File) e grave ele na sua pasta de estudo.

Depois siga as instruções abaixo para criar um programa que mostra mensagens diferentes dependendo do que a pessoa responder!

Não se esqueça de usar **print** para mostrar mensagens para a pessoa que está usando o programa, **input** para fazer as perguntas, e **if** para fazer coisas apenas se necessário!

Abra o exercício no navegador e copie.

