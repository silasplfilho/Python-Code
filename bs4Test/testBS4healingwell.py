import urllib.request
from bs4 import BeautifulSoup
import re
import json
import time
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
        # print(dictLayout)
        threadList.append(dictLayout.copy())
# -----------------------------------

for postIterator in threadList:
    postLink = "https://www.healingwell.com" + postIterator['link']
    source = urllib.request.urlopen(postLink).read()
    soup = BeautifulSoup(source, 'html.parser')

    try:

    except:

    # autor, timestamp e comentarios do post
    smthng = soup.findAll(['a', 'div'], class_=['user-name', 'post-body', 'posted'])

    threadComments = []
    commentDict = dict()

    for i in range(0, len(smthng), 3):
        commentDict['commentAuthor'] = smthng[i].text  # Autor do Comentario
        commentDict['commentTimestamp'] = smthng[i+1].text  # Data da publicacao
        commentDict['comment'] = smthng[i+2].text  # Texto do Comentario

        threadComments.append([commentDict['commentAuthor'],
                               commentDict['commentTimestamp'],
                               commentDict['comment']])

    postIterator['postContent'] = threadComments
    # print(postIterator['postContent'])

# ---------------------------
threadList[0]['last_date']

with open('bs4Test/testHealingWell.json', 'w') as file:
    json.dump(threadList, file)
# type(threadList)


# ---------------------------
