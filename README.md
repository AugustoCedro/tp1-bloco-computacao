# tp1-bloco-computacao

### 1. Para cada programa implementado, explique sua lógica e funcionamento.
***Exercicio1.py***

**Bubble Sort:**

O algoritmo Bubble Sort para ordenar os nomes dos arquivos em ordem crescente. O algoritmo percorre a lista várias vezes, comparando dois elementos vizinhos. Quando o elemento da esquerda é maior que o elemento da direita, os dois são trocados de posição. 

**Selection Sort:**

O algoritmo Selection Sort para ordenar os nomes dos arquivos em ordem crescente. A cada iteração, o algoritmo percorre a parte ainda não ordenada da lista procurando o menor elemento. Quando encontra esse elemento, ele é trocado com o primeiro elemento da parte não ordenada. 

**Insertion Sort:**

O algoritmo Insertion Sort para ordenar os nomes dos arquivos em ordem crescente. O algoritmo percorre a lista a partir do segundo elemento, considerando os elementos anteriores como a parte já ordenada. O elemento atual é comparado com os elementos anteriores e, enquanto forem maiores, eles são deslocados uma posição para a direita. Depois, o elemento atual é inserido na posição correta. Esse processo continua até que toda a lista esteja ordenada.

***Exercicio2.py***

**Tabela Hash:**  
O programa utiliza uma tabela hash para armazenar os nomes dos arquivos associados a uma chave. Dessa forma, é possível adicionar, localizar e remover os arquivos utilizando essa chave. O programa percorre a lista de arquivos e adiciona cada elemento à tabela.

**Fila:**  
O programa utiliza uma fila implementada com `deque`, seguindo o princípio **FIFO (First In, First Out)**, no qual o primeiro elemento inserido é o primeiro a ser removido. Os arquivos são adicionados utilizando `append()` e removidos utilizando `popleft()`.

**Pilha:**  
O programa utiliza uma lista para implementar uma pilha, seguindo o princípio **LIFO (Last In, First Out)**, no qual o último elemento inserido é o primeiro a ser removido. Os arquivos são adicionados utilizando `append()` e removidos utilizando `pop()`. 

### 2. Calcule e explique a complexidade de tempo de cada algoritmo usando a notação Big O.

***Exercicio1.py***

**Bubble Sort: O(n²)**
Possui dois laços de repetição que percorrem a lista, realizando comparações entre os elementos. Por isso, sua complexidade é O(n²). Na implementação utilizada, mesmo que a lista já esteja ordenada, os laços continuam sendo executados.

**Selection Sort: O(n²)**
A cada posição, o algoritmo percorre o restante da lista procurando o menor elemento. Assim, são realizadas aproximadamente n² comparações, resultando em O(n²) nos casos melhor, médio e pior.

**Insertion Sort: O(n²)**
No pior caso, os elementos precisam ser comparados e deslocados várias vezes, resultando em O(n²). No melhor caso, quando a lista já está ordenada, a complexidade é O(n), pois cada elemento precisa apenas ser comparado uma vez.

***Exercicio2.py***

**Tabela Hash:**  
A inserção, busca e remoção de um elemento possuem complexidade média **O(1)**, pois o elemento pode ser acessado diretamente por meio da chave. Considerando a inserção ou remoção de todos os `n` elementos, a complexidade total é **O(n)**.

**Fila:**  
A inserção de um elemento utilizando `append()` possui complexidade **O(1)**, assim como a remoção utilizando `popleft()`. Portanto, para inserir ou remover todos os `n` elementos, a complexidade é **O(n)**. A busca por uma posição específica pode ter complexidade **O(n)**, pois pode ser necessário percorrer os elementos anteriores até chegar à posição desejada.

**Pilha:**  
A inserção utilizando `append()` possui complexidade média **O(1)** e a remoção utilizando `pop()` também possui complexidade **O(1)**, pois ocorre no final da lista. Assim, para inserir ou remover todos os `n` elementos, a complexidade total é **O(n)**. A busca por uma posição específica pode chegar a **O(n)**, pois pode ser necessário remover temporariamente vários elementos até alcançar a posição desejada.

### 3. Explique os diferentes tempos de execução e memória encontrados em cada estrutura de dados usados.

***Exercicio1.py***

**Bubble Sort:** 

Apresentou um tempo de execução de aproximadamente 3,23 segundos e utilizou 85.176 bytes de memória. O tempo foi maior porque o algoritmo realiza várias comparações e trocas entre os elementos durante seus percursos pela lista.

**Selection Sort:**

Apresentou um tempo de execução de aproximadamente 1,27 segundos e utilizou 85.176 bytes de memória. Ele foi mais rápido que o Bubble Sort porque realiza menos trocas, apesar de também possuir complexidade O(n²).

**Insertion Sort:**

Apresentou um tempo de execução de aproximadamente 1,45 segundos e utilizou 85.176 bytes de memória. Seu desempenho ficou próximo ao Selection Sort, pois os elementos são deslocados até encontrar suas posições corretas.

A memória foi igual nos três algoritmos porque todos utilizam a mesma quantidade de elementos e realizam a ordenação na própria lista, sem criar uma nova estrutura para armazenar os dados.

***Exercicio2.py***

**Tabela Hash:**  
A tabela hash apresentou um tempo de aproximadamente **0,000868 segundos** para adicionar os elementos e **0,000345 segundos** para removê-los. O consumo de memória foi de aproximadamente **294.992 bytes**. O maior consumo de memória ocorre devido à estrutura interna da tabela hash, que precisa manter espaço para organizar e localizar os elementos de forma rápida.

**Fila:**  
A fila apresentou um tempo de aproximadamente **0,000303 segundos** para adicionar os elementos e **0,000203 segundos** para removê-los. O consumo de memória foi de aproximadamente **87.352 bytes**. A utilização do `deque` permite realizar as operações de inserção e remoção de forma eficiente, mas possui uma estrutura interna própria que influencia o uso de memória.

**Pilha:**  
A pilha apresentou um tempo de aproximadamente **0,000266 segundos** para adicionar os elementos e **0,000238 segundos** para removê-los. O consumo de memória foi de aproximadamente **85.176 bytes**. Por utilizar uma lista, a pilha apresentou um consumo de memória um pouco menor que a fila. Após a remoção dos elementos, a lista ficou vazia e passou a apresentar aproximadamente **56 bytes**.

### 4. Compare os tempos de execução observados e relacione-os com suas complexidades teóricas.

***Exercicio1.py***

Os resultados observados são compatíveis com as complexidades teóricas, pois os três algoritmos possuem comportamento quadrático no pior caso. A diferença nos tempos ocorre devido à quantidade de comparações, trocas e deslocamentos realizados por cada algoritmo. A complexidade Big O indica como o tempo cresce conforme o tamanho da entrada aumenta, enquanto os tempos medidos representam o desempenho dos algoritmos na execução realizada.

***Exercicio2.py***

Os tempos observados são próximos do comportamento esperado pelas complexidades teóricas. A pilha apresentou o menor tempo de adição, enquanto a fila apresentou o menor tempo de remoção. Essas pequenas diferenças não significam que uma estrutura tenha necessariamente uma complexidade melhor que outra.

