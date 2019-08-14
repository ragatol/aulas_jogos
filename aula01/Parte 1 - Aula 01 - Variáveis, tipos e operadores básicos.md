# Aula 01 - Constantes, Variáveis, tipos e operadores básicos

Nesta aula vamos revisar o básico que já vimos anteriormente, começando com programa de exemplo.

Você pode criar um novo arquivo no programa IDLE e salvá-lo como `exemplo.py` dentro da sua pasta de estudo.

Copie o código-fonte abaixo:

```python
personagem = "Joselito"
mensagem = "Olá " + personagem
print(mensagem)
idade = 25
print("Sua idade daqui uma década será",idade + 10)
```

Neste pequeno programa, foram utilizadas variáveis e constantes.

## Variáveis

Servem para guardar alguma informação. Para criar uma variável com uma informação, digitamos o nome da variável, usamos o operador de **atribuição**, o `=`, e então escrevemos uma expressão que tenha um valor.

No programa de exemplo, na primeira linha, criamos uma variável com nome **personagem**, e colocamos o valor **"Joselito"** dentro dela.

Quais são as outras variáveis definidas no programa e quais seus valores? Escreva no caderno!

## Constantes

Uma constante é um valor que não pode ser mudado no programa. Nós utilizamos constantes toda vez que digitamos algo a ser utilizado como valor, seja para colocar este valor em uma variável como fizemos na primeira linha, ou para ser usada em uma expressão, como o **"Olá "** na segunda linha.

Escreva no seu caderno quais foram as constantes que usamos no programa de exemplo.

## Tipos de valores

Todas as constantes e variáveis que usamos num programa tem um tipo. Os tipos mais básicos são **números, strings (texto) e booleanos (verdadeiro ou falso / True ou False)**. Existem outros tipos mas vamos estudá-los mais tarde.

Os números representam qualquer número inteiro (1, 2, 3, etc.) como não inteiro (1.4, 1.8). Como o programa é interpretado em inglês, usamos o formato de número não-inteiro inglês, que usa o PONTO ao invéz da vírgula.

As strings são apenas uma sequência de letras, formando palavras ou frases. Para que o programa não se confunda entre o nome de uma variável e um texto, os textos são colocados entre aspas simples ou duplas, tipo `'assim'` ou `"assim"`. Não se esqueça que as aspas tem que ser combinadas, não pode começar com uma aspas simples e terminar com uma aspas dupla por exemplo!

Os valores BOOLEANOS são valores utilizados para lógica. São **VERDADEIROS** ou **FALSOS**, e como temos que utilizar inglês, usamos **True** ou **False**. Vamos usar bastante eles quando estudarmos controle de fluxo do programa.

Você consegue dizer qual tipo de valor existe em cada uma das variáveis no programa de exemplo? Escreva no caderno.

## Operadores básicos

O tipo de valor é importante para saber qual tipo de operação podemos fazer com ele, e qual tipo de valor cada operação produz. Vamos ver as operações mais básicas:

| Operador | Operação      | Exemplo                                                      | Tipo de valor aceito | Tipo de valor resultante |
| -------- | ------------- | ------------------------------------------------------------ | -------------------- | ------------------------ |
| +        | Adição        | 2 + 3 → 5<br />"Olá " + "mundo!" → "Olá mundo!"              | número ou string     | número ou string         |
| -        | Subtração     | 3 - 2 → 1                                                    | número               | número                   |
| *        | Multiplicação | 2 * 3 → 6                                                    | número               | número                   |
| /        | Divisão       | 4 / 2 → 2                                                    | número               | número                   |
| ==       | Igual à       | 2 == 2 → True<br />2 == 3 → False                            | qualquer             | booleano                 |
| !=       | Diferente de  | 2 != 2 → False<br />2 != 3 → True                            | qualquer             | booleano                 |
| >        | maior que     | 2 > 2 → False<br />2 > 1 → True                              | número ou string     | booleano                 |
| <        | menor que     | 2 < 1 → False<br />1 < 2 → True                              | número ou string     | booleano                 |
| and      | E lógico      | True and True → True<br />True and False → False<br />False and False → False | booleano             | booleano                 |
| or       | OU lógico     | True or True → True<br />True or False → True<br />False or False → False | booleano             | booleano                 |

Tenha essa tabela como referência, anote ou volte aqui nesta aula para relembrar caso esqueça!

## Exercício da aula

Com as informações passadas nessa aula, vamos fazer um exercício para ver se você entendeu.

Primeiro, copie e salve o programa abaixo na sua pasta de estudo, com o nome **exercicio-aula01.py**. Depois, siga as instruções nos comentários (linhas começadas com **#**).

```

```

Seguiu todas as instruções? Salve o que você fez apertando **Ctrl+S** no teclado e então execute seu programa apertando **F5**. Depois mostre pro professor para ele conferir!