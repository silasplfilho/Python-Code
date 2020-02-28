import networkx as nx
# import json
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import jsonlines

import pandas as pd
# -----------------
# threadList=[]
# with jsonlines.open("Crawlers/HeallingWellCrawler/HealingWellThreads.jsonl", mode='r') as f:
#     for i in f:
#         threadList.extend(i)
#     # dataset = json.load(threadList)
# dataset = pd.DataFrame(threadList)
# dataset.columns
# # dataset.head()
# listOfUsers = list(dataset['author'].unique())

# # # criando grafo e nós
# G = nx.Graph()
# G.add_nodes_from(listOfUsers, type='user')

# for index, item in dataset.iterrows():
#     qtdViews = item['views'].strip(' views')
#     itemId = item['link'].strip("/community/default.aspx?f=19&m=")
#     # print(itemId, qtdViews)
#     G.add_nodes_from([itemId], title=item['title'], views=qtdViews, type='post')

# # # -----------------
# links = list(dataset['link'].str.strip("/community/default.aspx?f=19&m="))
# authors = list(dataset.loc[:, 'author'])
# edgesList = list(zip(authors, links))

# G.add_edges_from(edgesList)

# color_map = {'user': 'b', 'post': 'r'}
# nx.draw_networkx(G, with_labels=False, node_size=2, node_color=[color_map[G.nodes[node]['type']] for node in G])
# plt.show()

# Exsportando para dot - formato do graphviz
# nx.drawing.nx_pydot.write_dot(G, "Crawlers/HeallingWellCrawler/graphModel1.gv")
# from graphviz import render, Graph
# gG = Graph('Crawlers/HeallingWellCrawler/graphModel1.dot')
# gG.view()
# -----------------
# SEGUNDO EXEMPLO DE MODELAGEM
# -----------------
G2 = nx.Graph()
commentsList = []
with jsonlines.open("/home/silas/Documents/Silas_Personal_Files/Python-Codes/Crawlers/HeallingWellCrawler/HealingWellComments_labCores.jsonl", mode='r') as f:
    for i in f:
        commentsList.extend(i)

CommentsDataset = pd.DataFrame(commentsList)
AuthorsNamesList = []

# CommentsDataset.iloc[0,]

for thread in range(len(CommentsDataset)):
    listAuxiliar = [x['commentAuthor'] for x in CommentsDataset.loc[thread, "postContent"]]  # list comprehension
    # AuthorsNamesList.remove(-1)
    # del listAuxiliar[0]
    AuthorsNamesList.append(listAuxiliar)

a = itertools.combinations(AuthorsNamesList[0], 2)

for elem in AuthorsNamesList:
    auxList = itertools.combinations(elem, 2)
    G2.add_edges_from(auxList)

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

nx.draw_spectral(G2, 
                #  node_color='orange',
                 node_size=2,
                #  edge_color='black',
                #  font_size=2,
                 with_labels=False,
                 pos=nx.spring_layout(G2))
plt.show()
plt.savefig("HWpgrah.eps")
# -----
degreeList = pd.DataFrame.from_dict(nx.degree_centrality(G2), orient='index', columns=[
                                    'value']).sort_values(by=['value'], ascending=False)
closeList = pd.DataFrame.from_dict(nx.closeness_centrality(
    G2), orient='index', columns=['value']).sort_values(by=['value'], ascending=False)
betweenList = pd.DataFrame.from_dict(nx.betweenness_centrality(
    G2), orient='index', columns=['value']).sort_values(by=['value'], ascending=False)
# -
d = {'Degree': degreeList.head().value.reset_index()['value'],
     'Closeness': closeList.head().value.reset_index()['value'],
     'Betweeness': betweenList.head().value.reset_index()['value']}

resultsDF = pd.DataFrame.from_dict(d, orient='columns')
# -
pd.options.display.float_format = '{:.2E}'.format

d2 = {'Degree': degreeList.tail().value.reset_index()['value'],
      'Closeness': closeList.tail().value.reset_index()['value'],
      'Betweeness': betweenList.tail().value.reset_index()['value']}

resultsDF = pd.DataFrame.from_dict(d2, orient='columns')
print(resultsDF.to_latex())
