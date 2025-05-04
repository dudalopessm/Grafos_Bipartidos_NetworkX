import networkx as nx
from networkx.algorithms import bipartite
from networkx.algorithms.tree import is_forest
import matplotlib.pyplot as plt

# ===================
# EXEMPLO SLIDE 03
# ===================

B = nx.Graph()

usuarios = ["U1", "U2", "U3"]
filmes = ["F1", "F2", "F3", "F4"]

B.add_nodes_from(usuarios, bipartite=0)
B.add_nodes_from(filmes, bipartite=1)

arestas = [
    ("U1", "F1"),
    ("U1", "F2"),
    ("U2", "F2"),
    ("U2", "F3"),
    ("U3", "F1"),
    ("U3", "F4")
]
B.add_edges_from(arestas)

pos = dict()
pos.update((n, (1, i)) for i, n in enumerate(usuarios))  # linha da esquerda
pos.update((n, (2, i)) for i, n in enumerate(filmes))    # linha da direita

cores_nos = ['#dda2a2' if n in usuarios else '#bc81ca' for n in B.nodes()]

plt.figure(figsize=(8, 5))
nx.draw(B, pos, with_labels=True, node_color=cores_nos,
        node_size=1500, edge_color="gray", font_size=10)
plt.title("Exemplo de Grafo Bipartido: Usuários e Filmes")
plt.axis("off")
plt.close()

# ===================
# EXEMPLO SLIDE 05
# ===================

G_ímpar = nx.Graph()

arestas = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v5"), ("v5", "v1")]
G_ímpar.add_edges_from(arestas)

pos = nx.circular_layout(G_ímpar)

plt.figure(figsize=(5, 5))
nx.draw(G_ímpar, pos, with_labels=True, node_color="#dda2a2",
        node_size=1500, edge_color="gray", font_size=10)
plt.title("Exemplo de Ciclo Ímpar (5 vértices) - Não Bipartido")
plt.axis("off")
plt.show()

# ===================
# EXEMPLOS SLIDES 8 - 11
# ===================

G = nx.Graph()
G.add_edges_from([(1,'A'), (1,'B'), (2,'A'), (2, 'C')])

def is_bipartite(G):
    return nx.is_bipartite(G)

if is_bipartite(G):
    print("O grafo é bipartido.")
else:
    print("O grafo não é bipartido.")

G_nao_bipartido = nx.Graph()
G_nao_bipartido.add_edges_from([(1, 2), (2, 3), (3, 1)])

if is_bipartite(G_nao_bipartido):
    print("O grafo é bipartido.")
else:
    print("O grafo não é bipartido.")

# ===================
# EXEMPLO SLIDES 12 - 20
# ===================

# ===================
# CRIAÇÃO DO GRAFO G1
# ===================

# Cria um grafo vazio G1 (bipartido)
G1 = nx.Graph()

# Conjuntos bipartidos para G1
U = {1, 2, 3, 4, 5, 6, 7, 8}
V = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}

# Arestas entre os vértices de U e V para G1
arestas = [
    (1, 'a'), (1, 'b'), (1, 'c'),
    (2, 'b'), (2, 'd'),
    (3, 'c'), (3, 'e'),
    (4, 'a'), (4, 'f'),
    (5, 'd'), (5, 'g'),
    (6, 'e'), (6, 'h'),
    (7, 'f'), (7, 'g'),
    (8, 'h')
]
G1.add_edges_from(arestas)

# ===================
# CRIAÇÃO DO GRAFO G2
# ===================

# G2 com ciclo ímpar (portanto, não bipartido)
G2 = nx.Graph()
G2.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])

# Adiciona arestas que interligam nós com G1 (misturando conjuntos)
edges = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
G2.add_edges_from(edges)

# ===================
# FUNÇÕES DE APOIO
# ===================

# Verifica se um grafo é bipartido

def is_bipartide(graph):
    return bipartite.is_bipartite(graph)

"""
IMPLEMENTAÇÃO REAL DA FUNÇÃO is_bipartide
def is_bipartite(G):
   try:
        color(G)  # Tenta aplicar a coloração bipartida no grafo
        return True  # Se a coloração funcionar, o grafo é bipartido
    except nx.NetworkXError:  # Se houver erro (não for bipartido)
        return False  # O grafo não é bipartido
 """

# Encontra os dois conjuntos bipartidos de um grafo

def is_bipartide_node_set(graph):
    if not bipartite.is_bipartite(graph):
        raise ValueError("O grafo nao eh bipartido.")
    color = bipartite.color(graph)
    set1 = {node for node, c in color.items() if c == 0}
    set2 = {node for node, c in color.items() if c == 1}
    return set1, set2

"""
IMPLEMENTAÇÃO REAL DA FUNÇÃO is_bipartite_node_set
def is_bipartite_node_set(G, nodes):
  S = set(nodes)

    if len(S) < len(nodes):
        # this should maybe just return False?
        raise AmbiguousSolution(
            "The input node set contains duplicates.\n"
            "This may lead to incorrect results when using it in bipartite algorithms.\n"
            "Consider using set(nodes) as the input"
        )

    for CC in (G.subgraph(c).copy() for c in connected_components(G)):
        X, Y = sets(CC)
        if not (
            (X.issubset(S) and Y.isdisjoint(S)) or (Y.issubset(S) and X.isdisjoint(S))
        ):
            return False
    return True
 """
# ===================
# ANÁLISE DOS GRAFOS
# ===================

# GRAFO G1
print("Analise do Grafo G1:")
print("- Eh bipartido?", is_bipartide(G1))
try:
    u, v = is_bipartide_node_set(G1)
    print("- Conjunto U:", u)
    print("- Conjunto V:", v)
except ValueError as e:
    print("- Erro:", e)
print()

# GRAFO G2

print("Analise do Grafo G2:")
print("- Eh bipartido?", is_bipartide(G2))
try:
    u, v = is_bipartide_node_set(G2)
    print("- Conjunto U:", u)
    print("- Conjunto V:", v)
except ValueError as e:
    print("- Erro:", e)
print()

# Número cromático de G1
print("Numero cromatico de G1:")
coloring = nx.coloring.greedy_color(G1, strategy="largest_first")
num_colors = max(coloring.values()) + 1
print("- Numero cromatico:", num_colors)
print()

# ===================
# CRIAÇÃO DO GRAFO G3 (FLORESTA)
# ===================

G3 = nx.Graph()
G3.add_edges_from([(1, 2), (2, 3)])       # Primeira árvore
G3.add_edge(4, 5)                         # Segunda árvore
G3.add_edges_from([(6, 7), (7, 8), (8, 9)])  # Terceira árvore

# Análise de floresta e bipartição
print("Analise do Grafo G3:")
print("- Eh uma floresta?", is_forest(G3))
print("- Eh bipartido?", bipartite.is_bipartite(G3))
print()

# ===================
# FUNÇÃO DE VISUALIZAÇÃO COM MATPLOTLIB
# ===================

def desenhar_grafo(grafo, titulo, conjuntos=None, evidenciar_biparticao=False):
    plt.figure(figsize=(8, 6))

    if evidenciar_biparticao and conjuntos:
        pos = nx.bipartite_layout(grafo, conjuntos[0])
    else:
        pos = nx.spring_layout(grafo, seed=42)

    if conjuntos:
        u, v = conjuntos
        nx.draw_networkx_nodes(grafo, pos, nodelist=u,
                               node_color='#dda2a2', label='Conjunto U')
        nx.draw_networkx_nodes(grafo, pos, nodelist=v,
                               node_color='#bc81ca', label='Conjunto V')
    else:
        nx.draw_networkx_nodes(grafo, pos, node_color='#dda2a2')

    nx.draw_networkx_edges(grafo, pos, edge_color='black')
    nx.draw_networkx_labels(grafo, pos)
    plt.title(titulo)
    plt.axis('off')
    plt.show()

# ===================
# VISUALIZAÇÃO DOS GRAFOS
# ===================
try:
    u1, v1 = is_bipartide_node_set(G1)
    desenhar_grafo(G1, "Grafo G1 (Bipartido)", (u1, v1))
    desenhar_grafo(G1, "Grafo G1 (Bipartição Evidenciada)", (u1, v1), evidenciar_biparticao=True)
except:
    desenhar_grafo(G1, "Grafo G1")
    desenhar_grafo(G1, "Grafo G1 (Layout Alternativo)")

try:
    u2, v2 = is_bipartide_node_set(G2)
    desenhar_grafo(G2, "Grafo G2 (Bipartido)", (u2, v2))
    desenhar_grafo(G2, "Grafo G2 (Bipartição Evidenciada)", (u2, v2), evidenciar_biparticao=True)
except:
    desenhar_grafo(G2, "Grafo G2 (Nao Bipartido)")

try:
    u3, v3 = is_bipartide_node_set(G3)
    desenhar_grafo(G3, "Grafo G3 (Floresta Bipartida)", (u3, v3))
    desenhar_grafo(G3, "Grafo G3 (Bipartição Evidenciada)", (u3, v3), evidenciar_biparticao=True)
except:
    desenhar_grafo(G3, "Grafo G3 (Floresta)")
    desenhar_grafo(G3, "Grafo G3 (Floresta - Layout Alternativo)")