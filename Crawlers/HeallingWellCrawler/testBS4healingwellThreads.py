# teste com library requests
import requests
# import urllib.request
from bs4 import BeautifulSoup
import re
# pacotes para controlar o tempo de requisicao das paginas
from time import sleep, time
from random import random
# from warnings import warn
from datetime import datetime
import json
# -------------------------------


def timeSleep():
    # - variaveis para controle de tempo/sleep
    start_time = time()
    requestsControl = 0

    # - Tempo de espera para outra requisição
    requestsControl += 1
    sleep(random() * 3 + 1)  # - Escolhe um inteiro
    current_time = time()
    elapsed_time = current_time - start_time

    print('Request: {}; Frequency: {} requests/s'.format(requestsControl,
                                                         requestsControl/elapsed_time))


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

for pageIterator in range(1, 5):  # define um range de paginas-a ideia seria substituir pela variavel 
                               # 'pageNumber' q é a qtd total de paginas
    # definindo parametros a serem manipulados
    threadURL = "https://www.healingwell.com/community/default.aspx?f=19&p={}".format(pageIterator)
    source = requests.get(threadURL)
    soup = BeautifulSoup(source.content)
    # ---
    # tentando chegar direto no div que tem a informacao necessaria
    threadDiv = soup.findAll('div', class_=re.compile("row fugazi forum-list"))
    threadDiv[0].text.replace('^\n', '')
    threadDiv[0].find('a', class_='forum-title').get('href')

    # ---
    for thread in threadDiv:
        dictLayout['last_date'] = thread.find('div', class_='last-comment-date').text
        dictLayout['author'] = (thread.p.text).split("By ")[1]
        dictLayout['title'] = thread.a.text
        dictLayout['views'] = thread.find('div', class_='views').text
        dictLayout['link'] = thread.find('a', class_='forum-title').get('href')
        threadList.append(dictLayout.copy())


with open('Crawlers/HeallingWellCrawler/testHealingWellThreads.json', 'a+') as file:
    print("Saving the ")
    json.dump(threadList, file, indent=4, sort_keys=True)

