'''
Tools to find the polarity or to perform the sentiment analysis:
 - TextBlob
 - NLTK-Vader
'''

from gensim import corpora, models
from pprint import pprint
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
dictionary = gensim.corpora.Dictionary(processed_docs)  # salvo como um objeto gensim Dictionary a lista das palavras preprocessadas

count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 10:
        break

dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
dictionary.save('HWdictionary.dict')  # save dict to disk
# bow_corpus = [dictionary.doc2bow(doc) for doc in CommentsDataset.loc[:, 'postDocumentCorpus']]
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]  # salvo o dicionario num BoW
gensim.corpora.MmCorpus.serialize('bow_corpus.mm', bow_corpus)  # save corpus to disk

# bow_doc_3074 = bow_corpus[0]
# for i in range(len(bow_doc_3074)):
#     print("Word {} (\"{}\") appears {} time.".format(bow_doc_3074[i][0],
#                                                      dictionary[bow_doc_3074[i][0]],
#                                                      bow_doc_3074[i][1]))
# ------------------------------------------------------
# LOADING THE CORPUS AND DICTIONARY
loaded_dict = gensim.corpora.Dictionary.load('HWdictionary.dict')

corpus = gensim.corpora.MmCorpus('bow_corpus.mm')
# ------------------------------------------------------
# TFIDF
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

for doc in corpus_tfidf:
    pprint(doc)
    break

# ------------------------------------------------------
# LDA
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       num_topics=5,
                                       id2word=loaded_dict,
                                       passes=20,
                                       workers=2,
                                       random_state=0)

for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))
lda_model.save('lda_model.model')
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
