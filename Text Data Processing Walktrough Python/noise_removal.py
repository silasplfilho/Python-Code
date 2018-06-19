#--------------- Needed Packages
import re, string, unicodedata
import nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
#---------------
# tirando as partes de texto que são da linguagem HTML
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return(soup.get_text())

# removendo colchetes
def remove_between_square_brackets(text):
    return(re.sub( '\[[^]*\]', '', text ))

# uma funcao que chame as outras funcpes
def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    return(text)
#---------------
sample = open("/home/silas/Python-Codes/Text Data Processing Walktrough Python/sample_text.txt")
sample = sample.read()
sample = denoise_text(sample)
