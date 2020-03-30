'''
Tools to find the polarity or to perform the sentiment analysis:
 - TextBlob
 - NLTK-Vader
'''
from nltk.corpus import stopwords
from nltk.stem.porter import *
import pandas as pd
import jsonlines
from textblob import TextBlob

from gensim.utils import simple_preprocess
# Libraries for text preprocessing
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
stopwords = stopwords.words("english")
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
txtBlob= TextBlob(CommentsDataset.loc[450, 'postContent'][0]['comment'])
txtBlob.sentiment