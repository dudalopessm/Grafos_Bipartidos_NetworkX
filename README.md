# Grafos Bipartidos com NetworkX (Python)

Este repositório apresenta exemplos práticos e didáticos de **grafos bipartidos** utilizando a biblioteca [NetworkX](https://networkx.org/) em Python. O conteúdo foi produzido como parte de um trabalho acadêmico na disciplina de Teoria dos Grafos, com o objetivo de **popularizar e facilitar a compreensão da biblioteca NetworkX**, especialmente para iniciantes em Teoria dos Grafos e programação.

---

## O que são Grafos Bipartidos?

Um **grafo bipartido** é um tipo especial de grafo em que os **vértices podem ser divididos em dois conjuntos disjuntos**, de forma que **não existam arestas entre vértices do mesmo conjunto**. Ou seja, todas as conexões (arestas) ocorrem entre vértices de conjuntos diferentes.

Esse tipo de modelagem é útil em problemas de **recomendação**, **alocação**, **relacionamento entre entidades diferentes**, entre outros.

---

## O que o script `grafos_bipartidos.py` apresenta?

O arquivo Python incluído neste repositório contém exemplos comentados e estruturados com os seguintes objetivos:

### Exemplos de construção de grafos bipartidos
- Criação de diversos grafos bipartidos.
- Visualização com `matplotlib`.

### Exemplos de grafo não bipartido
- Demonstração de um **ciclo ímpar**, que impossibilita a bipartição.

### Verificação de bipartição
- Funções que checam se um grafo é bipartido com `networkx.algorithms.bipartite`.

### Análise de conjuntos bipartidos
- Recuperação dos dois conjuntos disjuntos (U e V) de um grafo bipartido.
- Tratamento de erros caso o grafo não seja bipartido.

### Visualização didática dos grafos
- Função `desenhar_grafo` para mostrar grafos com ou sem bipartição destacada.

### Florestas como grafos bipartidos
- Construção de uma floresta (conjunto de árvores disjuntas).
- Verificação de que florestas são sempre bipartidas.

### Número cromático
- Cálculo do número cromático de um grafo bipartido para mostrar que são **2-coloríveis**.

---
### Conceitos Aplicados
- Grafo Bipartido
- Verificação de Bipartição
- Partição de Conjuntos
- Ciclo Ímpar
- Floresta
- Número Cromático
- Visualização com Matplotlib
- Funções auxiliares com NetworkX
  
---

## Autoria
Trabalho acadêmico desenvolvido para a disciplina de Teoria dos Grafos.

Universidade Federal de Uberlândia - Ciência da Computação - Teoria dos Grafos - 2024.1

Autores: Yan Lucas, Diogo Koichi, Eduarda Lopes, Lucas Matos.

---

## Bibliotecas Utilizadas

- [`networkx`](https://networkx.org/): construção e análise de grafos.
- `matplotlib`: visualização dos grafos.
  
Instale com:

```bash
pip install networkx matplotlib
