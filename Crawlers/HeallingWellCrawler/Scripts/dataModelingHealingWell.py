from networkx.readwrite import json_graph
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import jsonlines
import json
# -----------------
'''
Esse modelo de grafo possui 2 tipos de nós, usuarios e posts. Eles sao ligados por relacionamentos
de tipos, criacao e interacao.

Nós azuis representam usuarios e nós vermelhos representam posts
Arestas roxas representam autoria, e arestas vermelhas representam participacao
'''
# LOADING THE DATASET
commentsList = []
with jsonlines.open("/home/silas/Documents/Silas_Personal_Files/Python-Codes/Crawlers/\
HeallingWellCrawler/HealingWellComments_labCores.jsonl", mode='r') as f:
    for i in f:
        commentsList.extend(i)
CommentsDataset = pd.DataFrame(commentsList)
G = nx.Graph()  # criacao de um objeto q é um grafo
# --------------------------------------
# -------------- 1a ETAPA --------------
# ADICIONANDO NÓS DO TIPO USUARIO
AuthorsNamesList = set()
# AuthorsNamesList2 = []
for thread in range(len(CommentsDataset)):
    listAuxiliar = [x['commentAuthor']
                    for x in CommentsDataset.loc[thread, "postContent"]]  # list comprehension
    AuthorsNamesList.update(listAuxiliar)

G.add_nodes_from(AuthorsNamesList, type='user')
# plt.figure(figsize=(8, 8))
# nx.draw_networkx(G)
# plt.show()
# --------------------------------------
# -------------- 2a ETAPA --------------
#  ADICIONANDO NÓS DO TIPO POST
for index, item in CommentsDataset.iterrows():  # Interacao entre as instancias do dataframe(indice, linha)
    qtdViews = int(item['views'].strip(' views'))  # variavel c a qtd de visualizacoes do post
    itemId = item['link'].strip("/community/default.aspx?f=19&m=")  # o codigo do post sera o label do nó
    # print(itemId, qtdViews)
    G.add_nodes_from([itemId], title=item['title'], views=qtdViews, type='post')  # ADD NÓS DO TIPO POST
    G.add_node(item['author'], type='user')
    G.add_edges_from([(itemId, item['author'])], type='hasAuthored')  # ADD ARESTAS DO TIPO AUTORIA
# -------------- 3a ETAPA --------------
# for index, item in CommentsDataset.iterrows():  # Interacao entre as instancias do dataframe(indice, linha)
    # ADICIONANDO ARESTAS DO TIPO INTERACAO
    listAuxiliar = [x['commentAuthor'] for x in item["postContent"]]  # list of all users who interacts within post/item
    author = item['author']
    listParticipants = list(set(listAuxiliar) - set([author]))  # set of users except the author
    G.add_nodes_from(listParticipants, type='user')
    edgeCombinations = itertools.product([itemId], listParticipants, repeat=1)
    G.add_edges_from(edgeCombinations, type='Interacts')  # ADD ARESTAS DO TIPO INTERAGE
# -----
l1 = [v for v in list(G.nodes()) if G.nodes[v]['type'] == 'user']  # lista de nos do tipo usuario
l2 = [v for v in list(G.nodes()) if G.nodes[v]['type'] == 'post']  # lista de nos do tipo post
l3 = [v for v in list(G.edges()) if G.edges[v]['type'] == 'hasAuthored']
l4 = [v for v in list(G.edges()) if G.edges[v]['type'] == 'Interacts']

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=l1, node_color='r', node_size=3, alpha=.5)
nx.draw_networkx_nodes(G, pos, nodelist=l2, node_color='b', node_size=.65)
nx.draw_networkx_edges(G, pos, edgelist=l3, edge_color='purple', alpha=.5)
nx.draw_networkx_edges(G, pos, edgelist=l4, edge_color='green', alpha=.3)

plt.show()
# -----------------------
x = [c for c in sorted(nx.connected_components(G), key=len, reverse=True)]
GComponent = G.subgraph(x[0])
# -----------------
jsonGraph = nx.node_link_data(GComponent)
with open('graph.json', 'w') as file:
    json.dump(jsonGraph, file)  # WRITING A JSON FILE OF THE SUBGRAPH
# -----------------
# READING A JSON FILE OF THE SUBGRAPH
with open('graph.json') as file:
    data = json.load(file)

H = json_graph.node_link_graph(data)

pos = nx.spring_layout(H)
nx.draw_networkx(H)
l1 = [v for v in list(H.nodes()) if H.nodes[v]['type'] == 'user']  # lista de nos do tipo usuario
l2 = [v for v in list(H.nodes()) if H.nodes[v]['type'] == 'post']  # lista de nos do tipo post
l3 = [v for v in list(H.edges()) if H.edges[v]['type'] == 'hasAuthored']
l4 = [v for v in list(H.edges()) if H.edges[v]['type'] == 'Interacts']

nx.draw_networkx_nodes(H, pos=pos, nodelist=l1, node_color='r', node_size=3, alpha=.5)
nx.draw_networkx_nodes(H, pos=pos, nodelist=l2, node_color='b', node_size=.65)
nx.draw_networkx_edges(H, pos=pos, edgelist=l3, edge_color='purple', alpha=.5)
nx.draw_networkx_edges(H, pos=pos, edgelist=l4, edge_color='green', alpha=.3)
plt.show()

