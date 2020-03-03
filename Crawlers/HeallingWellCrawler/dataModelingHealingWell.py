import networkx as nx
# import json
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import jsonlines
# import pandas as pd
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
AuthorsNamesList = []
for thread in range(len(CommentsDataset)):
    listAuxiliar = [x['commentAuthor']
                    for x in CommentsDataset.loc[thread, "postContent"]]  # list comprehension
    # AuthorsNamesList.remove(-1)

    AuthorsNamesList.append(listAuxiliar)

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
edge_color = ['purple', 'green']

nx.draw(G,
        font_size=5,
        node_size=10,
        node_color=edge_color,
        edge_color=edge_color)#,
        # edge_alpha=.5)
plt.show()
# -----------------
# SEGUNDO EXEMPLO DE MODELAGEM
# -----------------
A = nx.nx_agraph.to_agraph(G2)
A.write('HWgraph.dot')
nx.drawing.nx_agraph.write_dot(G2, 'HWgraphexample.dot')
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

nx.draw_kamada_kawai(G2, 
                #  node_color='orange',
                    node_size=2,
                #  edge_color='black',
                #  font_size=2,
                 with_labels=False)
plt.show()
plt.savefig("HWpgrah.eps")
# -----
