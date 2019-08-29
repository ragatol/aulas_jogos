# Básico 01 - Números

Em nossos programas, nós definimos valores numéricos como **INTEIROS** ou **REAIS**:

Números inteiros:

```python
1
4
0
7
-2
-10
```

Números reais:

```python
1.4
5.8
0.2
-3.2
-10.0
```

## Expressões

Uma expressão é uma **operação** com um ou mais valores, usando um **OPERADOR**.

Operadores Aritméticos:

| Nome          | Símbolo | Exemplo          |
| ------------- | ------- | ---------------- |
| Adição        | +       | 1 + 3 → 4        |
| Subtração     | -       | 4.3 - 2 → 2.3    |
| Multiplicação | *       | 2 * 10 → 20      |
| Divisão       | /       | -10.6 / 2 → -5.3 |

## Ordem das Operações

Quando vários operadores são usados na mesma expressão, alguns são calculados antes de outros. A ordem de execução é a mesma da álgebra: *** e / são feitos antes de + ou -**. Exemplo:

```
2 * 3 + 2 => 6 + 2 => 8
9 + 6 / 3 => 9 + 2 => 11
```

Para controlar a ordem das operações fora da ordem algébrica, podemos usar **parênteses ()**:

```
2 * (3 + 2) => 2 * 5 => 10
(9 + 6) / 3 => 15 / 3 => 5
```

## Variável

Variável é quando colocamos um valor dentro de um nome, usando **o operador =**, que podemos utilizar depois. Exemplos:

```python
idade = 14
altura = 1.7
```

Também podemos colocar o resultado de uma expressão:

```python
area_da_sala = 2 * 3.5
metade_de_cem = 100 / 2
```

Depois de colocar um valor dentro de uma variável, podemos reutilizar esse valor em outro lugar:

```python
minha_idade = 14
idade_do_professor = 39
diferenca_de_idade = idade_do_professor - minha_idade

cem = 2 * metade_de_cem
```

Também podemos copiar o valor de uma variável para outra:

```python
outro_cem = cem
copia_da_idade = idade
```



## Exercício

```python
## 1 - Criar expressões para as seguintes operações:

# a) Somar sua idade e 10:

# b) Calcular o dobro de 35:

# c) Diferença da sua idade com a de um(a) colega:

# d) Somar o dobro da sua idade com a metade da idade de um(a) colega:


## 2 - Usar parênteses, se necessário, para que as expressões abaixo façam o resultado certo:

# a) = 12
4 + 4 * 2

# b) = 3
10 - 4 / 2

# c) = 60
2 * 4 + 6 * 3

# d) = 17
2 * 4 + 6 - 3

## 3 - Vamos criar um pequeno programa:

# a) Crie 2 variáveis: uma para guardar o ano que você nasceu, e outra para guardar
# sua idade.



# b) Agora calcule a diferença entre um ano qualquer e o ano que você nasceu
# usando as variáveis que você criou antes, e coloque o resultado em uma nova
# variável. Este valor é quantos anos você terá no ano que você usar na expressão!


# c) Crie uma variável para guardar uma idade maior que a sua


# d) Usando essa idade maior, vamos ver em qual ano você vai ter essa idade.
# Para isso, subtraia a idade maior da sua idade, e some ao ano que você nasceu.
# Use apenas as variáveis que você criou antes, e coloque o resultado em uma nova
# variável!


# e) Agora copie o valor das variáveis que você criou para as variáveis abaixo, de
# acordo com o nome delas, no lugar dos '0':
copia_sua_idade = 0
copia_ano_nascimento = 0
copia_idade_no_furuto = 0
copia_ano_da_idade_no_futuro = 0

##### Agora EXECUTE O PROGRAMA COM F5 #####

print("Você nasceu em {}, e hoje tem {} anos.".format(copia_ano_nascimento,copia_sua_idade))
print("No ano de {}, você terá {} anos de idade!".format(copia_ano_da_idade_no_futuro,copia_idade_no_futuro))
```

Pronto!