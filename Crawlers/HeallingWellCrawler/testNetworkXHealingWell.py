import networkx as nx
import json
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import jsonlines
# -----------------
# with open("Crawlers/HeallingWellCrawler/testHealingWellThreads.json", 'r') as f:
#     dataset = json.load(f)
#     dataset = pd.DataFrame(dataset)

# listOfUsers = list(dataset['author'].unique())

# # criando grafo e nós
# G = nx.Graph()
# G.add_nodes_from(listOfUsers, type='user')

# for index, item in dataset.iterrows():
#     qtdViews = item['views'].strip(' views')
#     itemId = item['link'].strip("/community/default.aspx?f=19&m=")
#     # print(itemId, qtdViews)
#     G.add_nodes_from([itemId], title=item['title'], views=qtdViews, type='post')

# # -----------------
# links = list(dataset['link'].str.strip("/community/default.aspx?f=19&m="))
# authors = list(dataset.loc[:, 'author'])
# edgesList = list(zip(authors, links))

# G.add_edges_from(edgesList)

# color_map = {'user': 'b', 'post': 'r'}
# nx.draw(G, with_labels=True, node_color=[color_map[G.nodes[node]['type']] for node in G])
# plt.show()
# -----------------
# SEGUNDO EXEMPLO DE MODELAGEM
# -----------------
G2 = nx.Graph()
commentsList = []
with jsonlines.open("Crawlers/HeallingWellCrawler/HealingWellComments.jsonl", mode='r') as f:
    for i in f:
        commentsList.extend(i)
    # CommentsDataset = json.load(f)
    # CommentsDataset = pd.DataFrame(CommentsDataset)

AuthorsNamesList = []

for thread in CommentsDataset:
    listAuxiliar = [x['commentAuthor'] for x in thread['postContent']]  # list comprehension
    # AuthorsNamesList.remove(-1)
    # del listAuxiliar[0]
    AuthorsNamesList.append(listAuxiliar)

a = itertools.combinations(AuthorsNamesList[0], 2)

for elem in AuthorsNamesList:
    auxList = itertools.combinations(elem, 2)
    G2.add_edges_from(auxList)

pos = nx.spring_layout(G2)
nx.draw(G2, pos, with_labels=False)
for p in pos:  # raise text positions
    pos[p][1] += 0.07

nx.draw_networkx_labels(G2, pos, node_size=100,
                                 font_color='r',
                                 font_size=7,
                                 font_weight='bold')
                                 
# nx.draw(G2, node_color='orange', node_size=100, edge_color='black', linewidths=1, font_size=15)
plt.show()

# -------------------
nx.degree_centrality(G2)
nx.closeness_centrality(G2)
nx.betweenness_centrality(G2)
