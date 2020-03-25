import pandas as pd
import jsonlines
import numpy as np
# Libraries for text preprocessing
import gensim
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
stemmer = SnowballStemmer("english")

# ------------------------------------------------------
# LOADING THE DATASET
commentsList = []
with jsonlines.open("/home/silas/Documents/Silas_Personal_Files/Python-Codes/Crawlers/\
HeallingWellCrawler/HealingWellComments_labCores.jsonl", mode='r') as f:
    for i in f:
        commentsList.extend(i)
CommentsDataset = pd.DataFrame(commentsList)
CommentsDataset['postDocumentCorpus'] = ""
# -----
from nltk.stem.porter import *
np.random.seed(2018)
from nltk.corpus import stopwords
nltk.download('wordnet')
stopwords = stopwords.words("english")
# ------------------------------------------------------


def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in STOPWORDS or token not in stopwords and len(token) > 3:
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
# ------------------------------------------------------
# dictionary = gensim.corpora.Dictionary(CommentsDataset.loc[:, 'postDocumentCorpus'])
dictionary = gensim.corpora.Dictionary(processed_docs)

count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 10:
        break

dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
# bow_corpus = [dictionary.doc2bow(doc) for doc in CommentsDataset.loc[:, 'postDocumentCorpus']]
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# bow_doc_3074 = bow_corpus[0]
# for i in range(len(bow_doc_3074)):
#     print("Word {} (\"{}\") appears {} time.".format(bow_doc_3074[i][0],
#                                                      dictionary[bow_doc_3074[i][0]],
#                                                      bow_doc_3074[i][1]))


# ------------------------------------------------------
# TFIDF

from gensim import corpora, models
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

from pprint import pprint
for doc in corpus_tfidf:
    pprint(doc)
    break


# ------------------------------------------------------
# LDA

lda_model = gensim.models.LdaMulticore(
    bow_corpus, num_topics=5, id2word=dictionary, passes=20, workers=2)

for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))

# ------------------------------------------------------
# Running LDA using TF-IDF

lda_model_tfidf = gensim.models.LdaMulticore(
    corpus_tfidf, num_topics=5, id2word=dictionary, passes=20, workers=4)

for idx, topic in lda_model_tfidf.print_topics(-1):
    print('Topic: {} Word: {}'.format(idx, topic))


# Performance evaluation by classifying sample document using LDA Bag of Words model
for index, score in sorted(lda_model[bow_corpus[0]], key=lambda tup: -1*tup[1]):
    print("\nScore: {}\t \nTopic: {}".format(
        score, lda_model.print_topic(index, 10)))
