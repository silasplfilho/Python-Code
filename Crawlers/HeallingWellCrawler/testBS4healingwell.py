# teste com library requests
import requests

# import urllib.request
from bs4 import BeautifulSoup
import re

# pacotes para controlar o tempo de requisicao das paginas
from time import sleep, time
from random import random

from IPython.core.display import clear_output
from warnings import warn
from datetime import datetime
import json
# -------------------------------
# funcao para buscar comentarios


def threadCommentSeekerPagination(soupVariable):
    # autor, timestamp e comentarios do post
    smthng = soupVariable.findAll(['a', 'div'], class_=['user-name', 'post-body', 'posted'])
    threadComments = []
    commentDict = dict()

    for i in range(0, len(smthng), 3):
        commentDict['commentAuthor'] = smthng[i].text  # Autor do Comentario
        commentDict['comment'] = str(smthng[i+2].text).strip()  # Texto do Comentario
        # treating the timestamp string
        try:
            commentTimestamp = (smthng[i+1].text).strip("Posted ")
            timestamp_idx = commentTimestamp.find(" (GMT")
            commentTimestamp = commentTimestamp[:timestamp_idx]
            commentTimestamp = datetime.strptime(commentTimestamp, '%m/%d/%Y %I:%M %p')
            commentDict['commentTimestamp'] = datetime.timestamp(commentTimestamp)  # Data da publicacao
        except Exception:
            commentDict['commentTimestamp'] = (smthng[i+1].text).strip("Posted ")

        threadComments.append(commentDict.copy())

    return threadComments


# ----
mainURL = "https://www.healingwell.com/community/default.aspx?f=19"
source = requests.get(mainURL)
soup = BeautifulSoup(source.content)

paging = soup.find("div", class_='page-listing-bottom')
lastPage = paging.findAll('a')[-1].get('href')
pageNumber = int(lastPage.split('p=')[-1])  # numero da ultima pagina da comunidade analisada

# criando uma lista, onde cada elemento é um dicionario/thread
threadList = []  # Lista que guardara os posts
dictLayout = dict()

for pageIterator in range(2):
    # definindo parametros a serem manipulados
    threadURL = "https://www.healingwell.com/community/default.aspx?f=19&p={}".format(pageIterator)
    source = requests.get(threadURL)
    soup = BeautifulSoup(source.content)
    # ---
    # tentando chegar direto no div que tem a informacao necessaria
    # focusedDiv = soup.find('div', class_='section-body-secondary')
    threadDiv = soup.findAll('div', class_=re.compile("row fugazi forum-list"))
    threadDiv[0].text.replace('^\n', '')
    # threadDiv[0].text
    threadDiv[0].find('a', class_='forum-title').get('href')

    # ---
    for thread in threadDiv:
        dictLayout['last_date'] = thread.find('div', class_='last-comment-date').text
        dictLayout['author'] = (thread.p.text).split("By ")[1]
        dictLayout['title'] = thread.a.text
        dictLayout['views'] = thread.find('div', class_='views').text
        dictLayout['link'] = thread.find('a', class_='forum-title').get('href')
        # print(dictLayout)
        threadList.append(dictLayout.copy())
# -----------------------------------
with open('bs4Test/testHealingWellThreads.json', 'w') as file:
    json.dump(threadList, file)
# -----------------------------------
# BUSCANDO COMENTARIOS PARA CADA THREAD
start_time = time()
requestsControl = 0

for postIterator in threadList:
    # Controle da requisicao
    requestsControl += 1
    sleep(random() * 3 + 1)  # Escolhe um inteiro
    current_time = time()
    elapsed_time = current_time - start_time
    # ---

    # Trecho que faz a requisicao com requests
    postLink = "https://www.healingwell.com" + postIterator['link']
    source = requests.get(postLink)
    soup = BeautifulSoup(source.content)
    # ---
    print("Getting information from post: {}; The status code was; {}".format(postLink,
                                                                              source.status_code))
    print('Request: {}; Frequency: {} requests/s'.format(requestsControl,
                                                         requestsControl/elapsed_time))
    print("\n")
    clear_output(wait=True)

    if source.status_code != 200:
        warn('request: {}; Status code: {}'.format(requestsControl, source.status_code))

    # Break the loop if the number of requests is greater than expected
        if requestsControl > 72:
            warn('Number of requests was greater than expected.')
            break

    # Trecho para controlar a paginacao dentro de uma thread
    x = soup.find('div', class_='page-listing-bottom')
    if (x is not None) and (len(x) > 1):
        threadListComments = []
        for threadPage in range(1, len(x)+1):
            # print(threadPage)
            requestsControl += 1
            sleep(random() * 3 + 1)  # Escolhe um inteiro
            current_time = time()
            elapsed_time = current_time - start_time

            postLink = "https://www.healingwell.com" + postIterator['link']\
                + '&p={}'.format(threadPage)
            source = requests.get(postLink)
            soup = BeautifulSoup(source.content)

            # ---
            print("""Getting information from post: {};
                    The status code was; {}""".format(postLink, source.status_code))
            print('Request: {}; Frequency: {} requests/s'.format(requestsControl,
                                                                 requestsControl/elapsed_time))
            print("\n")

            threadListComments.extend(threadCommentSeekerPagination(soup))

        postIterator['postContent'] = threadListComments

    else:
        comments = threadCommentSeekerPagination(soup)
        postIterator['postContent'] = comments
# ------------------------
with open('bs4Test/testHealingWell2.json', 'w') as file:
    json.dump(threadList, file)
# ------------------------
# TESTES P BAIXO
# dateexe = 'Posted 10/27/2019 1:43 AM (GMT -7)'
# dateexe = dateexe.strip("Posted by ")
# timestamp_idx = dateexe.find(" (GMT")
# dateexe = dateexe[:timestamp_idx]

# x = datetime.strptime(dateexe, '%m/%d/%Y %I:%M %p')
# datetime.timestamp(x)


# smthng = soup.findAll('div', class_='posted')
# (smthng.text)[:26].strip("Posted by ")

#     threadComments = []
#     commentDict = dict()
# ------------------------
# print(postIterator['postContent'])
# len(postIterator)
# threadList[0]
# ['postContent']
# ---------------------------
# threadList[0]['last_date']
# len(threadList)
# with open('bs4Test/testHealingWell.json', 'w') as file:
#     json.dump(threadList, file)
# type(threadList)


# ---------------------------
# limpar espacos em branco
# acrescentar metadados dos comentarios
# threadListComments = []
# for threadPage in range(1, len(x)+1):
#     # print(threadPage)
#     requestsControl += 1
#     sleep(randint(3, 7))  # Escolhe um inteiro
#     current_time = time()
#     elapsed_time = current_time - start_time

#     postLink = "https://www.healingwell.com" + postIterator['link']\
#                 + '&p={}'.format(threadPage)
#     source = requests.get(postLink)
#     soup = BeautifulSoup(source.content)

#     # ---
#     print("""Getting information from post: {};
#             The status code was; {}""".format(postLink, source.status_code))
#     print('Request: {}; Frequency: {} requests/s'.format(requestsControl,
#                                                          requestsControl/elapsed_time))
#     print("\n")

#     # comments = threadCommentSeekerPagination(soup)
#     threadListComments.extend(threadCommentSeekerPagination(soup))

# len(threadListComments)
# threadListComments[-1]
# postIterator['postContent'].append(threadListComments)
