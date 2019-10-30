import urllib.request
from bs4 import BeautifulSoup
import re
# ----
mainURL = "https://www.healingwell.com/community/default.aspx?f=19"
source = urllib.request.urlopen(mainURL).read()
soup = BeautifulSoup(source, 'html.parser')

paging = soup.find("div", class_='page-listing-bottom')
lastPage = paging.findAll('a')[-1].get('href')
pageNumber = int(lastPage.split('p=')[-1]) # numero da ultima pagina da comunidade analisada

# criando uma lista, onde cada elemento é um dicionario/thread
threadList = []  # Lista que guardara os posts
dictLayout = dict()


for pageIterator in range(3):
    # definindo parametros a serem manipulados
    URL = "https://www.healingwell.com/community/default.aspx?f=19&p={}".format(pageIterator)
    source = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(source, 'html.parser')

    # ---
    # tentando chegar direto no div que tem a informacao necessaria
    focusedDiv = soup.find('div', class_='section-body-secondary')

    threadDiv = soup.findAll('div', class_=re.compile("row fugazi forum-list"))
    threadDiv[0].text.replace('^\n', '')

    threadDiv[0].text
    threadDiv[0].find('a', class_='forum-title').get('href')

    # ---
    for thread in threadDiv:
        dictLayout['last_date'] = thread.find('div', class_='last-comment-date').text
        dictLayout['author'] = thread.p.text
        dictLayout['title'] = thread.a.text
        dictLayout['views'] = thread.find('div', class_='views').text
        dictLayout['link'] = thread.find('a', class_='forum-title').get('href')
        print(dictLayout)
        threadList.append(dictLayout.copy())


threadComments = []
commentDict = dict()

for postIterator in threadList:
    postLink = postIterator['link']
    source = urllib.request.urlopen(postLink).read()
    soup = BeautifulSoup(source, 'html.parser')

    # comentarios e timestamp do post
    comments = soup.findAll('div', class_='post-body')
    commentsPostDate = soup.findAll('div', class_='posted')

    # postIterator['comment'] = 
    # commentDict['comment'] = 

    for i, j in zip(comments, commentsPostDate):
    print("__________JA ACABOU JESSICA")
    print(j.text)
    print(i.text)

# ---------------------------
postLink = threadList[0]['link']
postLink = "https://www.healingwell.com"+ postLink
source = urllib.request.urlopen(postLink).read()
soup = BeautifulSoup(source, 'html.parser')

comments = soup.find('div', class_='post-body')

while comments.findNext('div', class_='post-body') is not None:
    commentBody = comments.text.split('\r\n')[1]
    comments = comments.findNext('div')






commentsPostDate = soup.find('div', class_='posted').text




# ----------------------------
source = urllib.request.urlopen(postLink).read()
soup = BeautifulSoup(source, 'html.parser')
# /community/default.aspx?f = 19 & m = 4141476
# ---
# tentando chegar direto no div que tem a informacao necessaria
focusedDiv = soup.find('div', class_='section-body-secondary')

threadDiv = soup.findAll('div', class_=re.compile("row fugazi forum-list"))
threadDiv[0].text.replace('^\n', '')

threadDiv[0].text
threadDiv[0].find('a', class_='forum-title').get('href')
# ---
# criando uma lista, onde cada elemento é um dicionario/thread
threadList = []
dictLayout = dict()

for thread in threadDiv:
    dictLayout['last_date'] = thread.find('div', class_='last-comment-date').text
    dictLayout['author']    = thread.p.text
    dictLayout['title']     = thread.a.text
    dictLayout['views']     = thread.find('div', class_='views').text
    dictLayout['link']      = thread.find('a', class_='forum-title').get('href')
    print(dictLayout)
    threadList.append(dictLayout.copy())



threadList[0]
threadList[0]['link']

paging_link = paging[0].find_all('a', {'class': 'paging__link'})
last_page = int([item.get('href').split('/')[-1] for item in paging_link][-1])
