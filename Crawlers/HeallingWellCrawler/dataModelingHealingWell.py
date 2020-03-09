import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import jsonlines
# -----------------
'''
Esse modelo de grafo possui 2 tipos de nós, usuarios e posts. Eles sao ligados por relacionamentos
de tipos, criacao e interacao.
'''
# LOADING THE DATASET
commentsList = []
with jsonlines.open("/home/silas/Documents/Silas_Personal_Files/Python-Codes/Crawlers/\
HeallingWellCrawler/HealingWellComments_labCores.jsonl", mode='r') as f:
    for i in f:
        commentsList.extend(i)
CommentsDataset = pd.DataFrame(commentsList)
G = nx.Graph()  # criacao de um objeto q é um grafo
# -----
# ADICIONANDO NÓS DO TIPO USUARIO E POST
AuthorsNamesList = set()
AuthorsNamesList2 = []
for thread in range(len(CommentsDataset)):
    listAuxiliar = [x['commentAuthor']
                    for x in CommentsDataset.loc[thread, "postContent"]]  # list comprehension
    AuthorsNamesList.update(listAuxiliar)
    AuthorsNamesList2.append(listAuxiliar)


for index, item in CommentsDataset.iterrows():
    qtdViews = item['views'].strip(' views')
    itemId = item['link'].strip("/community/default.aspx?f=19&m=")  # o codigo do post sera o label do nó
    # print(itemId, qtdViews)
    G.add_nodes_from([itemId], title=item['title'], views=qtdViews, type='post')  # ADD NÓS DO TIPO POST
    G.add_edges_from([(itemId, item['author'])], type='hasAuthored', color='purple')  # ADD ARESTAS DO TIPO AUTORIA

    # ADICIONANDO ARESTAS DO TIPO INTERAGE
    listAuxiliar = [x['commentAuthor'] for x in item["postContent"]]  # list of all users who interacts within post/item
    author = item['author']
    listParticipants = list(set(listAuxiliar) - set([author]))  # set of users except the author
    G.add_nodes_from(listAuxiliar, type='user')
    edgeCombinations = itertools.product([itemId], listParticipants, repeat=1)
    G.add_edges_from(edgeCombinations, type='Interacts', color='green')  # ADD ARESTAS DO TIPO INTERAGE
# -----
G.nodes.data()
node_color = {'user': 'blue', 'post': 'red'}
edge_color = {'hasAuthored': 'purple', 'Interacts': 'green'}
# -----
l = [v for v in list(G.nodes()) if G.nodes[v]['type'] == 'user']
l2 = [v for v in list(G.nodes()) if G.nodes[v]['type'] == 'post']

l3 = [v for v in list(G.edges()) if G.edges[v]['type'] == 'hasAuthored']
l4 = [v for v in list(G.edges()) if G.edges[v]['type'] == 'Interacts']

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=l, node_color='r', node_size=3)
nx.draw_networkx_nodes(G, pos, nodelist=l2, node_color='b', node_size=7)
nx.draw_networkx_edges(G, pos, edgelist=l3, edge_color='purple', alpha='.85')
nx.draw_networkx_edges(G, pos, edgelist=l4, edge_color='green')

plt.show()
# -----------------
# SEGUNDO EXEMPLO DE MODELAGEM
# -----------------
A = nx.nx_agraph.to_agraph(G)
A.write('HWgraph.dot')
nx.drawing.nx_agraph.write_dot(G, 'HWgraphexample.dot')
# -----
# - setting the graph layout
# pos = nx.spring_layout(G2)
# nx.draw(G2, pos, with_labels=False)
# for p in pos:  # raise text positions
#     pos[p][1] += 0.07

# nx.draw_networkx_labels(G2, pos, node_size=2,
#                                  font_color='r',
#                                  font_size=7,
#                                  font_weight='bold')

# nx.draw_kamada_kawai(G2, 
#                 #  node_color='orange',
#                     node_size=2,
#                 #  edge_color='black',
#                 #  font_size=2,
#                  with_labels=False)
# plt.show()
# plt.savefig("HWpgrah.eps")
# -----
