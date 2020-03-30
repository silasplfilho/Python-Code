import networkx as nx
import pandas as pd
import pygraphviz as pgv
# -----
g = pgv.AGraph("HWgraph.dot")
g.draw('asdf', format='png', prog='neato')



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
