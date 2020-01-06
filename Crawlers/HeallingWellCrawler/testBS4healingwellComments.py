# teste com library requests
import requests
# import urllib.request
from bs4 import BeautifulSoup
# pacotes para controlar o tempo de requisicao das paginas
from time import sleep, time
from random import random
# from warnings import warn
from datetime import datetime
import json
import os
# -------------------------------


def timeSleep():
    # - Tempo de espera para outra requisição
    valueTimeToSleep = random() * 3 + 1
    sleep(valueTimeToSleep)  # - Escolhe um inteiro
    print('Have waited {} seconds for a new request'.format(valueTimeToSleep))


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
            commentDict['commentTimestamp'] = datetime.timestamp(commentTimestamp)  # Data Publicac
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
# threadList = []  # Lista que guardara os posts
# dictLayout = dict()

# -----------------------------------
# BUSCANDO COMENTARIOS PARA CADA THREAD
start_time = time()
requestsControl = 0
commentsDictionary = dict()
commentsList = []

with open('Crawlers/HeallingWellCrawler/testHealingWellThreads.json', 'r') as file:
    threadList = json.load(file)
    del threadList[0]

tamanhoListaPosts = len(threadList)
# -----
for postIterator in threadList:
    # Controle da requisicao
    timeSleep()

    # Trecho que faz a requisicao com requests
    postLink = "https://www.healingwell.com" + postIterator['link']  # link de um post da lista
    source = requests.get(postLink)
    soup = BeautifulSoup(source.content)

    # if source.status_code != 200:
    #     warn('request: {}; Status code: {}'.format(requestsControl, source.status_code))

    # # Break the loop if the number of requests is greater than expected
    #     if requestsControl > 72:
    #         warn('Number of requests was greater than expected.')
    #         break

    # Trecho para controlar a paginacao dentro de uma thread
    x = soup.find('div', class_='page-listing-bottom')  # variavel q possui a qtd de paginas do post
    if (x is not None) and (len(x) > 1):  # se x for nao nulo e maior q 1, devo controlar paginacao
        threadListComments = []
        for threadPage in range(1, len(x)+1):
            timeSleep()  # tempo de espera
            postPageLink = "https://www.healingwell.com" + postIterator['link']\
                + '&p={}'.format(threadPage)
            source = requests.get(postPageLink)
            soup = BeautifulSoup(source.content)
            # ---
            print("""Getting information from post: {};
                    The status code was; {} \n""".format(postPageLink, source.status_code))
            # print("\n")

            threadListComments.extend(threadCommentSeekerPagination(soup))

        postIterator['postContent'] = threadListComments

    else:
        comments = threadCommentSeekerPagination(soup)
        postIterator['postContent'] = comments

    # commentsList.extend(postIterator['link'])

    with open('Crawlers/HeallingWellCrawler/testHealingWellComments.json', 'a+') as file:
        if os.stat(file.name).st_size <= 3:
            json.dump(postIterator, file, indent=4, sort_keys=True)
        else:
            file.write(',')
            json.dump(postIterator, file, indent=4, sort_keys=True)

    tamanhoListaPosts = tamanhoListaPosts - 1
    print(tamanhoListaPosts)
