import networkx as nx
# import igraph

import json
import pandas as pd
import matplotlib.pyplot as plt

with open("Crawlers/HeallingWellCrawler/testHealingWellThreads.json", 'r') as f:
    dataset = json.load(f)
    dataset = pd.DataFrame(dataset)

listOfUsers = list(dataset['author'].unique())

# criando grafo e nós
G = nx.Graph()
G.add_nodes_from(listOfUsers, type='user')

for index, item in dataset.iterrows():
    qtdViews = item['views'].strip(' views')
    itemId = item['link'].strip("/community/default.aspx?f=19&m=")
    # print(itemId, qtdViews)
    G.add_nodes_from([itemId], title=item['title'], views=qtdViews, type='post')

# ------
links = list(dataset['link'].str.strip("/community/default.aspx?f=19&m="))
authors = list(dataset.loc[:, 'author'])
edgesList = list(zip(authors, links))

G.add_edges_from(edgesList)

color_map = {'user': 'b', 'post': 'r'}
nx.draw(G, with_labels=True, node_color=[color_map[G.nodes[node]['type']] for node in G])
plt.show()
# -----------------
G2 = nx.from_pandas_edgelist(dataset, source='author', target='link')
nx.draw_networkx(G2)
plt.show()
