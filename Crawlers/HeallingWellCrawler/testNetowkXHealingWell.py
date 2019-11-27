import networkx as nx
import json
import pandas as pd
import matplotlib.pyplot as plt

with open("Crawlers/HeallingWellCrawler/testHealingWellThreads.json", 'r') as f:
    dataset = json.load(f)
    dataset = pd.DataFrame(dataset)

listOfUsers = dataset['author'].unique()
listOfPosts = dataset['link'].unique()

# criando grafo e nós
G = nx.digraph()
G.add_nodes_from(listOfUsers, type='user')

for index, item in dataset.iterrows():
    qtdViews = item['views'].strip(' views')
    itemId = item['link'].strip("/community/default.aspx?f=19&m=")
    # print(itemId, qtdViews)
    G.add_nodes_from([itemId], title=item['title'], views=qtdViews, type='post', node_color="r")

# ------
links = list(dataset['link'].str.strip("/community/default.aspx?f=19&m="))
authors = list(dataset.loc[:, 'author'])

edgesList = list(zip(authors, links))

G.add_edges_from(edgesList)

nx.draw_networkx_edges(G)
plt.show()