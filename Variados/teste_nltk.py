import nltk
nltk.download()
#-------------
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_test = '''Hello Mr. Smith, how are you doing today? The weather \
    is great, and Python is awesome. \
    The sky is pinkish-blue. You shouldn't eat cardboard.'''

print(word_tokenize(example_test))
print(sent_tokenize(example_test))

for i in word_tokenize(EXAMPLE_TEXT):
    print(i)
#-----------------------
# Part 2
example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

for i in stop_words:
    print(i)

words = word_tokenize(example_sentence)
#
# filtered_sentence = []
#
# for w in words:
#     if w not in stopwords:
#         filtered_sentence.append(w)
#
# print(filtered_sentence)

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)
## stop_words em portugues
stop_words_pt = set(stopwords.words("portuguese"))


filtere
