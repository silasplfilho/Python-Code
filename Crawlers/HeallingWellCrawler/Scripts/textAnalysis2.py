'''
Tools to find the polarity or to perform the sentiment analysis:
 - TextBlob
 - NLTK-Vader
'''
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
import pandas as pd
import jsonlines
import json
from textblob import TextBlob

from gensim.utils import simple_preprocess
# Libraries for text preprocessing
from nltk.stem import WordNetLemmatizer, SnowballStemmer
stemmer = SnowballStemmer("english")

# ------------------------------------------------------
with open('graph.json') as file:
    data = json.load(file)

H = json_graph.node_link_graph(data)

l1 = [v for v in list(H.nodes()) if H.nodes[v]['type'] == 'user']  # lista de nos do tipo usuario
l2 = [v for v in list(H.nodes()) if H.nodes[v]['type'] == 'post']  # lista de nos do tipo post
l3 = [v for v in list(H.edges()) if H.edges[v]['type'] == 'hasAuthored']  # lista de arestas do tipo autoria
l4 = [v for v in list(H.edges()) if H.edges[v]['type'] == 'Interacts']  # lista de arestas do tipo interage

# ------------------------------------------------------
# PLOTTING THE GRAPH
pos = nx.spring_layout(H)
# pos = nx.fruchterman_reingold_layout(H)
# pos = nx.kamada_kawai_layout(H)

nx.draw_networkx_nodes(H, pos=pos, nodelist=l1, node_color='red', node_size=2, alpha=.5)
nx.draw_networkx_nodes(H, pos=pos, nodelist=l2, node_color='blue', node_size=3, alpha=.65)
nx.draw_networkx_edges(H, pos=pos, edgelist=l3, edge_color='purple', alpha=.5)
nx.draw_networkx_edges(H, pos=pos, edgelist=l4, edge_color='green', alpha=.1)
plt.show()

# ------------------------------------------------------
# LOADING THE DATASET
commentsList = []
with jsonlines.open("/home/silas/Documents/Silas_Personal_Files/Python-Codes/Crawlers/\
HeallingWellCrawler/HealingWellComments_labCores.jsonl", mode='r') as f:
    for i in f:
        commentsList.extend(i)
CommentsDataset = pd.DataFrame(commentsList)
CommentsDataset['postDocumentCorpus'] = ""
CommentsDataset['titlePolarity'] = ""
# -----
stopwords = stopwords.words("english")

# ------------------------------------------------------
# DISCOVER THE POLARITY OF POSTS TITLES
for itemIndex in range(0, len(CommentsDataset)):
    titleTxtBlob = TextBlob(CommentsDataset.loc[itemIndex, 'title'])
    CommentsDataset.loc[itemIndex, 'titlePolarity'] = titleTxtBlob.sentiment.polarity

titlePolarityList = sorted(CommentsDataset['titlePolarity'])

sns.distplot(titlePolarityList, hist=True, kde_kws={"shade": True, "color": "y", "alpha": .5}, bins=25)
plt.xlabel("Post Title Polarity")
plt.show()

# ------------------------------------------------------
# DISCOVER THE POLARITY OF POST TEXTS
for itemIndex in range(0, len(CommentsDataset)):
    postContent = CommentsDataset.loc[itemIndex, 'postContent']  # conteudo de texto de um post - item i do dataset
    postAuthorTxtBlob = TextBlob(postContent[0]['comment'])  # texto do autor do post - 1o elemento

    postIndex = CommentsDataset.loc[itemIndex, 'link'].strip("/community/default.aspx?f=19&m=")  # identificador do post - link
    authorPostPolarity = postAuthorTxtBlob.sentiment.polarity  # valor da polaridade do texto do autor
    if postIndex in l2:  # um post pode nao estar no grafo utilizado(q é o componente gigante), pois pode ser um post com apenas o autor
        H.nodes[postIndex]['polarity'] = authorPostPolarity
    else:
        continue


elementsL2 = [round(H.nodes[lj2]['polarity'], 4) for lj2 in l2]  # testando o uso de indice para selecionar elementos do grafo
sorted(elementsL2)[0]
sns.distplot(elementsL2, hist=True, kde_kws={"shade": True, "color": "y", "alpha": .5}, bins=40)

plt.xlabel("Author Text Polarity")
plt.show()


# ------------------------------------------------------
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    result = []
    for token in simple_preprocess(text):
        if token not in stopwords and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result
# ------------------------------------------------------


for indexController in range(0, len(CommentsDataset)):
    postDocument = []
    content = CommentsDataset.loc[indexController, 'postContent']
    for y in content:
        auxList = y['comment'].split(' ')
        postDocument.extend(auxList)
        CommentsDataset.at[indexController, 'postDocumentCorpus'] = postDocument

a = [preprocess(word) for word in CommentsDataset.loc[0, 'postDocumentCorpus'] if preprocess(word) != []]
# ------------------------------------------------------
processed_docs = CommentsDataset['postDocumentCorpus'].astype(str).apply(preprocess)

CommentsDataset.loc[450, 'postContent'][0]['comment']
txtBlob = TextBlob(CommentsDataset.loc[450, 'postContent'][0]['comment'])
txtBlob.sentiment
